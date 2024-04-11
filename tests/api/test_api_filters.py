from tests.base.base_test_case import BaseTestCase


class ApiFiltersViewTest(BaseTestCase):

    def test_api_filters(self):
        request = self.client.get('/api/filters/')
        self.assertIn('Brand', request.data)
        self.assertIn('Category', request.data)
        self.assertIn('Product', request.data)
        self.assertIn('Section', request.data)
