import csv
import logging
import os
import random
import typing as t
import uuid
from argparse import ArgumentParser
from collections import defaultdict
from datetime import datetime, timedelta

from django.core.files import File
from django.core.management.base import BaseCommand

from api.models import (Attribute, AttributeProduct, Brand, Category, Color,
                        Discount, InStock, Picture, Product, Section, Size)

log = logging.getLogger(__name__)


SECTION_ACCESSORIES_LST = [
    'Біжутерія та Шпильки',
    'Окуляри',
    'Рюкзаки',
    'Ремені',
    'Рукавиці',
    'Сумочки',
    'Шарфи Та Платки',
    'Шапки',
    'Барсетки та Бананки',
]

SECTION_CHOSE_LST = [
    'Балетки',
    'Гумові сапоги',
    'Еспадрильї, Сліпони, Мокасини',
    'Капці',
    'Кеди',
    'Кросівки',
    'Черевики та Лофери',
    'Чоботи та Пив Чоботи',
    'Шлепанці та Босоніжки',
    'Пінетки',
    'Бутси',
]

SECTION_CLOTHES_LST = [
    'Блузки',
    'Боді',
    'Верхній одяг',
    'Джинсі',
    'Кофті, кардигани',
    'Комбінезони',
    'Комплекти, костюми',
    'Спортивний одяг',
    'Свeтри',
    'Плаття',
    'Піджаки та костюми',
    'Піжами',
    'Футболки',
    'Трикотаж',
    'Шорті',
    'Штані',
    'Спідниці',
    'Шкільна форма',
    'Тематичні костюми',
    'Конверті',
    'Крижми',
    'Одяг для хрещення',
    'Повзунки',
    'Писачники',
    'Подряпки',
    'Чоловічки',
    'Шапочки',
    'Сорочки',
]

BRANDS_LST = [
    "Nike",
    "Adidas",
    "Zara",
    "H&M",
    "Gucci",
    "Louis Vuitton",
    "Chanel",
    "Calvin Klein",
    "Ralph Lauren",
    "Forever 21",
]

COUNTRIES_LST = ['Україна', 'Китай', 'США', 'Італія', 'Туреччина']

DISCOUNT_LST = [5, 10, 15, 20, 25, 30, 35]

NOW = datetime.now()

COLOR_LST = [
    '#FF5733',
    '#2ECC71',
    '#E74C3C',
    '#9B59B6',
    '#F39C12',
    '#1ABC9C',
    '#E67E22',
    '#27AE60',
    '#D35400',
    '#000000',
    '#43464B',
]

SECTION_CATEGORY = {
    'аксесуари': SECTION_ACCESSORIES_LST,
    'взуття': SECTION_CHOSE_LST,
    'одяг': SECTION_CLOTHES_LST,
}

SIZE_COUNTER = 21


IDENTIFICATOR_MALE = 'True'
IMAGE_FOLDER = 'data/kids'
CSV_PATH = 'data/goods.csv'


