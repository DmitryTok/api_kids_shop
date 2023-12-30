import csv
import os
import random
import typing as t
from argparse import ArgumentParser
from collections import defaultdict

from django.core.files import File
from django.core.management.base import BaseCommand

from api.models import (
    Brand,
    Category,
    Color,
    Discount,
    InStock,
    Picture,
    Product,
    Section,
    Size,
)
import logging


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

DISCOUNT_LST = [5, 10, 15, 20, 25, 30, 35]

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
        sizes = self.create_sizes()
        self._write('Size items count: %s' % len(sizes))

        self._write('Starting to upload --- COLOR ---')
        colors = self.create_colors()
        self._write('COLOR items count %s' % len(colors))

        self._write('Starting to upload --- PRODUCTS --- from %s' % path)
        products = self.create_products(
            sections=sections,
            brands=brands,
            discounts=discounts,
            reader=reader,
        )
        self._write('Product created items: %s' % len(products))

        self._write('Starting to upload --- STOCK ---')
        stocks = self.create_stock(
            sizes=sizes,
            colors=colors,
            products=products,
        )
        self._write('STOCK items count %s' % len(stocks))

        self._write('INSERT --- IMAGES ---')
        pictures = self.insert_images(products)
        self._write('PICTURES items count %s' % len(pictures))

    def validate_load_data(
        self, path: str
    ) -> tuple[list[dict[str, t.Any]], bool]:
        with open(path, encoding='utf-8') as file:
            reader = [row for row in csv.DictReader(file)]
        products = Product.objects.all().count()
        return reader, len(reader) == products

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
                'Insert images to %s count %s' % (product, len(image_products))
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
                age=random.randint(0, 55),
                rating=random.randint(0, 10),
                is_sale=is_sale,
                discount=random.choice(discounts) if is_sale else None,
            )
            products.append(product)
        Product.objects.bulk_create(products, ignore_conflicts=False)
        return products

    def create_stock(self, sizes, colors, products) -> list[InStock]:
        instoks = []
        for product in products:
            for _ in range(random.randint(3, 5)):
                instok = InStock(
                    product=product,
                    color=random.choice(colors),
                    product_size=random.choice(sizes),
                    in_stock=random.randint(0, 50),
                )
                instoks.append(instok)

        InStock.objects.bulk_create(instoks)
        return instoks

        # self._write('--- DISCOUNT IS_SALE PRODUCTS ---')
        # sale_product_ids = Product.objects.filter(is_sale=True).values_list(
        #     'pk', flat=True
        # )
        # Product.objects.filter(pk__in=sale_product_ids).update(
        #     discount=random.choice(discounts)
        # )
        # self._write('Products For Sale updated: %s' % sale_product_ids)

    def create_colors(self) -> list[Color]:
        colors = [Color(name=color) for color in COLOR_LST]
        Color.objects.bulk_create(colors, ignore_conflicts=False)
        assert len(colors) == len(COLOR_LST)
        return colors

    def create_sizes(self) -> list[Size]:
        sizes = [
            Size(
                brand_size=random.randint(15, 38),
                letter_size=random.choice(
                    [choice.value for choice in Size.LetterSizeChoices]
                ),
            )
            for _ in range(SIZE_COUNTER)
        ]

        Size.objects.bulk_create(sizes, ignore_conflicts=False)
        assert len(sizes) == SIZE_COUNTER
        return sizes

    def create_dicsounts(self) -> list[Discount]:
        discounts = [Discount(name=discount) for discount in DISCOUNT_LST]
        Discount.objects.bulk_create(discounts, ignore_conflicts=False)
        assert len(discounts) == len(DISCOUNT_LST)
        return discounts

    def create_brands(self) -> list[Brand]:
        brands = [Brand(name=brand) for brand in BRANDS_LST]
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
            self._write(
                'Category %s sections count: %s' % (category, len(sections))
            )
        Category.objects.bulk_create(categories, ignore_conflicts=False)
        Section.objects.bulk_create(all_sections, ignore_conflicts=False)
        return categories, all_sections
