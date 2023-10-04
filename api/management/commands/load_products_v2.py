import csv
import os

from django.core.files import File
from django.core.management.base import BaseCommand

from api.models import (Brand, Category, Color, Discount, InStock, Picture,
                        Product, Section, Size)
from kids_shop.logger import logger


class Command(BaseCommand):
    """ Class for input test data in to database """
    help = 'Loads data from a CSV file into the database'

    def add_arguments(self, parser):
        """ Set a path to file """
        parser.add_argument('path', type=str, default='data/goods.csv', help='Path to the CSV file')

    def handle(self, *args, **options):
        path = options['path']  # Get path to file with data
        logger.info(f'Starting to upload --- PRODUCTS --- from {path} to the --- DATABASE ---')

        """
        This function opens a file containing data and inserts it into the database
        """

        def make_dict_from_lists(list1, list2):
            return {key.strip(): value.strip().lower() for key, value in zip(list1, list2)}

        with open(path, encoding='utf-8') as file:

            reader = csv.reader(file, delimiter=';')

            lines = list(reader)
            keys = lines.pop(0)
            list_of_product_dicts = []

            for line in lines:
                new_dict = make_dict_from_lists(keys, line)
                list_of_product_dicts.append(new_dict)
            list_of_products = []
            counter = 0
            for product in list_of_product_dicts:
                category, _ = Category.objects.get_or_create(name=product['category'])
                discount, _ = Discount.objects.get_or_create(name=product['discount'])
                section, _ = Section.objects.get_or_create(name=product['section'], category=category)
                brand, _ = Brand.objects.get_or_create(name=product['brand'])
                male = 'true' == product['male']
                is_sale = 'true' == product['is_sale']
                list_of_products.append(
                    Product(
                        name=product['name'],
                        category=category,
                        section=section,
                        description=product['description'],
                        price=product['price'],
                        rating=product['rating'],
                        age=product['age'],
                        male=male,
                        is_sale=is_sale,
                        discount=discount,
                        brand=brand,
                    )
                )
                counter += 1

            Product.objects.bulk_create(list_of_products)

            logger.info(f'Objects created: {counter}')
            logger.info('Data has been uploaded successfully')



