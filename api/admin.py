from django.contrib import admin

from api.models import Category, Picture, Product, Section


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'section')
    search_fields = ('id', 'name', 'section')
    list_filter = ('id', 'name', 'section')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')


@admin.register(Picture)
class ProductImage(admin.ModelAdmin):
    list_display = ('id', 'product', 'product_image')
    search_fields = ('id', 'product', 'product_image')
    list_filter = ('id', 'product', 'product_image')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    search_fields = ('id', 'name', 'description', 'price')
    list_filter = ('id', 'name', 'description', 'price')
