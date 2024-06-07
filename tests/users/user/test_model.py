from tests.base.base_test_case import BaseTestCase
from users.models import CustomUser


class CustomUserModelTest(BaseTestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            email='user@example.com', password='password'
        )
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_active)

    def test_create_superuser(self):
        superuser = CustomUser.objects.create_superuser(
            email='321@example.com', password='adminpassword'
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)

    def test_create_superuser_with_invalid_flags(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                email='123@example.com',
                password='adminpassword1',
                is_staff=False,
            )
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                email='231@example.com',
                password='adminpassword2',
                is_superuser=False,
            )

    def test_create_user_with_no_email(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(
                email='',
                password='adminpassword2',
            )
