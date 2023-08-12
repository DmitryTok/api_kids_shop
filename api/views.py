from rest_framework import mixins, viewsets

from api import repository, serializers
from api.models import Favorite
from kids_shop.base.base_retrieve_hendler import BaseRetrieveViewSet


class ListCreateDeleteViewset(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    pass


class ProductListView(BaseRetrieveViewSet):
    product_repository = repository.ProductRepository()
    queryset = product_repository.get_all_objects_order_by_id()
    serializer_class = serializers.ProductListSerializer


class CategoryListView(BaseRetrieveViewSet):
    category_repository = repository.CategoryRepository()
    queryset = category_repository.get_all_objects_order_by_id()
    serializer_class = serializers.CategoryListSerializer


class SectionListView(BaseRetrieveViewSet):
    section_repository = repository.SectionRepository()
    queryset = section_repository.get_all_objects_order_by_id()
    serializer_class = serializers.SectionListSerializer


class BranListView(BaseRetrieveViewSet):
    brand_repository = repository.BrandRepository()
    queryset = brand_repository.get_all_objects_order_by_id()
    serializer_class = serializers.BrandListSerializer


class PictureListView(BaseRetrieveViewSet):
    picture_repository = repository.PictureRepository()
    queryset = picture_repository.get_all_objects_order_by_id()
    serializer_class = serializers.PictureListSerializer


class FavoriteViewSet(ListCreateDeleteViewset):
    queryset = Favorite.objects.all()
    serializer_class = serializers.FavoriteSerializer


class TOPProductView(BaseRetrieveViewSet):
    product_repository = repository.ProductRepository()
    queryset = product_repository.get_sorted_product_by_rate()
    serializer_class = serializers.TOPProductListSerializer
    pagination_class = None


class OnSaleProductView(BaseRetrieveViewSet):
    product_repository = repository.ProductRepository()
    queryset = product_repository.get_sorted_products_by_sale()
    serializer_class = serializers.OnSaleProductSerializer
    pagination_class = None
