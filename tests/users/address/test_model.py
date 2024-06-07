from tests.base.base_test_case import BaseTestCase


class AddressModelTest(BaseTestCase):

    def test_str_representation(self):
        expected_result = 'first_delivery_address'
        self.assertEqual(expected_result, str(self.address))
