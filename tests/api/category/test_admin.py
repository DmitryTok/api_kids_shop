from django.contrib import admin
from rest_framework.test import APITestCase

from api.admin import CategoryAdmin
from api.models import Category


class CategoryTest(APITestCase):
    def setUp(self):
        self.site = admin.site
        self.category_admin = CategoryAdmin(Category, self.site)

    def test_inlines(self):
        category_inlines = [
            item.__name__ for item in self.category_admin.inlines
        ]

        expected_inlines = ['SectionInLine']

        self.assertEqual(category_inlines, expected_inlines)
