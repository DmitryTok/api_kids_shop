from rest_framework.serializers import ModelSerializer, CharField

from api.models import (Attribute, AttributeProduct, Brand, Category, Discount,
                        Favorite, InStock, Picture, Product, Section,
                        ShoppingCart, OrderedProduct, Order, Size)


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
        fields = ('id', 'name', 'country')
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


class CategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class DiscountSerializer(ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'amount', 'info', 'date_start', 'date_end')
        read_only_fields = fields


class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class InStockSerializer(ModelSerializer):
    product_size = SizeSerializer(read_only=True)

    class Meta:
        model = InStock
        fields = ('id', 'product_size', 'in_stock')


class ProductSerializer(ModelSerializer):
    product_images = PictureSerializer(many=True, read_only=True)
    category = CategoryListSerializer(read_only=True)
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

    class Meta:
        model = ShoppingCart
        fields = ('id', 'profile', 'product', 'quantity')


class OrderedProductSerializer(ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = ['product', 'price', 'quantity']


class OrderSerializer(ModelSerializer):
    ordered_products = OrderedProductSerializer(many=True)
    promocode = CharField(max_length=150, required=False, allow_blank=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'patronymic',
            'email',
            'phone',
            'address',
            'total_price',
            'created_at',
            'updated_at',
            'status',
            'payment_status',
            'promocode',
            'comment',
            'ordered_products',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'status', 'total_price']
