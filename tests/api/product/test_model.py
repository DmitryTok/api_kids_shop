from django.test import TestCase
from django.utils import timezone

from api.models import Brand, Category, Discount, Product, Section


class ProductModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Shoes')
        section = Section.objects.create(name='Sport')
        brand = Brand.objects.create(name='Nike')
        discount = Discount.objects.create(
            amount=10,
            info='INFO',
            date_start=timezone.now(),
            date_end=timezone.now(),
        )

        self.product = Product.objects.create(
            name='Kids Shoes',
            category=category,
            section=section,
            description='Kids Shoes By Nike',
            brand=brand,
            price=1000.00,
            rating=4.5,
            male=1,
            discount=discount,
        )

    def test_str_representation(self):
        expected_str = 'Kids Shoes'
        self.assertEqual(expected_str, str(self.product))

    def test_product_discount(self):
        self.assertIsNotNone(self.product.discount)
        self.assertEqual(self.product.discount.amount, 10)
