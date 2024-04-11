from tests.base.base_test_case import BaseTestCase


class ProfileModelTest(BaseTestCase):
    def test_str_representation(self):
        expected_str = 'Doe'
        self.assertEqual(expected_str, str(self.profile))
