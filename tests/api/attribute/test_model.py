from tests.base.base_test_case import BaseTestCase


class AttributeModelTest(BaseTestCase):

    def test_str_representation(self):
        expected_str = 'Color'
        self.assertEqual(expected_str, str(self.attribute))
