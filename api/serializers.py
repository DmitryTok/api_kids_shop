from rest_framework import serializers

from api import models


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Picture
        fields = ('id', 'product', 'product_image')
        read_only_fields = fields


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Brand
        fields = ('id', 'name')
        read_only_fields = fields


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Section
        fields = ('id', 'name')
        read_only_fields = fields


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ('id', 'name')
        read_only_fields = fields


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Discount
        fields = ('id', 'name')
        read_only_fields = fields


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Color
        fields = ('id', 'name')
        read_only_fields = fields


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = ('name',)


class CountrySizeSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = models.CountrySize
        fields = ('size', 'letter_size', 'country')


class SizeSerializer(serializers.ModelSerializer):
    country_size = CountrySizeSerializer(many=True, read_only=True)

    class Meta:
        model = models.Size
        exclude = [
            'id',
            'brand',
            'height',
            'chest_size',
            'waist_size',
            'arm_length',
            'age',
            'brand_size',
            'insole_size'
        ]


class ProductSerializer(serializers.ModelSerializer):
    product_images = PictureSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    section = SectionSerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    discount = DiscountSerializer(read_only=True)
    color = ColorSerializer(many=True, read_only=True)
    product_size = SizeSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = '__all__'
        read_only_fields = (fields,)


class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = models.Favorite
        fields = ('id', 'product')
