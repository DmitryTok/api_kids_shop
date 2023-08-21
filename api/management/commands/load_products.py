import csv
import os
import random

from django.core.files import File
from django.core.management.base import BaseCommand

from api.models import Brand, Category, Color, Discount, Picture, Product, Section
from kids_shop.logger import logger


class Command(BaseCommand):
    """ Class for input test data in to database """
    help = 'Loads data from a CSV file into the database'

    def add_arguments(self, parser):
        """ Set a path to file """
        parser.add_argument('path', type=str, default='data/goods.csv', help='Path to the CSV file')

    def handle(self, *args, **options):
        category_lst = ['Одяг', 'Взуття', 'Аксесуары']

        section_accessories_lst = [
            'Біжутерія та Шпильки',
            'Окуляри',
            'Рюкзаки',
            'Ремені',
            'Рукавиці',
            'Сумочки',
            'Шарфи Та Платки',
            'Шапки',
            'Барсетки та Бананки'
        ]

        section_chose_lst = [
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

        section_clothes_lst = [
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

        brands_lst = [
            "Nike",
            "Adidas",
            "Zara",
            "H&M",
            "Gucci",
            "Louis Vuitton",
            "Chanel",
            "Calvin Klein",
            "Ralph Lauren",
            "Forever 21"
        ]

        discount_lst = [5, 10, 15, 20, 25, 30, 35]

        color_lst = [
            '#FF5733',
            '#3498DBб',
            '#2ECC71',
            '#E74C3C',
            '#9B59B6',
            '#F39C12',
            '#1ABC9C',
            '#E67E22',
            '#27AE60',
            '#D35400',
            '#000000',
            '#43464B'
        ]

        """
        First part of script that uploads categories from category_lst into the database.
        At the end, the logger will show how many objects are created
        """
        logger.info('Starting to upload --- CATEGORY --- to the database')
        category_counter = 0
        for category in category_lst:
            category_counter += 1
            Category.objects.get_or_create(name=category)
        logger.info(f'Objects created: {category_counter}')

        """
        Second part of script that uploads brands from brands_lst into the database.
        At the end, the logger will show how many objects are created
        """
        logger.info('Starting to upload --- BRAND --- to the database')
        brand_counter = 0
        for brand in brands_lst:
            brand_counter += 1
            Brand.objects.get_or_create(name=brand)
        logger.info(f'Objects created: {brand_counter}')

        """
        Third part of script that uploads discount from discount_lst into the database.
        At the end, the logger will show how many objects are created
        """
        logger.info('Starting to upload --- DISCOUNT --- to the database')
        discount_counter = 0
        for discount in discount_lst:
            discount_counter += 1
            Discount.objects.get_or_create(name=discount)
        logger.info(f'Objects created: {discount_counter}')

        logger.info('Starting to upload --- COLOR --- to the database')
        color_counter = 0
        for color in color_lst:
            color_counter += 1
            Color.objects.get_or_create(name=color)
        logger.info(f'Objects created: {color_counter}')

        """
        Here, we begin the process of uploading sections all at once
        While associating each section with its corresponding category
        """
        logger.info('Starting to upload --- SECTION --- to the --- ACCESSORIES CATEGORY ---')
        section_counter = 0
        accessories_category = Category.objects.get(name='Аксесуары')
        for section_name in section_accessories_lst:
            _, created = Section.objects.get_or_create(name=section_name, category=accessories_category)
            section_counter += 1
        logger.info(f'Objects created: {section_counter}')

        """
        Same process
        """
        logger.info('Starting to upload --- SECTION --- to the --- CHOSE CATEGORY ---')
        section_counter = 0
        chose_category = Category.objects.get(name='Взуття')
        for section_name in section_chose_lst:
            section, _ = Section.objects.get_or_create(name=section_name, category=chose_category)
            section_counter += 1
        logger.info(f'Objects created: {section_counter}')

        """
        Same process
        """
        logger.info('Starting to upload --- SECTION --- to the --- CLOTHES CATEGORY ---')
        section_counter = 0
        clothes_category = Category.objects.get(name='Одяг')
        for section_name in section_clothes_lst:
            _, created = Section.objects.get_or_create(name=section_name, category=clothes_category)
            section_counter += 1
        logger.info(f'Objects created: {section_counter}')

        path = options['path']  # Get path to file with data
        logger.info(f'Starting to upload --- PRODUCTS --- from {path} to the --- DATABASE ---')

        """
        This function opens a file containing data and inserts it into the database
        Additionally, it retrieves all previously generated objects and populates the corresponding fields
        The objects will be assigned randomly
        """
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            counter = 0
            is_sale = (True, False)
            categories = Category.objects.all()
            sections = Section.objects.all()
            brand = Brand.objects.all()
            discount = Discount.objects.all()
            color = Color.objects.all()
            for item in reader:
                counter += 1
                male_value = item['male'].strip().lower()
                male = True if male_value == 'true' else False
                product, _ = Product.objects.get_or_create(
                    name=item['name'],
                    category=random.choice(categories),  # random category
                    section=random.choice(sections),  # random section
                    brand=random.choice(brand),  # random brand
                    description=item['description'],
                    price=item['price'],
                    size=random.randint(1, 30),  # random size from 1 to 30
                    male=male,
                    age=random.randint(0, 15),  # random age from 0 to 15
                    rating=random.randint(0, 10),  # random rating from 0 to 10
                    is_sale=random.choice(is_sale),  # random on sale flag
                )
                product.color.add(*random.sample(list(color), random.randint(1, len(color))))
        logger.info(f'Objects created: {counter}')

        logger.info('Put --- DISCOUNT --- to all IS_SALE --- PRODUCTS ---')
        sale_products = Product.objects.filter(is_sale=True)
        discount_sale_counter = 0
        for product in sale_products:
            discount_sale_counter += 1
            Product.objects.update_or_create(
                id=product.id,
                defaults={'discount': random.choice(discount)}
            )
        logger.info(f'Objects created: {discount_sale_counter}')

        image_folder = 'data/kids'

        logger.info('Start to insert --- IMAGES --- in to --- DATABASE ---')
        for product in Product.objects.all():

            image_filenames = [
                f for f in os.listdir(image_folder) if f.startswith(f'{product.id}_')
            ]

            for image_filename in image_filenames:
                image_path = os.path.join(image_folder, image_filename)

                with open(image_path, 'rb') as image_file:
                    picture = Picture(product=product)
                    picture.product_image.save(image_filename, File(image_file))

                    picture.save()

    logger.info('Data has been uploaded successfully')
