from rest_framework.test import APITestCase


class CategoryUrlTest(APITestCase):

    def test_category_url(self):
        response = self.client.get('/api/category/')
        self.assertEqual(response.status_code, 200)
