import datetime

from django.core.exceptions import ValidationError


def validate_date_format(value):
    try:
        datetime.datetime.strptime(value, '%d/%m/%Y')
        return True
    except ValueError:
        raise ValidationError(
            f'Incorrect date format{value}, must bee day/month/year'
        )
