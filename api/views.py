from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.models import Product
from api.serializers import ProductListSerializer
from kids_shop.permissions import IsAdminOrReadOnly


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductListSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = LimitOffsetPagination
