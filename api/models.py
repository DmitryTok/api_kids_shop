from enum import Enum

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Sum, F

from users.models import Profile
from users.models import CustomUser
from users.models import Address


class GenderChoices(models.IntegerChoices):
    male = 0
    female = 1
    father = 2
    mother = 3
    babies = 4


class Discount(models.Model):
    amount = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    info = models.CharField(max_length=120)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.amount} {self.info}'


class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

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
        null=True,
    )


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
    description = models.CharField(max_length=2000)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='product_brands',
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        null=False,
        blank=True,
        verbose_name='Price',
    )
    rating = models.FloatField(null=True, blank=True)
    male = models.IntegerField(
        choices=GenderChoices.choices, default=GenderChoices.male
    )
    discount = models.ForeignKey(
        Discount,
        related_name='discount',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f'{self.name}'


class Attribute(models.Model):
    name = models.CharField(
        max_length=120,
        unique=True,
        db_index=True,
    )
    is_global = models.BooleanField(default=False)
    widget = models.CharField(max_length=120)
    extra = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class AttributeProduct(models.Model):
    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='attributes',
    )
    attribute_name = models.CharField(
        max_length=120,
        db_index=True,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='attributes',
    )
    value = models.CharField(max_length=120)

    def __str__(self) -> str:
        return f'{self.attribute_name} {self.value}'


class InStock(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='in_stock',
    )
    article = models.CharField(
        max_length=50,
        unique=True,
    )
    in_stock = models.SmallIntegerField(
        blank=True, null=True, validators=[MinValueValidator(0)]
    )

    def __str__(self) -> str:
        return f'{self.product.name} {self.article}'


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
        Profile, on_delete=models.CASCADE, related_name='favorites'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='favorites'
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
        Profile, on_delete=models.CASCADE, related_name='shopping_carts'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='shopping_carts'
    )
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    class Meta:
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=('profile', 'product', 'quantity'),
                name='unique_shopping_cart',
            )
        ]


class Promocode(models.Model):
    code = models.CharField(max_length=150, unique=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, default=None)
    usage_limit = models.PositiveIntegerField(null=True, blank=True)
    times_used = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.code

    def is_valid(self):
        if self.discount.date_end < timezone.now():
            return False
        if self.usage_limit is not None and self.times_used >= self.usage_limit:
            return False
        return True


ORDER_STATUS_CHOICES = (
    (0, 'Pending'),
    (1, 'Confirmed'),
    (2, 'Declined'),
    (3, 'Out for shipping'),
    (4, 'Completed'),
)

PAYMENT_STATUS_CHOICES = (
    (0, 'Unpaid'),
    (1, 'Paid'),
    (2, 'Refunded'),
)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    patronymic = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50,
        choices=ORDER_STATUS_CHOICES,
        default=0
    )
    payment_status = models.CharField(
        max_length=50,
        choices=PAYMENT_STATUS_CHOICES,
        default=0
    )
    promocode = models.ForeignKey(
        Promocode,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    comment = models.TextField(blank=True, null=True)
    # TODO: tracking_number?

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'

    def get_status_display(self):
        return ORDER_STATUS_CHOICES[self.status][1]

    def get_payment_status_display(self):
        return PAYMENT_STATUS_CHOICES[self.payment_status][1]

    def calculate_total_price(self):
        total_price = OrderedProduct.objects.filter(
            order=self
        ).aggregate(
            total_price=models.Sum(models.F('price') * models.F('quantity'))
        )['total_price'] or 0.00
        self.total_price = total_price
        # TODO: calculate with promocode
        self.save(update_fields=['total_price'])


class OrderedProduct(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='ordered_products',
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        null=False,
        blank=True,
        verbose_name='Price',
    )
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return f'{self.product.name} ({self.quantity}) in Order {self.order.id}'
