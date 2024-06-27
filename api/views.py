from django.http import HttpRequest
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.filters import (
    BrandFilter,
    CategoryFilter,
    ProductFilter,
    SectionFilter
)
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
    ShoppingCartSerializer
)
from api.utils import favorite_or_cart, get_products, store_filters
from kids_shop.base.base_retrieve_handler import BaseRetrieveViewSet
from kids_shop.permissions import IsOwner, IsOwnerFavoriteOrCart
from users.users_repository import ProfileRepository


class ListCreateDeleteViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    pass


class ProductListView(BaseRetrieveViewSet):
    product_repository = ProductRepository()
    favorite_repository = FavoriteRepository()
    shopping_cart_repository = ShoppingCartRepository()
    profile_repository = ProfileRepository()
    queryset = product_repository.get_all_objects_order_by_id()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def base_action_sorted_response(
        self, request: HttpRequest, field: str
    ) -> Response:
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.order_by(field)

        page = self.paginate_queryset(obj)
        if page:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        description='Get all products ordered by price from max to min',
        request=ProductSerializer,
        responses={200: ProductSerializer()},
        parameters=[
            OpenApiParameter(
                name='limit',
                description='Number of objects to return per page.',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name='offset',
                description='The initial number from which object to return the results.',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
        ],
    )
    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[AllowAny],
        url_path=r'max_price',
    )
    def max_price(self, request: HttpRequest) -> Response:
        return self.base_action_sorted_response(request, '-price')

    @extend_schema(
        description='Get all products ordered by price from max to min',
        request=ProductSerializer,
        responses={200: ProductSerializer()},
        parameters=[
            OpenApiParameter(
                name='limit',
                description='Number of objects to return per page.',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name='offset',
                description='The initial number from which object to return the results.',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
        ],
    )
    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[AllowAny],
        url_path=r'min_price',
    )
    def min_price(self, request: HttpRequest) -> Response:
        return self.base_action_sorted_response(request, 'price')

    @extend_schema(
        description='Get all products ordered by price from max to min',
        request=ProductSerializer,
        responses={200: ProductSerializer()},
        parameters=[
            OpenApiParameter(
                name='limit',
                description='Number of objects to return per page.',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name='offset',
                description='The initial number from which object to return the results.',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
        ],
    )
    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[AllowAny],
        url_path=r'rating',
    )
    def rating(self, request: HttpRequest) -> Response:
        return self.base_action_sorted_response(request, 'rating')

    @extend_schema(
        description='Get all products ordered by price from max to min',
        request=ProductSerializer,
        responses={200: ProductSerializer()},
        parameters=[
            OpenApiParameter(
                name='limit',
                description='Number of objects to return per page.',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name='offset',
                description='The initial number from which object to return the results.',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
        ],
    )
    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[AllowAny],
        url_path=r'sale',
    )
    def sale(self, request: HttpRequest) -> Response:
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.filter(discount__isnull=False)

        page = self.paginate_queryset(obj)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        description='Get all products ordered by price from max to min',
        request=ProductSerializer,
        responses={200: ProductSerializer()},
        parameters=[
            OpenApiParameter(
                name='limit',
                description='Number of objects to return per page.',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name='offset',
                description='The initial number from which object to return the results.',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
        ],
    )
    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[AllowAny],
        url_path=r'min_sale',
    )
    def min_sale(self, request: HttpRequest) -> Response:
        return self.base_action_sorted_response(request, 'discount')

    @extend_schema(
        description='Get all products ordered by price from max to min',
        request=ProductSerializer,
        responses={200: ProductSerializer()},
        parameters=[
            OpenApiParameter(
                name='limit',
                description='Number of objects to return per page.',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name='offset',
                description='The initial number from which object to return the results.',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
        ],
    )
    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[AllowAny],
        url_path=r'max_sale',
    )
    def max_sale(self, request: HttpRequest) -> Response:
        return self.base_action_sorted_response(request, '-discount')

    @action(
        detail=False,
        methods=['POST', 'DELETE'],
        permission_classes=[IsOwnerFavoriteOrCart],
        url_path=r'(?P<product_id>\d+)/favorite/(?P<profile_id>\d+)',
    )
    def favorite(
        self, request: HttpRequest, product_id: int, profile_id: int
    ) -> Response:
        return favorite_or_cart(
            request=request,
            product_id=product_id,
            profile_id=profile_id,
            profile_repository=self.profile_repository,
            product_repository=self.product_repository,
            repository=self.favorite_repository,
            obj_serializer=FavoriteSerializer,
            is_shop=False,
        )

    @action(
        detail=False,
        methods=['POST', 'DELETE'],
        permission_classes=[IsOwnerFavoriteOrCart],
        url_path=r'(?P<product_id>\d+)/(?P<quantity>\d+)/shopping_cart/(?P<profile_id>\d+)',
    )
    def shopping_card(
        self,
        request: HttpRequest,
        profile_id: int,
        product_id: int,
        quantity: int,
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
            is_shop=True,
        )

    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[IsOwnerFavoriteOrCart],
        url_path=r'favorite/(?P<profile_id>\d+)',
    )
    def get_favorite(self, request: HttpRequest, profile_id: int) -> Response:
        return get_products(
            request=request,
            profile_id=profile_id,
            repository=self.favorite_repository,
            obj_serializer=FavoriteSerializer,
        )

    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[IsOwnerFavoriteOrCart],
        url_path=r'shopping_cart/(?P<profile_id>\d+)',
    )
    def get_shopping_cart(
        self, request: HttpRequest, profile_id: int
    ) -> Response:
        return get_products(
            request=request,
            profile_id=profile_id,
            repository=self.shopping_cart_repository,
            obj_serializer=ShoppingCartSerializer,
        )


class CategoryListView(BaseRetrieveViewSet):
    category_repository = CategoryRepository()
    queryset = category_repository.get_all_objects_order_by_id()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter


class SectionListView(BaseRetrieveViewSet):
    section_repository = SectionRepository()
    queryset = section_repository.get_all_objects_order_by_id()
    serializer_class = None
    filterset_class = SectionFilter


class BranListView(BaseRetrieveViewSet):
    brand_repository = BrandRepository()
    queryset = brand_repository.get_all_objects_order_by_id()
    serializer_class = BrandSerializer
    filterset_class = BrandFilter


class PictureListView(BaseRetrieveViewSet):
    picture_repository = PictureRepository()
    queryset = picture_repository.get_all_objects_order_by_id()
    serializer_class = PictureSerializer


class ShoppingCartViewSet(ListCreateDeleteViewSet):
    shopping_cart_repository = ShoppingCartRepository()
    queryset = shopping_cart_repository.get_all_objects_order_by_id()
    serializer_class = ShoppingCartSerializer
    permission_classes = [IsOwner]


@api_view(['GET'])
def api_filters(request: HttpRequest) -> Response:
    return Response(store_filters())
