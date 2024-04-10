from tests.base.base_test_case import BaseTestCase


class CategoryUrlTest(BaseTestCase):

    def test_category_url(self):
        response = self.client.get('/api/category/')
        self.assertEqual(response.status_code, 200)
