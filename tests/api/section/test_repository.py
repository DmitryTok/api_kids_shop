from rest_framework.test import APITestCase

from api.models import Section
from api.repository import SectionRepository


class SectionRepositoryTest(APITestCase):
    def setUp(self) -> None:
        self.section = Section.objects.create(name='Test')
        self.section_repository = SectionRepository()

    def test_category_model_property(self):
        self.assertEqual(self.section_repository.model, Section)

    def test_get_all_categories(self):
        expected_result = self.section_repository.get_all_objects_order_by_id()
        result = Section.objects.values('id', 'name').order_by('id')

        self.assertEqual(list(expected_result), list(result))
