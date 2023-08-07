from django.contrib import admin

from api.models import Category, Favorite, Picture, Product, Section, ShoppingCart


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_filter = ('id', 'name',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('id', 'name', 'category')
    list_filter = ('id', 'name', 'category')


@admin.register(Picture)
class ProductImage(admin.ModelAdmin):
    list_display = ('id', 'product', 'product_image')
    search_fields = ('id', 'product', 'product_image')
    list_filter = ('id', 'product', 'product_image')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'rating', 'size', 'color', 'male', 'category')
    search_fields = ('id', 'name', 'description', 'price', 'rating', 'size', 'color', 'male', 'category')
    list_filter = ('id', 'name', 'description', 'price', 'rating', 'size', 'color', 'male', 'category')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')
    search_fields = ('id', 'user', 'product')
    list_filter = ('id', 'user', 'product')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')
    search_fields = ('id', 'user', 'product')
    list_filter = ('id', 'user', 'product')
