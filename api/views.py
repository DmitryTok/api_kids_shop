from rest_framework import mixins, status, viewsets
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
    def favorite(self, request, product_id: int, profile_id: int) -> Response:
        profile = self.profile_repository.get_obj(profile_id)
        product = self.product_repository.get_obj(product_id)

        if request.method == 'POST':
            if self.favorite_repository.get_obj(
                    profile_id,
                    product_id).exists():
                return Response(
                    {'error': 'This product already in favorite'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            favorite = self.favorite_repository.create_obj(profile, product)
            serializer = FavoriteSerializer(favorite)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'DELETE':
            favorite = self.favorite_repository.get_obj(profile_id, product_id)
            if favorite.exists():
                favorite.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=False,
        methods=['POST', 'DELETE'],
        permission_classes=[IsOwnerFavoriteOrCart],
        url_path=r'(?P<product_id>\d+)/shopping_cart/(?P<profile_id>\d+)/(?P<quantity>\d+)'
    )
    def shopping_card(self, request,  profile_id: int, product_id: int, quantity: int) -> Response:
        profile = self.profile_repository.get_obj(profile_id)
        product = self.product_repository.get_obj(product_id)

        if request.method == 'POST':
            if self.shopping_cart_repository.get_obj(
                    profile_id,
                    product_id).exists():
                return Response(
                    {'error': 'This product already in favorite'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            favorite = self.shopping_cart_repository.create_obj(
                profile,
                product,
                quantity
            )
            serializer = ShoppingCartSerializer(favorite)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'DELETE':
            cart = self.shopping_cart_repository.get_obj(
                profile_id,
                product_id
            )
            if cart.exists():
                cart.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[IsOwnerFavoriteOrCart],
        url_path=r'favorite/(?P<profile_id>\d+)'
    )
    def get_favorite(self, request, profile_id: int) -> Response:
        favorites = self.favorite_repository.get_all_products(profile_id)
        serializer = FavoriteSerializer(favorites, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[IsOwnerFavoriteOrCart],
        url_path=r'shopping_cart/(?P<profile_id>\d+)'
    )
    def get_shopping_cart(self, request, profile_id: int) -> Response:
        cart = self.shopping_cart_repository.get_all_products(profile_id)
        serializer = ShoppingCartSerializer(cart, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


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
