from api.models import Favorite
from api.repository import FavoriteRepository
from tests.base.base_test_case import BaseTestCase


class ProductRepositoryTest(BaseTestCase):
    def setUp(self) -> None:
        self.favorite_repository = FavoriteRepository()

    def test_product_model_property(self):
        self.assertEqual(self.favorite_repository.model, Favorite)
