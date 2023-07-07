from typing import Type

from api import models
from kids_shop.base.base_repository import BaseRepository


class ProductRepository(BaseRepository):

    @property
    def model(self) -> Type[models.Product]:
        return models.Product


class SectionRepository(BaseRepository):

    @property
    def model(self) -> Type[models.Section]:
        return models.Section


class PictureRepository(BaseRepository):

    @property
    def model(self) -> Type[models.Picture]:
        return models.Picture


class CategoryRepository(BaseRepository):

    @property
    def model(self) -> Type[models.Category]:
        return models.Category
