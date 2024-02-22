from rest_framework.serializers import ModelSerializer, SerializerMethodField

from api.models import (Attribute, AttributeProduct, Brand, Category, Color,
                        Discount, Favorite, InStock, Picture, Product, Section,
                        ShoppingCart, Size)


class AttributeSerializer(ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'


class AttributeProductSerializer(ModelSerializer):
    class Meta:
        model = AttributeProduct
        fields = '__all__'


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


class CategorySerializer(ModelSerializer):
    sections = SectionSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'sections')


class DiscountSerializer(ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'amount', 'info', 'date_start', 'date_end')
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
    attributes = AttributeProductSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'


class FavoriteSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'profile', 'product')


class ShoppingCartSerializer(ModelSerializer):
    total_price = SerializerMethodField()

    class Meta:
        model = ShoppingCart
        fields = ('id', 'profile', 'product', 'quantity', 'total_price')

    @staticmethod
    def get_total_price(obj) -> int:
        price = 0
        price += int(obj.product.price * obj.quantity)
        return price
