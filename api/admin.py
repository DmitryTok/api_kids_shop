from django.contrib import admin

from api.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    search_fields = ('id', 'name', 'description', 'price')
    list_filter = ('id', 'name', 'description', 'price')
