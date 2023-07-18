from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import Category, Favorite, Picture, Product, Section, ShoppingCart
from users.serializers import CustomUserShoppingCartSerializer


class PictureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'product', 'product_image')
        read_only_fields = fields


class SectionListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'category')
        read_only_fields = fields


class CategoryListSerializer(serializers.ModelSerializer):
    section = SectionListSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'section')
        read_only_fields = fields


class ProductListSerializer(serializers.ModelSerializer):
    product_images = PictureListSerializer(many=True, read_only=True)
    category = CategoryListSerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'description',
            'price',
            'rating',
            'product_images',
            'male'
        )
        read_only_fields = fields


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'user', 'product')


class ShoppingCartSerializer(serializers.ModelSerializer):
    user = CustomUserShoppingCartSerializer()

    class Meta:
        model = ShoppingCart
        fields = ('id', 'user')

    def validate(self, data):
        user = data['user']
        product_id = data['product'].id
        if ShoppingCart.objects.filter(
                user=user, product__id=product_id).exists():
            raise ValidationError('Item already in shopping cart')
        return data
