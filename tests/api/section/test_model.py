from django.db.utils import DataError, IntegrityError

from api.models import Section
from tests.base.base_test_case import BaseTestCase


class SectionModelTest(BaseTestCase):

    def test_unique_name(self):
        with self.assertRaises(IntegrityError):
            Section.objects.create(name='Section')

    def test_name_length(self):
        with self.assertRaises(DataError):
            Section.objects.create(name='name' * 201)

    def test_str(self):
        expected_str = 'Section'
        self.assertEqual(expected_str, str(self.section))
