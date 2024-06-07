from api.serializers import AttributeProductSerializer
from tests.base.base_test_case import BaseTestCase


class AttributeProductSerializerTest(BaseTestCase):
    def setUp(self) -> None:
        self.serializer = AttributeProductSerializer(
            instance=self.attribute_product
        )

    def test_serializer(self):
        self.assertEqual(self.serializer.data['id'], self.attribute_product.id)
        self.assertEqual(
            self.serializer.data['attribute_name'],
            self.attribute_product.attribute_name,
        )
        self.assertEqual(
            self.serializer.data['value'],
            self.attribute_product.value,
        )
        self.assertEqual(
            self.serializer.data['attribute'],
            self.attribute.id,
        )
        self.assertEqual(
            self.serializer.data['product'],
            self.product.id,
        )
