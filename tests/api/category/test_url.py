from tests.base.base_test_case import BaseTestCase


class CategoryUrlTest(BaseTestCase):

    def test_all_category_url(self):
        response = self.client.get('/api/category/')
        self.assertEqual(response.status_code, 200)

    def test_category_url(self):
        response = self.client.get(f'/api/category/{self.category.pk}/')
        self.assertEqual(response.status_code, 200)
