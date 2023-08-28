from django.contrib import admin

from api import models


@admin.register(models.Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_filter = ('id', 'name',)


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_filter = ('id', 'name',)


@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('id', 'name', 'category')
    list_filter = ('id', 'name', 'category')


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')


@admin.register(models.Picture)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'product_image')
    search_fields = ('id', 'product', 'product_image')
    list_filter = ('id', 'product', 'product_image')


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')


@admin.register(models.CountrySize)
class CountrySizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'size', 'letter_size')
    search_fields = ('id', 'country', 'size', 'letter_size')
    list_filter = ('id', 'country', 'size', 'letter_size')


@admin.register(models.Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'height', 'age', 'brand_size', 'insole_size'
    )
    search_fields = (
        'id', 'height', 'age', 'brand_size', 'insole_size'
    )
    list_filter = (
        'id', 'height', 'age', 'brand_size', 'insole_size'
    )


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'rating', 'male', 'is_sale', 'discount')
    search_fields = ('id', 'name', 'price', 'rating', 'male', 'is_sale', 'discount')
    list_filter = ('id', 'name', 'price', 'rating', 'male', 'is_sale', 'discount')


@admin.register(models.Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')
    search_fields = ('id', 'user', 'product')
    list_filter = ('id', 'user', 'product')


@admin.register(models.ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')
    search_fields = ('id', 'user', 'product')
    list_filter = ('id', 'user', 'product')
