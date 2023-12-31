import uuid
from enum import Enum

from django.core.validators import MinValueValidator
from django.db import models

from users.models import Profile


class Discount(models.Model):
    name = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    def __str__(self) -> str:
        return str(self.name)


class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.name}'


class Section(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='sections'
    )

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.name}'


class Size(models.Model):

    class LetterSizeChoices(Enum):
        DOUBLE_EXTRA_SMALL = 'XXS'
        EXTRA_SMALL = 'XS'
        SMALL = 'S'
        MEDIUM = 'M'
        LARGE = 'L'
        EXTRA_LARGE = 'XL'
        DOUBLE_EXTRA_LARGE = 'XXL'

    brand_size = models.PositiveSmallIntegerField(blank=True, null=True)
    letter_size = models.CharField(
        choices=[(choice.name, choice.value) for choice in LetterSizeChoices],
        default=None,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.letter_size}({str(self.brand_size)})'


class Color(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='product_categories'
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='product_sections'
    )
    description = models.CharField(max_length=2000)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='product_brands'
    )
    item_number = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    price = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    rating = models.FloatField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(0)]
    )
    male = models.BooleanField(default=True)
    is_sale = models.BooleanField(default=False)
    discount = models.ForeignKey(
        Discount,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.name}'


class InStock(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='in_stock'
    )
    color = models.ForeignKey(
        Color,
        blank=False,
        on_delete=models.CASCADE,
        related_name='in_stock'
    )
    product_size = models.ForeignKey(
        Size,
        blank=True,
        related_name='product_sizes',
        on_delete=models.CASCADE
    )
    in_stock = models.SmallIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )

    def __str__(self) -> str:
        return f'{self.color.name}'


class Picture(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='product_images',
        on_delete=models.CASCADE,
    )
    product_image = models.ImageField(upload_to='product_images')

    def __str__(self) -> str:
        return f'{self.product}: {self.product_image}'


class Favorite(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='favorites'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='favorites'
    )

    class Meta:
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=('profile', 'product'), name='unique_favorite_product'
            )
        ]


class ShoppingCart(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='shopping_carts'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='shopping_carts'
    )
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=('profile', 'product', 'quantity'), name='unique_shopping_cart'
            )
        ]

    def __str__(self) -> str:
        return f'{self.profile.user}: {self.product}'
