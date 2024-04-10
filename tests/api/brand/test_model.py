from django.db.utils import DataError, IntegrityError

from api.models import Brand
from tests.base.base_test_case import BaseTestCase


class BrandModelTest(BaseTestCase):

    def test_unique_name(self):
        with self.assertRaises(IntegrityError):
            Brand.objects.create(name='Unique_Name')

    def test_name_length(self):
        with self.assertRaises(DataError):
            Brand.objects.create(name='name' * 201)

    def test_country_length(self):
        with self.assertRaises(DataError):
            Brand.objects.create(name='name', country='country' * 31)

    def test_str(self):
        expected_str = 'Unique_Name'
        self.assertEqual(expected_str, str(self.brand))
