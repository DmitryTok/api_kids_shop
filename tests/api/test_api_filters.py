from api.filters import split_value
from tests.base.base_test_case import BaseTestCase


class ApiFiltersViewTest(BaseTestCase):

    def test_split_values_single(self):
        self.assertEqual(split_value('10'), 10)

    def test_split_values_multiple(self):
        self.assertEqual(split_value('5-15'), (5, 15))

    def test_api_filters(self):
        request = self.client.get('/api/filters/')
        self.assertIn('Brand', request.data)
        self.assertIn('Category', request.data)
        self.assertIn('Product', request.data)
        self.assertIn('Section', request.data)
