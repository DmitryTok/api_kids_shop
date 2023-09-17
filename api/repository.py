from api import models
from kids_shop.base.base_repository import BaseRepository


class ProductRepository(BaseRepository):

    @property
    def model(self) -> type[models.Product]:
        return models.Product

    def get_sorted_product_by_rate(self):
        return self.model.objects.order_by('-rating')

    def get_sorted_products_by_sale(self):
        return self.model.objects.filter(is_sale=True)


class SectionRepository(BaseRepository):

    @property
    def model(self) -> type[models.Section]:
        return models.Section


class PictureRepository(BaseRepository):

    @property
    def model(self) -> type[models.Picture]:
        return models.Picture


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

    def get_all_users_products(self, user_id):
        return self.model.objects.filter(user=user_id).count()
