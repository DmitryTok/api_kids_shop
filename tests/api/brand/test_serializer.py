from rest_framework.test import APITestCase

from api.models import Brand
from api.serializers import BrandSerializer


class BrandSerializerTest(APITestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='name', country='country')
        self.serializer = BrandSerializer(instance=self.brand)

    def test_serializer(self):
        self.assertEqual(self.serializer.data['id'], self.brand.id)
        self.assertEqual(self.serializer.data['name'], self.brand.name)
        self.assertEqual(self.serializer.data['country'], self.brand.country)
