from django.forms import ValidationError

from tests.base.base_test_case import BaseTestCase
from users.validators import validate_date_format


class TestValidateDateFormat(BaseTestCase):
    def test_valid_date_format(self):
        valid_date = '15/04/2024'
        self.assertTrue(validate_date_format(valid_date))

    def test_invalid_date_format(self):
        invalid_date = '2024-04-15'
        with self.assertRaises(ValidationError):
            validate_date_format(invalid_date)
