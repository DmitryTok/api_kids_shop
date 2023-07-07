from api.repository import CategoryRepository, PictureRepository, ProductRepository, SectionRepository
from api.serializers import CategoryListSerializer, PictureListSerializer, ProductListSerializer, SectionListSerializer
from kids_shop.base.base_retrieve_hendler import BaseRetrieveViewSet


class ProductListView(BaseRetrieveViewSet):
    product_repository = ProductRepository()
    queryset = product_repository.get_all_objects_order_by_id()
    serializer_class = ProductListSerializer


class SectionListView(BaseRetrieveViewSet):
    section_repository = SectionRepository()
    queryset = section_repository.get_all_objects_order_by_id()
    serializer_class = SectionListSerializer


class PictureListView(BaseRetrieveViewSet):
    picture_repository = PictureRepository()
    queryset = picture_repository.get_all_objects_order_by_id()
    serializer_class = PictureListSerializer


class CategoryListView(BaseRetrieveViewSet):
    category_repository = CategoryRepository()
    queryset = category_repository.get_all_objects_order_by_id()
    serializer_class = CategoryListSerializer
