from django.db.models import F, Prefetch, Subquery

from api import models
from kids_shop.base.base_repository import BaseRepository


class ProductRepository(BaseRepository):
    @property
    def model(self) -> type[models.Product]:
        return models.Product

    def get_obj(self, product_id: int) -> models.Product:
        return (
            self.model.objects.filter(id=product_id)
            .select_related('category', 'section', 'brand')
            .prefetch_related(
                Prefetch(
                    'product_images',
                    queryset=models.Picture.objects.select_related('product'),
                ),
                Prefetch(
                    'attributes',
                    queryset=models.AttributeProduct.objects.all(),
                ),
                Prefetch('discount', queryset=models.Discount.objects.all()),
            )
            .first()
        )

    def get_all_objects_order_by_id(self) -> models.Product:
        return (
            self.model.objects.select_related('category', 'brand', 'section')
            .prefetch_related(
                Prefetch(
                    'product_images',
                    queryset=models.Picture.objects.select_related('product'),
                ),
                Prefetch(
                    'attributes',
                    queryset=models.AttributeProduct.objects.all(),
                ),
                Prefetch('discount', queryset=models.Discount.objects.all()),
                Prefetch('in_stock', queryset=models.InStock.objects.all()),
            )
            .order_by('id')
        )

    def get_sorted_products_by_sale(self) -> models.Product:
        return (
            self.model.objects.filter(discount__isnull=False)
            .select_related('category', 'section', 'brand')
            .prefetch_related(
                Prefetch(
                    'product_images',
                    queryset=models.Picture.objects.select_related('product'),
                ),
                Prefetch(
                    'attributes',
                    queryset=models.AttributeProduct.objects.all(),
                ),
                Prefetch('discount', queryset=models.Discount.objects.all()),
            )
        ).order_by('discount')


class PictureRepository(BaseRepository):
    @property
    def model(self) -> type[models.Picture]:
        return models.Picture

    def get_all_objects_order_by_id(self) -> models.Picture:
        return self.model.objects.select_related('product').order_by('id')


class CategoryRepository(BaseRepository):
    @property
    def model(self) -> type[models.Category]:
        return models.Category

    def get_all_objects_order_by_id(self):
        return self.model.objects.prefetch_related(
            Prefetch(
                'sections',
                queryset=models.Section.objects.annotate(
                    section_name=F('name')
                ),
            )
        ).order_by('id')


class SectionRepository(BaseRepository):
    @property
    def model(self) -> type[models.Section]:
        return models.Section

    def get_all_objects_order_by_id(self) -> models.Section:
        return self.model.objects.values('id', 'name')


class BrandRepository(BaseRepository):
    @property
    def model(self) -> type[models.Brand]:
        return models.Brand


class FavoriteRepository(BaseRepository):
    @property
    def model(self) -> type[models.Favorite]:
        return models.Favorite

    def get_all_products(self, profile_id: int) -> models.Product:
        favorite_products = self.model.objects.filter(profile_id=profile_id)
        return ProductRepository().model.objects.filter(
            id__in=Subquery(favorite_products.values('product_id'))
        )
    
    def get_obj(self, profile_id: int, product_id: int) -> models.Favorite:
        return self.model.objects.filter(
            profile_id=profile_id, product_id=product_id
        )
    
    def create_obj(self, profile, product) -> models.Favorite:
        return self.model.objects.create(profile=profile, product=product)



class ShoppingCartRepository(BaseRepository):
    @property
    def model(self) -> type[models.ShoppingCart]:
        return models.ShoppingCart
