from rest_framework.reverse import reverse

from tests.base.base_test_case import BaseTestCase


class CategoryViewTest(BaseTestCase):

    def test_list_view(self):
        response = self.client.get(reverse('category-list'))

        self.assertEqual(response.status_code, 200)

    def test_retrieve_view(self):
        response = self.client.get(
            reverse('category-detail', args=[self.category.id])
        )

        self.assertEqual(response.status_code, 200)
