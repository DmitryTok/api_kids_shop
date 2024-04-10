from django.db.utils import DataError
from django.utils import timezone

from api.models import Discount
from tests.base.base_test_case import BaseTestCase


class AttributeModelTest(BaseTestCase):

    def test_str_representation(self):
        expected_str = 'Color'
        self.assertEqual(expected_str, str(self.attribute))

    def test_name_length(self):
        with self.assertRaises(DataError):
            Discount.objects.create(
                amount=5,
                info='INFO' * 121,
                date_start=timezone.now(),
                date_end=timezone.now(),
            )
