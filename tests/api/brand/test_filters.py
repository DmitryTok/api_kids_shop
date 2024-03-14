from rest_framework.test import APITestCase

from api.filters import BrandFilter
from api.models import Brand


class BrandFilterTest(APITestCase):
    def setUp(self) -> None:
        self.filter = BrandFilter(data={}, queryset=Brand.objects.all())
        self.filter_none = BrandFilter(
            data={'name': 'Unexpected Name'}, queryset=Brand.objects.all()
        )

        Brand.objects.create(name='Test_1')
        Brand.objects.create(name='Test_2')
        Brand.objects.create(name='Test_3')

    def test_name_filter(self):
        self.assertIn('Test_1', [brand.name for brand in self.filter.qs])
        self.assertEqual(self.filter.qs.count(), 3)

    def test_name_not_exists(self):
        self.assertEqual(self.filter_none.qs.count(), 0)

    def test_empty_name_filter(self):
        expected_result = ['Test_1', 'Test_2', 'Test_3']
        self.assertEqual(
            expected_result, [brand.name for brand in self.filter.qs]
        )
