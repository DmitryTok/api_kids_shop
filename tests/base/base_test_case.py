from django.test import Client
from django.utils import timezone
from rest_framework.test import APITestCase

from api.models import (Attribute, AttributeProduct, Brand, Category, Discount,
                        InStock, Picture, Product, Section)
from users.models import Address, CustomUser, Kid, Profile


class BaseTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.auth_client = Client()

        # User Objects
        cls.user = CustomUser.objects.create(
            email='test_user@example.com',
            password='password123',
        )
        cls.superuser = CustomUser.objects.create_superuser(
            email='admin@example.com', password='admin123'
        )
        cls.auth_client.force_login(cls.superuser)

        # Kid Objects
        cls.kid = Kid.objects.create(
            male=Kid.MaleChoices.Male,
            birth_date='01/01/2000',
        )

        # Address Object
        cls.address = Address.objects.create(
            first_delivery_address='first_delivery_address',
            second_delivery_address='second_delivery_address',
            city='city',
            street='street',
            building='building',
            apartment=1,
        )

        # Profile Objects
        cls.profile = Profile.objects.create(
            user=cls.user,
            address=cls.address,
            gender=Profile.GenderChoices.Man,
            first_name='John',
            middle_name='Gary',
            last_name='Doe',
            birth_date='01/01/2000',
            first_phone=1234567890,
            second_phone=1234567890,
        )
        cls.profile.kids.add(cls.kid)

        # Attribute Objects
        cls.attribute = Attribute.objects.create(
            name='Color',
            is_global=True,
            widget='ColorPicker',
            extra={'options': ['Red', 'Blue', 'Green']},
        )

        # Brand objects
        cls.brand = Brand.objects.create(name='Unique_Name', country='country')
        cls.brand_test_1 = Brand.objects.create(name='Test_1')
        cls.brand_test_2 = Brand.objects.create(name='Test_2')
        cls.brand_test_3 = Brand.objects.create(name='Test_3')

        # Category Objects
        cls.category = Category.objects.create(name='Category')
        cls.category_test_1 = Category.objects.create(name='Category_Test_1')
        cls.category_test_2 = Category.objects.create(name='Category_Test_2')
        cls.category_test_3 = Category.objects.create(name='Category_Test_3')

        # Section Objects
        cls.section = Section.objects.create(name='Section')
        cls.section_test_1 = Section.objects.create(
            name='Section_Test_1', category=cls.category_test_1
        )
        cls.section_test_2 = Section.objects.create(
            name='Section_Test_2', category=cls.category_test_1
        )
        cls.section_test_3 = Section.objects.create(
            name='Section_Test_3', category=cls.category_test_1
        )

        # Discount Objects
        cls.discount = Discount.objects.create(
            amount=10,
            info='INFO',
            date_start=timezone.now(),
            date_end=timezone.now(),
        )

        # Product Object
        cls.product = Product.objects.create(
            name='Product',
            category=cls.category,
            section=cls.section,
            description='Product description',
            brand=cls.brand,
            price=1000.00,
            rating=4.5,
            male=1,
            discount=cls.discount,
        )

        # AttributeProduct Objects
        cls.attribute_product = AttributeProduct.objects.create(
            attribute=cls.attribute,
            attribute_name='Attribute Name',
            product=cls.product,
            value='Value',
        )

        # InStock Objects
        cls.in_stock = InStock.objects.create(
            product=cls.product, article='Article', in_stock=20
        )

        # Picture Objects
        cls.picture = Picture.objects.create(
            product=cls.product, product_image='image.png'
        )

    def test_create_objects(cls):

        # Users
        cls.assertIsNotNone(cls.user)

        # Kids
        cls.assertIsNotNone(cls.kid)

        # Addresses
        cls.assertIsNotNone(cls.address)

        # Profiles

        # Attributes
        cls.assertIsNotNone(cls.attribute)

        # Brands
        cls.assertIsNotNone(cls.brand)
        cls.assertIsNotNone(cls.brand_test_1)
        cls.assertIsNotNone(cls.brand_test_2)
        cls.assertIsNotNone(cls.brand_test_3)

        # Categories
        cls.assertIsNotNone(cls.category)
        cls.assertIsNotNone(cls.category_test_1)
        cls.assertIsNotNone(cls.category_test_2)
        cls.assertIsNotNone(cls.category_test_3)

        # Sections
        cls.assertIsNotNone(cls.section)
        cls.assertIsNotNone(cls.section_test_1)
        cls.assertIsNotNone(cls.section_test_2)
        cls.assertIsNotNone(cls.section_test_3)

        # Discounts
        cls.assertIsNotNone(cls.discount)

        # Products
        cls.assertIsNotNone(cls.product)

        # AttributeProducts
        cls.assertIsNotNone(cls.attribute_product)

        # InStocks
        cls.assertIsNotNone(cls.in_stock)

    def setUp(cls):
        super().setUp()

    def tearDown(cls):
        super().tearDown()
