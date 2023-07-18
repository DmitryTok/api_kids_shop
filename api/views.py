from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from api import repository, serializers
from kids_shop.base.base_retrieve_hendler import BaseRetrieveViewSet
from kids_shop.permissions import IsAdminOrAuthorPermission


class ListCreateDeleteViewset(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    pass


class ProductListView(BaseRetrieveViewSet):
    product_repository = repository.ProductRepository()
    queryset = product_repository.get_all_objects_order_by_id()
    serializer_class = serializers.ProductListSerializer


class SectionListView(BaseRetrieveViewSet):
    section_repository = repository.SectionRepository()
    queryset = section_repository.get_all_objects_order_by_id()
    serializer_class = serializers.SectionListSerializer


class PictureListView(BaseRetrieveViewSet):
    picture_repository = repository.PictureRepository()
    queryset = picture_repository.get_all_objects_order_by_id()
    serializer_class = serializers.PictureListSerializer


class CategoryListView(BaseRetrieveViewSet):
    category_repository = repository.CategoryRepository()
    queryset = category_repository.get_all_objects_order_by_id()
    serializer_class = serializers.CategoryListSerializer


class FavoriteView(ListCreateDeleteViewset):
    favorite_repository = repository.FavoriteRepository()
    queryset = favorite_repository.get_all_objects_order_by_id()
    serializer_class = serializers.FavoriteSerializer
    permission_classes = (IsAuthenticated, IsAdminOrAuthorPermission,)


class ShoppingCartView(ListCreateDeleteViewset):
    shoppingcart_repository = repository.ShoppingCartRepository()
    queryset = shoppingcart_repository.get_all_objects_order_by_id()
    serializer_class = serializers.ShoppingCartSerializer
    permission_classes = (IsAdminOrAuthorPermission,)
