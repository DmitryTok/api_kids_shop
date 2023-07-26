from rest_framework import generics, mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api import repository, serializers
from api.models import Favorite
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


class FavoriteViewSet(ListCreateDeleteViewset):
    queryset = Favorite.objects.all()
    serializer_class = serializers.FavoriteSerializer
