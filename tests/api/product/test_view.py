from tests.base.base_test_case import BaseTestCase


class ProductListViewTestCase(BaseTestCase):

    def test_max_price(self):
        request = self.client.get('/api/products/max_price/')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(len(request.data), 1)

    def test_min_price(self):
        request = self.client.get('/api/products/min_price/')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(len(request.data), 1)

    def test_rating(self):
        request = self.client.get('/api/products/rating/')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(len(request.data), 1)
