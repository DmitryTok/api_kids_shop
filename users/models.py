from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, validators=[validate_email])
    username = models.CharField(max_length=70, unique=True)
