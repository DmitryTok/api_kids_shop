from api.serializers import SectionSerializer
from tests.base.base_test_case import BaseTestCase


class SectionSerializerTest(BaseTestCase):
    def setUp(self):
        self.serializer = SectionSerializer(instance=self.section)

    def test_serializer(self):
        self.assertEqual(self.serializer.data['id'], self.section.id)
        self.assertEqual(self.serializer.data['name'], self.section.name)
