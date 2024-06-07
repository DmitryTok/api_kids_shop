from tests.base.base_test_case import BaseTestCase
from users.models import CustomUser
from users.users_repository import UserRepository


class UserRepositoryTest(BaseTestCase):

    def setUp(self) -> None:
        self.user_repository = UserRepository()

    def test_user_model_property(self):
        self.assertEqual(self.user_repository.model, CustomUser)

    def test_get_user_obj(self):
        expected_result = self.user_repository.get_user_obj(
            user_id=self.user.pk
        )
        result = CustomUser.objects.get(id=self.user.pk)

        self.assertEqual(expected_result, result)
