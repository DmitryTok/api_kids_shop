from django.db.models import F, Prefetch

from api.models import Category, Section
from api.repository import CategoryRepository
from tests.base.base_test_case import BaseTestCase


class CategoryRepositoryTest(BaseTestCase):
    def setUp(self) -> None:
        self.category_repository = CategoryRepository()

    def test_category_model_property(self):
        self.assertEqual(self.category_repository.model, Category)

    def test_get_all_categories(self):
        expected_result = (
            self.category_repository.get_all_objects_order_by_id()
        )
        result = Category.objects.prefetch_related(
            Prefetch(
                'sections',
                queryset=Section.objects.annotate(section_name=F('name')),
            )
        ).order_by('id')

        self.assertEqual(list(expected_result), list(result))
