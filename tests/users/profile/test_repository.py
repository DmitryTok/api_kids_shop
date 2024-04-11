from tests.base.base_test_case import BaseTestCase
from users.models import Profile
from users.users_repository import ProfileRepository


class ProfileRepositoryTest(BaseTestCase):

    def setUp(self):
        self.profile_repository = ProfileRepository()

    def test_get_obj(self):
        expected_result = self.profile_repository.get_obj(
            profile_id=self.profile.pk
        )
        result = Profile.objects.get(id=self.profile.pk)

        self.assertEqual(expected_result, result)
