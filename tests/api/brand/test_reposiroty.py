from api.models import Brand
from api.repository import BrandRepository
from tests.base.base_test_case import BaseTestCase


class BrandRepositoryTest(BaseTestCase):
    def setUp(self) -> None:
        self.brand_repository = BrandRepository()

    def test_category_model_property(self):
        self.assertEqual(self.brand_repository.model, Brand)

    def test_get_all_categories(self):
        expected_result = self.brand_repository.get_all_objects_order_by_id()
        result = Brand.objects.all().order_by('id')

        self.assertEqual(list(expected_result), list(result))
