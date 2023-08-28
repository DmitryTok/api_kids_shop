from rest_framework import mixins, viewsets

from api import repository, serializers
from api.models import Favorite
from kids_shop.base.base_retrieve_hendler import BaseRetrieveViewSet


class ListCreateDeleteViewSet(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    pass


class ProductListView(BaseRetrieveViewSet):
    product_repository = repository.ProductRepository()
    queryset = product_repository.get_all_objects_order_by_id()
    serializer_class = serializers.ProductSerializer


class CategoryListView(BaseRetrieveViewSet):
    category_repository = repository.CategoryRepository()
    queryset = category_repository.get_all_objects_order_by_id()
    serializer_class = serializers.CategorySerializer


class SectionListView(BaseRetrieveViewSet):
    section_repository = repository.SectionRepository()
    queryset = section_repository.get_all_objects_order_by_id()
    serializer_class = serializers.SectionSerializer


class BranListView(BaseRetrieveViewSet):
    brand_repository = repository.BrandRepository()
    queryset = brand_repository.get_all_objects_order_by_id()
    serializer_class = serializers.BrandSerializer


class PictureListView(BaseRetrieveViewSet):
    picture_repository = repository.PictureRepository()
    queryset = picture_repository.get_all_objects_order_by_id()
    serializer_class = serializers.PictureSerializer


class FavoriteViewSet(ListCreateDeleteViewSet):
    queryset = Favorite.objects.all()
    serializer_class = serializers.FavoriteSerializer


class TOPProductView(BaseRetrieveViewSet):
    product_repository = repository.ProductRepository()
    queryset = product_repository.get_sorted_product_by_rate()
    serializer_class = serializers.ProductSerializer
    pagination_class = None


class OnSaleProductView(BaseRetrieveViewSet):
    product_repository = repository.ProductRepository()
    queryset = product_repository.get_sorted_products_by_sale()
    serializer_class = serializers.ProductSerializer
    pagination_class = None
