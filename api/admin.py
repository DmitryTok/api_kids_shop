from django.contrib import admin
from django.db.models import Sum

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


# class DiscountInline(admin.TabularInline):
#     model = models.Discount
#     extra = 0


@admin.register(models.AttributeProduct)
class AttributeProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Attribute)
class AttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'id',
        'name',
    )
    list_filter = (
        'id',
        'name',
    )


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


@admin.register(models.Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_size', 'letter_size')
    search_fields = ('id', 'brand_size', 'letter_size')
    list_filter = ('id', 'brand_size', 'letter_size')


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAttributeInline,]

    def in_stock_display(self, obj):
        in_stock_info = obj.in_stock.all()
        return ', '.join(
            [
                f"{item.product.id} {item.article}: {item.in_stock}"
                for item in in_stock_info
            ]
        )

    def get_queryset(self, request):
        queryset = (
            super()
            .get_queryset(request)
            .annotate(total_in_stock=Sum('in_stock__in_stock'))
        )
        return queryset

    def total_in_stock(self, obj):
        return obj.total_in_stock

    in_stock_display.short_description = 'In Stock'


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
    list_display = ('id', 'product', 'article', 'in_stock')
    search_fields = ('id', 'product', 'article',  'in_stock')
    list_filter = ('id', 'product', 'article',  'in_stock')
