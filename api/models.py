from django.core.validators import MinValueValidator
from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    description = models.CharField(max_length=2000)
    price = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    rating = models.FloatField(null=True, blank=True)
    male = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} ${self.price}'


class Picture(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='product_images',
        on_delete=models.CASCADE
    )
    product_image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f'{self.product}: {self.product_image}'
