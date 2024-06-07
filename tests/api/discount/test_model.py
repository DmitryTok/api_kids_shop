from django.db.utils import DataError
from django.utils import timezone

from api.models import Discount
from tests.base.base_test_case import BaseTestCase


class DiscountModelTest(BaseTestCase):

    def test_name_length(self):
        with self.assertRaises(DataError):
            Discount.objects.create(
                amount=5,
                info='INFO' * 121,
                date_start=timezone.now(),
                date_end=timezone.now(),
            )

    def test_str(self):
        expected_str = '10 INFO'
        self.assertEqual(
            expected_str,
            str(self.discount),
        )
