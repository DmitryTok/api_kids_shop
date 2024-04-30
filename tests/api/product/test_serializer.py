from api.serializers import ProductSerializer
from tests.base.base_test_case import BaseTestCase


class ProductSerializerTest(BaseTestCase):
    def setUp(self) -> None:
        self.serializer = ProductSerializer(instance=self.product)

    def test_serializer(self):
        self.assertEqual(self.serializer.data['id'], self.product.id)
        self.assertEqual(
            self.serializer.data['category']['id'], self.category.id
        )
        self.assertEqual(
            self.serializer.data['section']['id'], self.section.id
        )
        self.assertEqual(self.serializer.data['brand']['id'], self.brand.id)
        self.assertEqual(
            self.serializer.data['discount']['id'], self.discount.id
        )
        self.assertEqual(
            self.serializer.data['in_stock'][0]['id'], self.in_stock.id
        )
        self.assertEqual(
            self.serializer.data['attributes'][0]['id'], self.attribute.id
        )
