from api.models import Section
from api.repository import SectionRepository
from tests.base.base_test_case import BaseTestCase


class SectionRepositoryTest(BaseTestCase):
    def setUp(self) -> None:
        self.section_repository = SectionRepository()

    def test_category_model_property(self):
        self.assertEqual(self.section_repository.model, Section)

    def test_get_all_categories(self):
        expected_result = self.section_repository.get_all_objects_order_by_id()
        result = Section.objects.values('id', 'name').order_by('id')

        self.assertEqual(list(expected_result), list(result))
