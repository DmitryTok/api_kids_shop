from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from api.models import Category


class CategoryViewTest(APITestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(name='TestCategory')

    def test_list_view(self):
        response = self.client.get(reverse('category-list'))

        self.assertEqual(response.status_code, 200)

    def test_retrieve_view(self):
        response = self.client.get(
            reverse('category-detail', args=[self.category.id])
        )

        self.assertEqual(response.status_code, 200)
