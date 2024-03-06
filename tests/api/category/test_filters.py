from rest_framework.test import APITestCase

from api.filters import CategoryFilter
from api.models import Category


class CategoryFilterTest(APITestCase):
    def setUp(self) -> None:
        self.filter = CategoryFilter(data={}, queryset=Category.objects.all())
        self.filter_none = CategoryFilter(
            data={'name': 'Unexpected Name'}, queryset=Category.objects.all()
        )

        Category.objects.create(name='Test_1')
        Category.objects.create(name='Test_2')
        Category.objects.create(name='Test_3')

    def test_name_filter(self):
        self.assertIn('Test_1', [category.name for category in self.filter.qs])
        self.assertEqual(self.filter.qs.count(), 3)

    def test_name_not_exists(self):
        self.assertEqual(self.filter_none.qs.count(), 0)

    def test_empty_name_filter(self):
        expected_result = ['Test_1', 'Test_2', 'Test_3']
        self.assertEqual(
            expected_result, [category.name for category in self.filter.qs]
        )
