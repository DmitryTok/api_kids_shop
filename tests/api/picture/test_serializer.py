from api.serializers import PictureSerializer
from tests.base.base_test_case import BaseTestCase


class PictureSerializerTest(BaseTestCase):

    def setUp(self) -> None:
        self.serializer = PictureSerializer(instance=self.picture)

    def test_serializer(self):
        self.assertEqual(self.serializer.data['id'], self.picture.id)
