from api.filters import ProductFilter
from api.models import Product
from tests.base.base_test_case import BaseTestCase


class ProductFilterTest(BaseTestCase):
    def setUp(self) -> None:
        self.filter = ProductFilter(data={}, queryset=Product.objects.all())

    def test_filter_age(self):
        filtered_queryset = self.filter.filter_age(
            queryset=self.filter.queryset, name='age', value=20
        )
        self.assertEqual(filtered_queryset.count(), 0)
