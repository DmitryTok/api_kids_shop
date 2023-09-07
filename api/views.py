from rest_framework import mixins, viewsets

from api.repository import (BrandRepository, CategoryRepository,
                            FavoriteRepository, PictureRepository,
                            ProductRepository, SectionRepository,
                            ShoppingCartRepository)
from api.serializers import (BrandSerializer, CategorySerializer,
                             FavoriteSerializer, PictureSerializer,
                             ProductSerializer, SectionSerializer,
                             ShoppingCartSerializer)
from kids_shop.base.base_retrieve_hendler import BaseRetrieveViewSet


class ListCreateDeleteViewSet(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    pass


class ProductListView(BaseRetrieveViewSet):
    product_repository = ProductRepository()
    queryset = product_repository.get_all_objects_order_by_id()
    serializer_class = ProductSerializer
    filterset_fields = ['category__name', 'section__name', 'brand', 'price', 'rating', 'age', 'male']


class CategoryListView(BaseRetrieveViewSet):
    category_repository = CategoryRepository()
    queryset = category_repository.get_all_objects_order_by_id()
    serializer_class = CategorySerializer


class SectionListView(BaseRetrieveViewSet):
    section_repository = SectionRepository()
    queryset = section_repository.get_all_objects_order_by_id()
    serializer_class = SectionSerializer


class BranListView(BaseRetrieveViewSet):
    brand_repository = BrandRepository()
    queryset = brand_repository.get_all_objects_order_by_id()
    serializer_class = BrandSerializer


class PictureListView(BaseRetrieveViewSet):
    picture_repository = PictureRepository()
    queryset = picture_repository.get_all_objects_order_by_id()
    serializer_class = PictureSerializer


class FavoriteViewSet(ListCreateDeleteViewSet):
    favorite_repository = FavoriteRepository()
    queryset = favorite_repository.get_all_objects_order_by_id()
    serializer_class = FavoriteSerializer


class TOPProductView(BaseRetrieveViewSet):
    product_repository = ProductRepository()
    queryset = product_repository.get_sorted_product_by_rate()
    serializer_class = ProductSerializer
    pagination_class = None


class OnSaleProductView(BaseRetrieveViewSet):
    product_repository = ProductRepository()
    queryset = product_repository.get_sorted_products_by_sale()
    serializer_class = ProductSerializer
    pagination_class = None


class ShoppingCartViewSet(ListCreateDeleteViewSet):
    shopping_cart_repository = ShoppingCartRepository()
    queryset = shopping_cart_repository.get_all_objects_order_by_id()
    serializer_class = ShoppingCartSerializer
