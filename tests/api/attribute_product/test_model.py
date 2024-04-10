from django.db.utils import DataError

from api.models import AttributeProduct
from tests.base.base_test_case import BaseTestCase


class AttributeProductModelTest(BaseTestCase):

    def test_name_length(self):
        with self.assertRaises(DataError):
            AttributeProduct.objects.create(
                attribute=self.attribute,
                attribute_name='Attribute Name' * 121,
                product=self.product,
                value='Value' * 121,
            )

    def test_str_representation(self):
        expected_str = 'Attribute Name Value'
        self.assertEqual(expected_str, str(self.attribute_product))
