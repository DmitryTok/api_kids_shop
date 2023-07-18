from django.core.management.base import BaseCommand

from api.models import Category, Section
from kids_shop.logger import logger


class Command(BaseCommand):
    help = 'Loads category and section in to database'

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

        logger.info('Starting to upload --- CATEGORY --- to the database')
        category_counter = 0
        for category in category_lst:
            category_counter += 1
            Category.objects.get_or_create(name=category)
        logger.info(f'Objects created: {category_counter}')

        logger.info('Starting to upload --- SECTION --- to the --- ACCESSORIES CATEGORY ---')
        section_counter = 0
        accessories_category = Category.objects.get(name='Аксесуары')
        for section_name in section_accessories_lst:
            section, created = Section.objects.get_or_create(name=section_name, category=accessories_category)
            section_counter += 1
        logger.info(f'Objects created: {section_counter}')

        logger.info('Starting to upload --- SECTION --- to the --- CHOSE CATEGORY ---')
        section_counter = 0
        chose_category = Category.objects.get(name='Взуття')
        for section_name in section_chose_lst:
            section, created = Section.objects.get_or_create(name=section_name, category=chose_category)
            section_counter += 1
        logger.info(f'Objects created: {section_counter}')

        logger.info('Starting to upload --- SECTION --- to the --- CLOTHES CATEGORY ---')
        section_counter = 0
        clothes_category = Category.objects.get(name='Одяг')
        for section_name in section_clothes_lst:
            section, created = Section.objects.get_or_create(name=section_name, category=clothes_category)
            section_counter += 1
        logger.info(f'Objects created: {section_counter}')

        logger.info('Data has been uploaded successfully')
