from rest_framework.serializers import ModelSerializer

from api.models import (Brand, Category, Color, Discount, Favorite, InStock,
                        Picture, Product, Section, ShoppingCart, Size)


class PictureSerializer(ModelSerializer):

    class Meta:
        model = Picture
        fields = ('id', 'product', 'product_image')
        read_only_fields = fields


class BrandSerializer(ModelSerializer):

    class Meta:
        model = Brand
        fields = ('id', 'name')
        read_only_fields = fields


class SectionSerializer(ModelSerializer):

    class Meta:
        model = Section
        fields = ('id', 'name')
        read_only_fields = fields


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = fields


class DiscountSerializer(ModelSerializer):

    class Meta:
        model = Discount
        fields = ('id', 'name')
        read_only_fields = fields


class SizeSerializer(ModelSerializer):

    class Meta:
        model = Size
        fields = '__all__'


class ColorSerializer(ModelSerializer):

    class Meta:
        model = Color
        fields = ('id', 'name')
        read_only_fields = fields


class InStockSerializer(ModelSerializer):
    color = ColorSerializer(read_only=True)
    product_size = SizeSerializer(read_only=True)

    class Meta:
        model = InStock
        fields = ('id', 'color', 'product_size', 'in_stock')


class ProductSerializer(ModelSerializer):
    product_images = PictureSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    section = SectionSerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    discount = DiscountSerializer(read_only=True)
    in_stock = InStockSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'


class FavoriteSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Favorite
        fields = ('id', 'product')


class ShoppingCartSerializer(ModelSerializer):

    class Meta:
        model = ShoppingCart
        fields = ('user', 'product')
