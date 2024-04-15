from api.serializers import AttributeSerializer
from tests.base.base_test_case import BaseTestCase


class AttributeSerializerTest(BaseTestCase):
    def setUp(self) -> None:
        self.serializer = AttributeSerializer(instance=self.attribute)

    def test_serializer(self):
        self.assertEqual(self.serializer.data['id'], self.attribute.id)
        self.assertEqual(self.serializer.data['name'], self.attribute.name)
        self.assertEqual(self.serializer.data['extra'], self.attribute.extra)
