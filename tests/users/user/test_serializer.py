from tests.base.base_test_case import BaseTestCase
from users.models import CustomUser
from users.serializers import CustomUserCreateSerializer


class UserSerializerTest(BaseTestCase):

    def setUp(self) -> None:
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword123',
        }

    def test_serializer_valid(self):
        serializer = CustomUserCreateSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())

    def test_create_serializer(self):
        serializer = CustomUserCreateSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertIsInstance(user, CustomUser)
        self.assertEqual(user.email, self.user_data['email'])
