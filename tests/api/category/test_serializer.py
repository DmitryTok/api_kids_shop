from api.serializers import CategorySerializer
from tests.base.base_test_case import BaseTestCase


class CategorySerializerTest(BaseTestCase):
    def setUp(self):
        self.serializer = CategorySerializer(instance=self.category_test_1)

    def test_serializer(self):
        self.assertEqual(self.serializer.data['id'], self.category_test_1.id)
        self.assertEqual(
            self.serializer.data['name'], self.category_test_1.name
        )
        self.assertEqual(
            self.serializer.data['sections'][0]['id'], self.section_test_1.id
        )

        self.assertEqual(
            self.serializer.data['sections'][0]['name'],
            self.section_test_1.name,
        )

        self.assertEqual(
            self.serializer.data['sections'][1]['id'], self.section_test_2.id
        )

        self.assertEqual(
            self.serializer.data['sections'][1]['name'],
            self.section_test_2.name,
        )

    def test_serializer_list(self):
        self.assertEqual(self.serializer.data['id'], self.category_test_1.id)
        self.assertEqual(
            self.serializer.data['name'], self.category_test_1.name
        )