class Command(BaseCommand):
    """Class for input test data in to database"""

    help = 'Loads data from a CSV file into the database'

    def _write(self, message: str) -> None:
        self.stdout.write(message)

    def add_arguments(self, parser: ArgumentParser) -> None:
        """Set a path to file"""
        parser.add_argument(
            'path',
            type=str,
            default=CSV_PATH,
            help='Path to the CSV file',
        )

    def handle(self, *args: t.Any, **options: t.Any) -> None:
        path = options['path']
        reader, is_exists = self.validate_load_data(path)
        if is_exists:
            self._write('Data has already been uploaded')
        else:
            self.upload_data(path, reader)
            self._write('Data has been uploaded successfully')

    def upload_data(self, path: str, reader: list[dict[str, t.Any]]) -> None:
        self._write('Starting to upload --- SECTION_CATEGORY ---')
        categories, sections = self.create_categories()
        self._write('Category items count: %s' % len(categories))
        self._write('Section items count: %s' % len(sections))

        self._write('Starting to upload --- BRAND ---')
        brands = self.create_brands()
        self._write('BRAND items count %s' % len(brands))

        self._write('Starting to upload --- DISCOUNT ---')
        discounts = self.create_dicsounts()
        self._write('DISCOUNT items count %s' % len(discounts))

        self._write('Starting to upload --- SIZE ---')
        size = self.create_size_attr()

        self._write('Starting to upload --- COLOR ---')
        color = self.create_color_attr()

        self._write('Starting to upload --- PRODUCTS --- from %s' % path)
        products = self.create_products(
            sections=sections,
            brands=brands,
            discounts=discounts,
            reader=reader,
        )
        self._write('Product created items: %s' % len(products))

        self._write('Starting to upload --- STOCK ---')
        stocks, colors, sizes = self.create_stock(
            size=size,
            color=color,
            products=products,
        )
        self._write('STOCK items count %s' % len(stocks))
        self._write('Size items count: %s' % len(sizes))
        self._write('COLOR items count %s' % len(colors))

        self._write('INSERT --- IMAGES ---')
        pictures = self.insert_images(products)
        self._write('PICTURES items count %s' % len(pictures))

    def validate_load_data(
        self, path: str, delimiter: str = ','
    ) -> tuple[list[dict[str, t.Any]], bool]:

        with open(path, encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=delimiter)

            lines = list(reader)
            keys = lines.pop(0)
            list_of_product_dicts = []

            for line in lines:
                new_dict = self.make_dict_from_lists(keys, line)
                list_of_product_dicts.append(new_dict)
            self._write(str(list_of_product_dicts))

        with open(path, encoding='utf-8') as file:
            reader = [row for row in csv.DictReader(file)]
        products = Product.objects.all().count()
        self._write(str(reader))
        return reader, len(reader) == products

    def create_unique_article(self) -> str:
        # Generate a unique identifier using UUID
        unique_id = str(uuid.uuid4().hex)[:8]  # Extract the first 8 characters

        # Combine with a product prefix or any other information as needed
        product_prefix = "PRD"
        article = f"{product_prefix}_{unique_id}"

        return article

    def make_dict_from_lists(self, list1, list2) -> dict[str, str]:
        return {key.strip(): value.strip() for key, value in zip(list1, list2)}

    def insert_images(self, products: list[Product]) -> list[Picture]:
        images = defaultdict(list)
        for name in os.listdir(IMAGE_FOLDER):
            key = name.split('_', 1)[0]
            images[key].append(os.path.join(IMAGE_FOLDER, name))

        picture_objects = []
        for product in products:
            image_products = images.get(str(product.pk), [])
            for image_path in image_products:
                with open(image_path, 'rb') as image_file:
                    picture = Picture(product=product)
                    picture.product_image.save(
                        image_file.name, File(image_file)
                    )
                    picture_objects.append(picture)
            self._write(
                f'Insert images to {product} count {len(image_products)}'
            )
        # if picture_objects:
        #     Picture.objects.bulk_create(picture_objects, ignore_conflicts=True)
        return picture_objects

    def create_products(
        self,
        sections: list[Section],
        brands: list[Brand],
        discounts: list[Discount],
        reader: list[dict[str, t.Any]],
    ) -> list[Product]:
        products = []
        for item in reader:
            male = True if item['male'] == IDENTIFICATOR_MALE else False
            is_sale = random.choice((True, False))
            section = random.choice(sections)

            product = Product(
                name=item['name'],
                category=section.category,
                section=section,
                brand=random.choice(brands),
                description=item['description'],
                price=item['price'],
                male=male,
                # age=random.randint(0, 55),
                rating=random.randint(0, 10),
                # is_sale=is_sale,
                discount=random.choice(discounts) if is_sale else None,
            )
            products.append(product)
        Product.objects.bulk_create(products, ignore_conflicts=False)
        return products

    def create_stock(self, size, color, products) -> list[InStock]:
        instoks = []
        colors = []
        sizes = []
        for product in products:
            for _ in range(random.randint(3, 5)):

                instok = InStock(
                    product=product,
                    article=self.create_unique_article(),
                    # color=random.choice(colors),
                    # product_size=random.choice(sizes),
                    in_stock=random.randint(0, 50),
                )
                instoks.append(instok)

                size_product = AttributeProduct(
                    product=product,
                    attribute=size,
                    _attribute_name='Size',
                    value=random.randint(15, 38),
                )
                sizes.append(size_product)

                color_product = AttributeProduct(
                    product=product,
                    attribute=color,
                    _attribute_name='Color',
                    value=random.choice(COLOR_LST),
                )

                colors.append(color_product)

        InStock.objects.bulk_create(instoks)
        AttributeProduct.objects.bulk_create(colors)
        AttributeProduct.objects.bulk_create(sizes)

        return instoks, colors, sizes

    def create_color_attr(self) -> list[Color]:
        attribute_color = Attribute.objects.create(
            name='Color', widget='Default'
        )
        # colors = [Color(name=color) for color in COLOR_LST]
        # Color.objects.bulk_create(colors, ignore_conflicts=False)
        # assert len(colors) == len(COLOR_LST)
        return attribute_color

    def create_size_attr(self) -> list[Size]:
        attribute_size = Attribute.objects.create(
            name='Size', widget='Default'
        )
        # sizes = [AttributeProduct
        #     (
        #         attribute=attribute,
        #         _attribute_name='Size',
        #         value=random.randint(15, 38),
        #
        #     )
        #     for _ in range(SIZE_COUNTER)
        # ]
        #
        # AttributeProduct.objects.bulk_create(sizes, ignore_conflicts=False)
        # assert len(sizes) == SIZE_COUNTER
        return attribute_size

    def create_dicsounts(self) -> list[Discount]:
        discounts = [
            Discount(
                amount=discount,
                info='Discounted products',
                date_start=NOW,
                date_end=NOW + timedelta(weeks=1),
            )
            for discount in DISCOUNT_LST
        ]
        Discount.objects.bulk_create(discounts, ignore_conflicts=False)
        assert len(discounts) == len(DISCOUNT_LST)
        return discounts

    def create_brands(self) -> list[Brand]:
        brands = [
            Brand(name=brand, country=random.choice(COUNTRIES_LST))
            for brand in BRANDS_LST
        ]
        Brand.objects.bulk_create(brands, ignore_conflicts=False)
        assert len(brands) == len(BRANDS_LST)
        return brands

    def create_categories(self) -> tuple[list[Category], list[Section]]:
        all_sections = []
        categories = []
        for accessories_category, section_names in SECTION_CATEGORY.items():
            category = Category(name=accessories_category)
            categories.append(category)
            sections = [
                Section(name=section_name, category=category)
                for section_name in section_names
            ]

            all_sections.extend(sections)
            self._write(f'Category {category} sections count: {len(sections)}')
        Category.objects.bulk_create(categories, ignore_conflicts=False)
        Section.objects.bulk_create(all_sections, ignore_conflicts=False)
        return categories, all_sections


