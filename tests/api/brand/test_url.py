from tests.base.base_test_case import BaseTestCase


class BrandUrlTest(BaseTestCase):

    def test_all_brands_url(self):
        response = self.client.get('/api/brand/')
        self.assertEqual(response.status_code, 200)

    def test_brand_url(self):
        response = self.client.get(f'/api/brand/{self.brand.pk}/')
        self.assertEqual(response.status_code, 200)
