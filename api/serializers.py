from rest_framework import serializers

from api.models import Brand, Category, Favorite, Picture, Product, Section


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


class ProductListSerializer(serializers.ModelSerializer):
    product_images = PictureListSerializer(many=True, read_only=True)
    category = CategoryListSerializer(read_only=True)
    section = SectionListSerializer(read_only=True)
    brand = BrandListSerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'brand',
            'category',
            'section',
            'description',
            'price',
            'size',
            'rating',
            'product_images',
            'male',
            'color',
            'age',
            'is_sale',
            'item_number',
        )
        read_only_fields = fields


class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = Favorite
        fields = ('id', 'product')


class TOPProductListSerializer(ProductListSerializer):
    pass


class OnSaleProductSerializer(ProductListSerializer):
    pass
