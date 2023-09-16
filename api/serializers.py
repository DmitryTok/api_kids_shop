from rest_framework.serializers import ModelSerializer

from api.models import (Brand, Category, Color, Discount, Favorite, Picture,
                        Product, Section, ShoppingCart, Size)


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
    product_size = SizeSerializer(read_only=True)

    class Meta:
        model = Color
        fields = ('id', 'name', 'product_size')
        read_only_fields = fields


class ProductSerializer(ModelSerializer):
    product_images = PictureSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    section = SectionSerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    discount = DiscountSerializer(read_only=True)
    color = ColorSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = (fields,)


class FavoriteSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Favorite
        fields = ('id', 'product')


class ShoppingCartSerializer(ModelSerializer):

    class Meta:
        model = ShoppingCart
        fields = ('user', 'product')
