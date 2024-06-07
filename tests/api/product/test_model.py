from tests.base.base_test_case import BaseTestCase


class ProductModelTest(BaseTestCase):

    def test_str_representation(self):
        expected_str = 'Product'
        self.assertEqual(expected_str, str(self.product))

    def test_product_discount(self):
        self.assertIsNotNone(self.product.discount)
        self.assertEqual(self.product.discount.amount, 10)
