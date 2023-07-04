from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=2000)
    price = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    rating = models.FloatField(null=True, blank=True)
    image = models.ImageField(
        upload_to='data/',
        null=True,
        blank=True
    )
    male = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} ${self.price}'
