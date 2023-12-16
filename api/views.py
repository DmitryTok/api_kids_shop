from django.http import HttpRequest
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.filters import ProductFilter
from api.repository import (
    BrandRepository,
    CategoryRepository,
    FavoriteRepository,
    PictureRepository,
    ProductRepository,
    SectionRepository,
    ShoppingCartRepository
)
from api.serializers import (
    BrandSerializer,
    CategorySerializer,
    FavoriteSerializer,
    PictureSerializer,
    ProductSerializer,
    SectionSerializer,
    ShoppingCartSerializer
)
from api.utils import favorite_or_cart, get_products
from kids_shop.base.base_retrieve_hendler import BaseRetrieveViewSet
from kids_shop.permissions import IsOwner, IsOwnerFavoriteOrCart
from users.users_repository import ProfileRepository


class ListCreateDeleteViewSet(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    pass


class ProductListView(BaseRetrieveViewSet):
    product_repository = ProductRepository()
    favorite_repository = FavoriteRepository()
    shopping_cart_repository = ShoppingCartRepository()
    profile_repository = ProfileRepository()
    queryset = product_repository.get_all_objects_order_by_id()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    @action(
        detail=False,
        methods=['POST', 'DELETE'],
        permission_classes=[IsOwnerFavoriteOrCart],
        url_path=r'(?P<product_id>\d+)/favorite/(?P<profile_id>\d+)'
    )
    def favorite(self, request: HttpRequest, product_id: int, profile_id: int) -> Response:
        return favorite_or_cart(
            request=request,
            product_id=product_id,
            profile_id=profile_id,
            profile_repository=self.profile_repository,
            product_repository=self.product_repository,
            repository=self.favorite_repository,
            obj_serializer=FavoriteSerializer,
            is_shop=False
        )

    @action(
        detail=False,
        methods=['POST', 'DELETE'],
        permission_classes=[IsOwnerFavoriteOrCart],
        url_path=r'(?P<product_id>\d+)/(?P<quantity>\d+)/shopping_cart/(?P<profile_id>\d+)'
    )
    def shopping_card(
            self,
            request: HttpRequest,
            profile_id: int,
            product_id: int,
            quantity: int
    ) -> Response:
        return favorite_or_cart(
            request=request,
            product_id=product_id,
            profile_id=profile_id,
            profile_repository=self.profile_repository,
            product_repository=self.product_repository,
            repository=self.shopping_cart_repository,
            obj_serializer=ShoppingCartSerializer,
            quantity=quantity,
            is_shop=True
        )

    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[IsOwnerFavoriteOrCart],
        url_path=r'favorite/(?P<profile_id>\d+)'
    )
    def get_favorite(self, request: HttpRequest, profile_id: int) -> Response:
        return get_products(
            request=request,
            profile_id=profile_id,
            repository=self.favorite_repository,
            obj_serializer=FavoriteSerializer
        )
    
    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[IsOwnerFavoriteOrCart],
        url_path=r'shopping_cart/(?P<profile_id>\d+)'
    )
    def get_shopping_cart(self, request: HttpRequest, profile_id: int) -> Response:
        return get_products(
            request=request,
            profile_id=profile_id,
            repository=self.shopping_cart_repository,
            obj_serializer=ShoppingCartSerializer
        )


class CategoryListView(BaseRetrieveViewSet):
    category_repository = CategoryRepository()
    queryset = category_repository.get_all_objects_order_by_id()
    serializer_class = CategorySerializer
    filterset_fields = ['name']

class SectionListView(BaseRetrieveViewSet):
    section_repository = SectionRepository()
    queryset = section_repository.get_all_objects_order_by_id()
    serializer_class = SectionSerializer
    filterset_fields = ['name']


class BranListView(BaseRetrieveViewSet):
    brand_repository = BrandRepository()
    queryset = brand_repository.get_all_objects_order_by_id()
    serializer_class = BrandSerializer
    filterset_fields = ['name']


class PictureListView(BaseRetrieveViewSet):
    picture_repository = PictureRepository()
    queryset = picture_repository.get_all_objects_order_by_id()
    serializer_class = PictureSerializer


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
    permission_classes = [IsOwner]
