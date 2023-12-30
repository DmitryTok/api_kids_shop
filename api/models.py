import uuid
from enum import Enum
from typing import Any

from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

from users.models import Profile

import logging
log = logging.getLogger(__name__)


class Discount(models.Model):
    name = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    def __str__(self) -> str:
        return str(self.name)


class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)
    logo = GenericRelation("ImageModel")

    def __str__(self) -> str:
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Section(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='sections',
    )

    def __str__(self) -> str:
        return f'{self.name}'


class Atribute(models.Model):
    name = models.CharField(
        max_length=120,
        unique=True,
        db_index=True
    )
    is_global = models.BooleanField(default=False)
    widget = models.CharField(max_length=120)
    extra = models.JSONField(blank=True, null=True)  # Maybe GenericForeignKey

    def __str__(self) -> str:
        return f'{self.name}'


class AtributeCategory(models.Model):
    atribute = models.ForeignKey(
        Atribute,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='atributes',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='category'
    )  # Maybe GenericForeignKey to Category or Section

    def __str__(self) -> str:
        return f'{self.atribute}'


class AtributeProducts(models.Model):
    atribute = models.ForeignKey(
        Atribute,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='atributes',
    )
    __atribute_name = models.CharField(max_length=120)
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='product',
    )  # Maybe GenericForeignKey to Category or Section
    value = models.CharField(max_length=120)

    def __str__(self) -> str:
        return f'{self.atribute}'


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
    # Choices are stored in the database as strings
    letter_size = models.CharField(
        choices=[(choice.name, choice.value) for choice in LetterSizeChoices],
        default=None,
        blank=True,
        null=True,
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
        related_name='product_categories',
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='product_sections',
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='product_brands',
    )
    item_number = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=False
    )
    description = models.CharField(max_length=2000)
    price = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    rating = models.FloatField(null=True, blank=True)

    male = models.BooleanField(default=True)  # Choise

    age = models.PositiveSmallIntegerField(
        null=False, blank=False, validators=[MinValueValidator(0)]
    )

    is_sale = models.BooleanField(default=False)  # Fk

    discount = models.ForeignKey(
        Discount, on_delete=models.CASCADE, blank=True, null=True
    )  # Fk

    image = GenericRelation("ImageModel")

    def __str__(self) -> str:
        return f'{self.name}'


class InStock(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='in_stock',
    )
    color = models.ForeignKey(
        Color, blank=False, on_delete=models.CASCADE, related_name='in_stock'
    )
    product_size = models.ForeignKey(
        Size,
        blank=True,
        related_name='product_sizes',
        on_delete=models.CASCADE,
    )
    in_stock = models.SmallIntegerField(
        blank=True, null=True, validators=[MinValueValidator(0)]
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

# https://docs.djangoproject.com/en/5.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericRelation
def directory_path(instance: Any, filename: str, base_folder: str = 'data') -> str:
    log.error(f"instance: {instance} type={type(instance)}")
    log.error(f'{dir(instance)}')
    return f"{base_folder}/{instance.pk}/{filename}"


class ImageModel(models.Model):
    image = models.ImageField(upload_to=directory_path)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.image.url

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]


class Favorite(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='favorites'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='favorites'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        constraints = [
            models.UniqueConstraint(
                fields=('profile', 'product'), name='unique_favorite_product'
            )
        ]


class ShoppingCart(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='shopping_carts'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='shopping_carts'
    )
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', 'quantity')
        constraints = [
            models.UniqueConstraint(
                fields=('profile', 'product', 'quantity'),  # ??
                name='unique_shopping_cart',
            )
        ]

    def __str__(self) -> str:
        return f'{self.profile.user}: {self.product}'
