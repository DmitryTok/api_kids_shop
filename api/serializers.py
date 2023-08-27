from rest_framework import serializers

from api.models import Brand, Category, Color, Country, CountrySize, Discount, Favorite, Picture, Product, Section, Size


class PictureListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ('id', 'product', 'product_image')
        read_only_fields = fields


class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('id', 'name')
        read_only_fields = fields


class SectionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ('id', 'name')
        read_only_fields = fields


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = fields


class DiscountListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = ('id', 'name')
        read_only_fields = fields


class ColorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ('id', 'name')
        read_only_fields = fields


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CountrySizeSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = CountrySize
        fields = ('size', 'country')


class SizeSerializer(serializers.ModelSerializer):
    country_size = CountrySizeSerializer(many=True, read_only=True)

    class Meta:
        model = Size
        exclude = [
            'brand',
            'height',
            'chest_size',
            'waist_size',
            'arm_length',
            'age',
            'brand_size',
            'insole_size'
        ]


class ProductListSerializer(serializers.ModelSerializer):
    product_images = PictureListSerializer(many=True, read_only=True)
    category = CategoryListSerializer(read_only=True)
    section = SectionListSerializer(read_only=True)
    brand = BrandListSerializer(read_only=True)
    discount = DiscountListSerializer(read_only=True)
    color = ColorListSerializer(many=True, read_only=True)
    product_size = SizeSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = (fields,)


class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = Favorite
        fields = ('id', 'product')
