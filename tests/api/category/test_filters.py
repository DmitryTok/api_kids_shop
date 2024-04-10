from api.filters import CategoryFilter
from api.models import Category
from tests.base.base_test_case import BaseTestCase


class CategoryFilterTest(BaseTestCase):
    def setUp(self) -> None:
        self.filter = CategoryFilter(data={}, queryset=Category.objects.all())
        self.filter_none = CategoryFilter(
            data={'name': 'Unexpected Name'}, queryset=Category.objects.all()
        )

    def test_name_filter(self):
        self.assertIn(
            'Category_Test_1', [category.name for category in self.filter.qs]
        )
        self.assertEqual(self.filter.qs.count(), 4)

    def test_name_not_exists(self):
        self.assertEqual(self.filter_none.qs.count(), 0)

    def test_empty_name_filter(self):
        expected_result = [
            'Category',
            'Category_Test_1',
            'Category_Test_2',
            'Category_Test_3',
        ]
        self.assertEqual(
            expected_result, [category.name for category in self.filter.qs]
        )
