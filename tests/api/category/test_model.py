from django.db.utils import DataError, IntegrityError

from api.models import Category
from tests.base.base_test_case import BaseTestCase


class CategoryModelTest(BaseTestCase):

    def test_unique_name(self):
        with self.assertRaises(IntegrityError):
            Category.objects.create(name='Category')

    def test_name_length(self):
        with self.assertRaises(DataError):
            Category.objects.create(name='name' * 201)

    def test_str_representation(self):
        expected_str = 'Category'
        self.assertEqual(expected_str, str(self.category))
