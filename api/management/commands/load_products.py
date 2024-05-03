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

from api.models import (Attribute, AttributeProduct, Brand, Category, Discount,
                        InStock, Picture, Product, Section)

log = logging.getLogger(__name__)


SECTION_ACCESSORIES_LST = ['Колготки', 'Рукавички', 'Шапки']

SECTION_CLOTHES_LST = [
    'Бомбери',
    'Джинси',
    'Жилетки',
    'Кльош костюми',
    'Комбінезони',
    'Комплекти',
    'Куртки',
    'Лонгсліви',
    'Лосини',
    'Напівкомбінезони',
    'Светри',
    'Світшоти',
    'Сорочки',
    'Спортивні костюми',
    'Сукні',
    'Футболки',
    'Худі',
    'Шорти',
    'Шорти-спідниця',
    'Штани',
    'Літні комплекти',
    'Боді',
    'Кофтинки',
    'Панамки',
    'Повʼязки',
    'Пісочники',
    'Чоловічки',
    'Шапочки',
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
    'Аксесуари': SECTION_ACCESSORIES_LST,
    'Одяг': SECTION_CLOTHES_LST,
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
        discounts = self.create_discounts()
        self._write('DISCOUNT items count %s' % len(discounts))

        self._write('Starting to upload --- SIZE ---')
        size = self.create_size_attr()

        self._write('Starting to upload --- COLOR ---')
        color = self.create_color_attr()

        self._write('Starting to upload --- AGE ---')
        age = self.create_age_attr()

        self._write('Starting to upload --- PRODUCTS --- from %s' % path)

        products = self.create_products(
            sections=sections,
            brands=brands,
            discounts=discounts,
            reader=reader,
        )
        self._write('Product created items: %s' % len(products))

        self._write('Starting to upload --- STOCK ---')
        stocks, colors, sizes, ages = self.create_stock(
            size=size,
            color=color,
            age=age,
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

    def create_unique_article(self):
        # Generate a unique identifier using UUID
        unique_id = str(uuid.uuid4().hex)[:8]  # Extract the first 8 characters

        # Combine with a product prefix or any other information as needed
        product_prefix = "PRD"
        article = f"{product_prefix}_{unique_id}"

        return article

    def make_dict_from_lists(self, list1, list2):
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
            male = random.randint(0, 4)
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
                rating=random.randint(0, 10),
                discount=random.choice(discounts) if is_sale else None,
            )
            products.append(product)
        Product.objects.bulk_create(products, ignore_conflicts=False)
        return products

    def create_stock(self, size, color, age, products) -> list[InStock]:
        instoks = []
        colors = []
        sizes = []
        ages = []
        for product in products:
            age_product = AttributeProduct(
                product=product,
                attribute=age,
                attribute_name='Age',
                value=f'{random.randint(1, 5)} {random.randint(6, 12)}',
            )
            ages.append(age_product)
            for _ in range(random.randint(3, 5)):

                instok = InStock(
                    product=product,
                    article=self.create_unique_article(),
                    in_stock=random.randint(0, 50),
                )
                instoks.append(instok)

                size_product = AttributeProduct(
                    product=product,
                    attribute=size,
                    attribute_name='Size',
                    value=random.randint(15, 38),
                )
                sizes.append(size_product)

                color_product = AttributeProduct(
                    product=product,
                    attribute=color,
                    attribute_name='Color',
                    value=random.choice(COLOR_LST),
                )

                colors.append(color_product)

        InStock.objects.bulk_create(instoks)
        AttributeProduct.objects.bulk_create(colors)
        AttributeProduct.objects.bulk_create(sizes)
        AttributeProduct.objects.bulk_create(ages)

        return instoks, colors, sizes, ages

    def create_color_attr(self) -> Attribute:
        attribute_color = Attribute.objects.create(
            name='Color', widget='Default'
        )
        return attribute_color

    def create_size_attr(self) -> Attribute:
        attribute_size = Attribute.objects.create(
            name='Size', widget='Default'
        )
        return attribute_size

    def create_age_attr(self) -> Attribute:
        attribute_age = Attribute.objects.create(name='Age', widget='default')
        return attribute_age

    def create_discounts(self) -> list[Discount]:
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
