from django.db.utils import DataError
from django.utils import timezone
from rest_framework.test import APITestCase

from api.models import Discount


class BrandModelTest(APITestCase):

    def setUp(self):
        self.discount = Discount.objects.create(
            amount=5,
            info='INFO',
            date_start=timezone.now(),
            date_end=timezone.now(),
        )

    def test_name_length(self):
        with self.assertRaises(DataError):
            Discount.objects.create(
                amount=5,
                info='INFO' * 121,
                date_start=timezone.now(),
                date_end=timezone.now(),
            )

    def test_str(self):
        expected_str = '5 INFO'
        self.assertEqual(
            expected_str,
            str(self.discount),
        )
