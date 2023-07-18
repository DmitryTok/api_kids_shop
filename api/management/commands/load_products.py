import csv

from django.core.management.base import BaseCommand

from api.models import Product
from kids_shop.logger import logger


class Command(BaseCommand):
    help = 'Loads data from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, default='data/goods.csv', help='Path to the CSV file')

    def handle(self, *args, **options):
        path = options['path']
        logger.info(f'Starting to upload data from {path} to the database')

        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            counter = 0
            for item in reader:
                counter += 1
                male_value = item['male'].strip().lower()
                male = True if male_value == 'true' else False
                Product.objects.get_or_create(
                    name=item['name'],
                    description=item['description'],
                    price=item['price'],
                    male=male
                )
        logger.info(f'Objects created: {counter}')
        logger.info('Data has been uploaded successfully')
