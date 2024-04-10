from api.serializers import BrandSerializer
from tests.base.base_test_case import BaseTestCase


class BrandSerializerTest(BaseTestCase):
    def setUp(self):
        self.serializer = BrandSerializer(instance=self.brand)

    def test_serializer(self):
        self.assertEqual(self.serializer.data['id'], self.brand.id)
        self.assertEqual(self.serializer.data['name'], self.brand.name)
        self.assertEqual(self.serializer.data['country'], self.brand.country)
