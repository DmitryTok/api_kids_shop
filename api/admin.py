from django.contrib import admin

from api import models


class ProductInline(admin.TabularInline):
    model = models.Product


class ProductInStockInline(admin.TabularInline):
    model = models.InStock
    readonly_fields = ('id',)
    extra = 1


class ProductAttributeInline(admin.TabularInline):
    model = models.AttributeProduct
    readonly_fields = ('id',)
    extra = 1


class SectionInLine(admin.TabularInline):
    model = models.Section
    extra = 1


class InStockInline(admin.TabularInline):
    model = models.InStock
    extra = 1


class ImageInline(admin.TabularInline):
    model = models.Picture
    extra = 1


@admin.register(models.AttributeProduct)
class AttributeProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Attribute)
class AttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Size)
class SizeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
        ProductAttributeInline,
        InStockInline,
    ]
    list_display = (
        'name',
        'price',
        'rating',
        'male',
        'discount',
    )
    list_display_links = ('name',)



@admin.register(models.Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'product')
    search_fields = ('id', 'profile', 'product')
    list_filter = ('id', 'profile', 'product')


@admin.register(models.ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'product')
    search_fields = ('id', 'profile', 'product')
    list_filter = ('id', 'profile', 'product')


@admin.register(models.InStock)
class InStockAdmin(admin.ModelAdmin):
    list_display = ('article', 'product', 'in_stock')
    list_display_links = ('article', 'product')
    search_fields = ('article', 'product__name')


@admin.register(models.Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['product']
    list_display_links = ['product']
