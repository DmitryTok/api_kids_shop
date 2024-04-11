from tests.base.base_test_case import BaseTestCase


class KidModelTest(BaseTestCase):

    def test_str_representation(self):
        expected_result = 'MaleChoices.Male'
        self.assertEqual(expected_result, str(self.kid))
