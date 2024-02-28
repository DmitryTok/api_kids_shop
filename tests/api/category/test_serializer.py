from rest_framework.test import APITestCase

from api.models import Category, Section
from api.serializers import CategorySerializer


class CategorySerializerTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test')
        self.section1 = Section.objects.create(
            name="Section 1", category=self.category
        )
        self.section2 = Section.objects.create(
            name="Section 2", category=self.category
        )
        self.serializer = CategorySerializer(instance=self.category)

    def test_serializer(self):
        self.assertEqual(self.serializer)

    def test_serializer_list(self):
        self.assertEqual(self.serializer.data['id'], self.category.id)
        self.assertEqual(self.serializer.data['name'], self.category.name)
