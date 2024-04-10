from django.db.utils import DataError

from api.models import InStock
from tests.base.base_test_case import BaseTestCase


class InStockModelTest(BaseTestCase):

    def test_str_representation(self):
        expected_tr = 'Product Article'
        self.assertEqual(expected_tr, str(self.in_stock))

    def test_name_length(self):
        with self.assertRaises(DataError):
            InStock.objects.create(
                product=self.product,
                article='Article' * 51,
                in_stock=25,
            )