# with open(path, encoding='utf-8') as file:
#     reader = csv.reader(file, delimiter=';')
#
#     lines = list(reader)
#     keys = lines.pop(0)
#     list_of_product_dicts = []
#
#     for line in lines:
#         new_dict = make_dict_from_lists(keys, line)
#         list_of_product_dicts.append(new_dict)

# class Command(BaseCommand):
#     """Class for input test data in to database"""
#
#     help = 'Loads data from a CSV file into the database'
#
#     def add_arguments(self, parser):
#         """Set a path to file"""
#         parser.add_argument(
#             'path',
#             type=str,
#             default='data/goods.csv',
#             help='Path to the CSV file',
#         )
#
#     def handle(self, *args, **options):
#         category_lst = ['Одяг', 'Взуття', 'Аксесуары']
#
#         section_accessories_lst = [
#             'Біжутерія та Шпильки',
#             'Окуляри',
#             'Рюкзаки',
#             'Ремені',
#             'Рукавиці',
#             'Сумочки',
#             'Шарфи Та Платки',
#             'Шапки',
#             'Барсетки та Бананки',
#         ]
#
#         section_chose_lst = [
#             'Балетки',
#             'Гумові сапоги',
#             'Еспадрильї, Сліпони, Мокасини',
#             'Капці',
#             'Кеди',
#             'Кросівки',
#             'Черевики та Лофери',
#             'Чоботи та Пив Чоботи',
#             'Шлепанці та Босоніжки',
#             'Пінетки',
#             'Бутси',
#         ]
#
#         section_clothes_lst = [
#             'Блузки',
#             'Боді',
#             'Верхній одяг',
#             'Джинсі',
#             'Кофті, кардигани',
#             'Комбінезони',
#             'Комплекти, костюми',
#             'Спортивний одяг',
#             'Свeтри',
#             'Плаття',
#             'Піджаки та костюми',
#             'Піжами',
#             'Футболки',
#             'Трикотаж',
#             'Шорті',
#             'Штані',
#             'Спідниці',
#             'Шкільна форма',
#             'Тематичні костюми',
#             'Конверті',
#             'Крижми',
#             'Одяг для хрещення',
#             'Повзунки',
#             'Писачники',
#             'Подряпки',
#             'Чоловічки',
#             'Шапочки',
#             'Сорочки',
#         ]
#
#         brands_lst = [
#             "Nike",
#             "Adidas",
#             "Zara",
#             "H&M",
#             "Gucci",
#             "Louis Vuitton",
#             "Chanel",
#             "Calvin Klein",
#             "Ralph Lauren",
#             "Forever 21",
#         ]
#
#
#         color_lst = [
#             '#FF5733',
#             '#2ECC71',
#             '#E74C3C',
#             '#9B59B6',
#             '#F39C12',
#             '#1ABC9C',
#             '#E67E22',
#             '#27AE60',
#             '#D35400',
#             '#000000',
#             '#43464B',
#         ]
#
#         """
#         First part of script that uploads categories into the database.
#         At the end, the logger will show how many objects are created
#         """
#         logger.info('Starting to upload --- CATEGORY --- to the database')
#         category_counter = 0
#         for category in category_lst:
#             category_counter += 1
#             Category.objects.get_or_create(name=category)
#         logger.info(f'Objects created: {category_counter}')
#
#         """
#         At the end, the logger will show how many objects are created
#         """
#         logger.info('Starting to upload --- BRAND --- to the database')
#         brand_counter = 0
#         for brand in brands_lst:
#             brand_counter += 1
#             Brand.objects.get_or_create(name=brand)
#         logger.info(f'Objects created: {brand_counter}')
#
#         """
#         At the end, the logger will show how many objects are created
#         """
#         # logger.info('Starting to upload --- DISCOUNT --- to the database')
#         # discount_counter = 0
#         # for discount in discount_lst:
#         #     discount_counter += 1
#         #     Discount.objects.get_or_create(name=discount)
#         # logger.info(f'Objects created: {discount_counter}')
#
#         logger.info('Starting to upload --- SIZE --- in to --- DATABASE ---')
#         size_counter = 0
#         for _ in range(0, 21):
#             size_counter += 1
#             brand = Brand.objects.all()
#             size_instance, _ = Size.objects.get_or_create(
#                 brand_size=random.randint(15, 38),
#                 letter_size=random.choice(
#                     [choice.value for choice in Size.LetterSizeChoices]
#                 ),
#             )
#         logger.info(f'Objects created: {size_counter}')
#
#         logger.info('Starting to upload --- COLOR --- to the database')
#         color_counter = 0
#         for color in color_lst:
#             color_counter += 1
#             Color.objects.create(name=color)
#
#         """
#         Here, we begin the process of uploading sections all at once
#         While associating each section with its corresponding category
#         """
#         logger.info(
#             'Starting to upload --- SECTION --- to the --- ACCESSORIES CATEGORY ---'
#         )
#         section_counter = 0
#         accessories_category = Category.objects.get(name='аксесуары')
#         for section_name in section_accessories_lst:
#             _, created = Section.objects.get_or_create(
#                 name=section_name, category=accessories_category
#             )
#             section_counter += 1
#         logger.info(f'Objects created: {section_counter}')
#
#         """
#         Same process
#         """
#         logger.info(
#             'Starting to upload --- SECTION --- to the --- CHOSE CATEGORY ---'
#         )
#         section_counter = 0
#         chose_category = Category.objects.get(name='взуття')
#         for section_name in section_chose_lst:
#             section, _ = Section.objects.get_or_create(
#                 name=section_name, category=chose_category
#             )
#             section_counter += 1
#         logger.info(f'Objects created: {section_counter}')
#
#         """
#         Same process
#         """
#         logger.info(
#             'Starting to upload --- SECTION --- to the --- CLOTHES CATEGORY ---'
#         )
#         section_counter = 0
#         clothes_category = Category.objects.get(name='одяг')
#         for section_name in section_clothes_lst:
#             _, created = Section.objects.get_or_create(
#                 name=section_name, category=clothes_category
#             )
#             section_counter += 1
#         logger.info(f'Objects created: {section_counter}')
#
#         logger.info('Starting to upload --- SIZE --- in to --- DATABASE ---')
#         for _ in range(0, 21):
#             brand = Brand.objects.all()
#             size_instance, _ = Size.objects.get_or_create(
#                 brand_size=random.randint(15, 38),
#                 letter_size=random.choice(
#                     [choice.value for choice in Size.LetterSizeChoices]
#                 ),
#             )
#         logger.info(f'Objects created: {section_counter}')
#
#         path = options['path']  # Get path to file with data
#         logger.info(
#             f'Starting to upload --- PRODUCTS --- from {path} to the --- DATABASE ---'
#         )
#
#         """
#         This function opens a file containing data and inserts it into the database
#         Additionally, it retrieves all previously generated objects
#         And populates the corresponding fields
#         The objects will be assigned randomly
#         """
#         # with (open(path, encoding='utf-8') as file):
#         #     reader = csv.DictReader(file)
#         #     counter = 0
#         #     categories = Category.objects.all()
#         #     sections = Section.objects.all()
#         #     discount = Discount.objects.all()
#         #     colors = Color.objects.all()
#         #     sizes = Size.objects.all()
#         #     for item in reader:
#         #         counter += 1
#         #         male_value = item['male'].strip().lower()
#         #         male = True if male_value == 'true' else False
#         #         product, _ = Product.objects.get_or_create(
#         #             name=item['name'],
#         #             category=random.choice(categories),  # random category
#         #             section=random.choice(sections),  # random section
#         #             brand=random.choice(brand),  # random brand
#         #             description=item['description'],
#         #             price=item['price'],
#         #             male=male,
#         #             rating=random.randint(0, 10),  # random rating from 0 to 10
#         #         )
#         #
#         #         for _ in range(random.randint(3, 5)):
#         #             InStock.objects.create(
#         #                 product=product,
#         #                 color=random.choice(colors),
#         #                 product_size=random.choice(sizes),
#         #                 in_stock=random.randint(0, 50),
#         #             )
#         # logger.info(f'Objects created: {counter}')
#         #
#         # logger.info(
#         #     'Put --- DISCOUNT --- to all --- IS_SALE --- --- PRODUCTS ---'
#         # )
#         # sale_products = Product.objects.filter(is_sale=True)
#         # discount_sale_counter = 0
#         # for product in sale_products:
#         #     discount_sale_counter += 1
#         #     Product.objects.update_or_create(
#         #         id=product.id, defaults={'discount': random.choice(discount)}
#         #     )
#         # logger.info(f'Objects created: {discount_sale_counter}')
#         #
#         # image_folder = 'data/kids'
#         #
#         # logger.info('Start to insert --- IMAGES --- in to --- DATABASE ---')
#         # count_images = 0
#         # for product in Product.objects.all():
#         #     count_images += 1
#         #     image_filenames = [
#         #         f
#         #         for f in os.listdir(image_folder)
#         #         if f.startswith(f'{product.id}_')
#         #     ]
#         #
#         #     for image_filename in image_filenames:
#         #         image_path = os.path.join(image_folder, image_filename)
#         #
#         #         with open(image_path, 'rb') as image_file:
#         #             picture = Picture(product=product)
#         #             picture.product_image.save(
#         #                 image_filename, File(image_file)
#         #             )
#         #
#         #             picture.save()
#         # logger.info(f'Insert images {count_images}')
#
#         logger.info('Data has been uploaded successfully')
