from rest_framework.test import APITestCase

from api.models import Attribute, Brand


class BaseTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Attribute Objects
        cls.attribute = Attribute.objects.create(
            name='Color',
            is_global=True,
            widget='ColorPicker',
            extra={'options': ['Red', 'Blue', 'Green']},
        )
        # Brand objects
        cls.brand = Brand.objects.create(name='Unique_Name')
        cls.brand_test_1 = Brand.objects.create(name='Test_1')
        cls.brand_test_2 = Brand.objects.create(name='Test_2')
        cls.brand_test_3 = Brand.objects.create(name='Test_3')

    def test_create_objects(cls):
        cls.assertIsNotNone(cls.attribute)
        cls.assertIsNotNone(cls.brand)

    def setUp(cls):
        super().setUp()

    def tearDown(cls):
        super().tearDown()
