from rest_framework.test import APITestCase

from api.models import Section
from api.serializers import SectionSerializer


class SectionSerializerTest(APITestCase):
    def setUp(self):
        self.section = Section.objects.create(name='Test')
        self.serializer = SectionSerializer(instance=self.section)

    def test_serializer(self):
        self.assertEqual(self.serializer.data['id'], self.section.id)
        self.assertEqual(self.serializer.data['name'], self.section.name)
