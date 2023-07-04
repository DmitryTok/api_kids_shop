from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from api.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'rating', 'image', 'male')
        read_only_fields = fields
