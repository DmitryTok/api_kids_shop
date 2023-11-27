from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
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
from kids_shop.permissions import IsOwner
from users.users_repository import UserRepository


class ListCreateDeleteViewSet(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    pass


class ProductListView(BaseRetrieveViewSet):
    product_repository = ProductRepository()
    favorite_repository = FavoriteRepository()
    user_repository = UserRepository()
    queryset = product_repository.get_all_objects_order_by_id()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    
    @action(
        detail=True,
        methods=['POST'],
        permission_classes=[IsAuthenticated]
    )
    def favorite(self, request, pk=None) -> Response:
        product = self.product_repository.get_all_objects_order_by_id().get(pk=pk)
        user = self.user_repository.get_user_obj(request.user.id)

        if self.favorite_repository.get_filter_obj(user, product):
            return Response({'Error': 'Product already in favorite'}, status=status.HTTP_400_BAD_REQUEST)

        favorite = self.favorite_repository.create_obj(user, product)
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
