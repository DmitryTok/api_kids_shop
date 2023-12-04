from enum import Enum

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import validate_email
from django.db import models

from users.validators import validate_date_format


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', False)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, validators=[validate_email])
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Kid(models.Model):

    class MaleChoices(Enum):
        Male = 'Boy'
        Female = 'Girl'

    male = models.CharField(
        choices=[(male.value, male.name) for male in MaleChoices],
        blank=True,
        null=True
    )
    birth_date = models.CharField(
        blank=True,
        null=True,
        validators=[validate_date_format]
    )

    def __str__(self) -> str:
        return str(self.male)


class Address(models.Model):
    first_delivery_address = models.CharField(
        blank=False,
        null=False
    )
    second_delivery_address = models.CharField(
        blank=True,
        null=True
    )
    city = models.CharField(
        blank=False,
        null=False
    )
    street = models.CharField(
        blank=False,
        null=False
    )
    building = models.CharField(
        blank=False,
        null=False
    )
    apartment = models.IntegerField(
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.first_delivery_address}'


class Profile(models.Model):
    class GenderChoices(Enum):
        Man = 'Man'
        Woman = 'Woman'

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='users_profile',
        blank=False,
        null=False
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name='users_address',
        blank=True,
        null=True
    )
    kids = models.ManyToManyField(
        Kid,
        blank=True,
        related_name='profile_kids'
    )
    gender = models.CharField(
        choices=[(gender.value, gender.name) for gender in GenderChoices],
        blank=True,
        null=True
    )
    first_name = models.CharField(
        max_length=125,
        blank=True,
        null=True
    )
    middle_name = models.CharField(
        max_length=125,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=125,
        blank=True,
        null=True
    )
    birth_date = models.CharField(
        blank=True,
        null=True,
        validators=[validate_date_format]
    )
    first_phone = models.IntegerField(
        blank=True,
        null=True
    )
    second_phone = models.IntegerField(
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.last_name}'
