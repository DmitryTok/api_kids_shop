from django.db.models import Prefetch

from api import models
from api.models import InStock, Picture
from kids_shop.base.base_repository import BaseRepository


class ProductRepository(BaseRepository):

    @property
    def model(self) -> type[models.Product]:
        return models.Product

    def get_all_objects_order_by_id(self):
        return self.model.objects.select_related(
            'category',
            'section',
            'brand',
            'discount'
        ).prefetch_related(
            Prefetch(
                'in_stock',
                queryset=InStock.objects.select_related(
                    'product',
                    'color',
                    'product_size'
                )
            ),
            Prefetch(
                'product_images',
                queryset=Picture.objects.select_related('product')
            )
        )

    def get_sorted_product_by_rate(self):
        return self.model.objects.select_related(
            'category',
            'section',
            'brand',
            'discount'
        ).prefetch_related(
            Prefetch(
                'in_stock',
                queryset=InStock.objects.select_related(
                    'product',
                    'color',
                    'product_size'
                )
            ),
            Prefetch(
                'product_images',
                queryset=Picture.objects.select_related('product')
            )
        ).order_by('-rating')

    def get_sorted_products_by_sale(self):
        return self.model.objects.filter(is_sale=True).select_related(
            'category',
            'section',
            'brand',
            'discount'
        ).prefetch_related(
            Prefetch(
                'in_stock',
                queryset=InStock.objects.select_related(
                    'product',
                    'color',
                    'product_size'
                )
            ),
            Prefetch(
                'product_images',
                queryset=Picture.objects.select_related('product')
            )
        ).order_by('-rating')


class SectionRepository(BaseRepository):

    @property
    def model(self) -> type[models.Section]:
        return models.Section

    def get_all_objects_order_by_id(self):
        return self.model.objects.values('id', 'name')


class PictureRepository(BaseRepository):

    @property
    def model(self) -> type[models.Picture]:
        return models.Picture

    def get_all_objects_order_by_id(self):
        return self.model.objects.select_related('product')


class CategoryRepository(BaseRepository):

    @property
    def model(self) -> type[models.Category]:
        return models.Category


class BrandRepository(BaseRepository):

    @property
    def model(self) -> type[models.Product]:
        return models.Brand


class FavoriteRepository(BaseRepository):

    @property
    def model(self) -> type[models.Favorite]:
        return models.Favorite


class ShoppingCartRepository(BaseRepository):

    @property
    def model(self) -> type[models.ShoppingCart]:
        return models.ShoppingCart
