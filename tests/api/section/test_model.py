from django.db.utils import DataError, IntegrityError
from rest_framework.test import APITestCase

from api.models import Section


class SectionModelTest(APITestCase):

    def setUp(self):
        self.section = Section.objects.create(name='Unique_Name')

    def test_unique_name(self):
        with self.assertRaises(IntegrityError):
            Section.objects.create(name='Unique_Name')

    def test_name_length(self):
        with self.assertRaises(DataError):
            Section.objects.create(name='name' * 201)

    def test_str(self):
        expected_str = 'Unique_Name'
        self.assertEqual(expected_str, str(self.section))
