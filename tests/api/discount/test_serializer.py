from api.serializers import DiscountSerializer
from tests.base.base_test_case import BaseTestCase


class DiscountSerializerTest(BaseTestCase):
    def setUp(self) -> None:
        self.serializer = DiscountSerializer(instance=self.discount)

    def test_serializer(self):
        self.assertEqual(self.serializer.data['id'], self.discount.id)
        self.assertEqual(self.serializer.data['amount'], self.discount.amount)
        self.assertEqual(self.serializer.data['info'], self.discount.info)
