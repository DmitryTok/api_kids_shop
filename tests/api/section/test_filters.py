from api.filters import SectionFilter
from api.models import Section
from tests.base.base_test_case import BaseTestCase


class SectionFilterTest(BaseTestCase):
    def setUp(self) -> None:
        self.filter = SectionFilter(data={}, queryset=Section.objects.all())
        self.filter_none = SectionFilter(
            data={'name': 'Unexpected Name'}, queryset=Section.objects.all()
        )

    def test_name_filter(self):
        self.assertIn(
            'Section_Test_1', [section.name for section in self.filter.qs]
        )
        self.assertEqual(self.filter.qs.count(), 4)

    def test_name_not_exists(self):
        self.assertEqual(self.filter_none.qs.count(), 0)

    def test_empty_name_filter(self):
        expected_result = [
            'Section',
            'Section_Test_1',
            'Section_Test_2',
            'Section_Test_3',
        ]
        self.assertEqual(
            expected_result, [section.name for section in self.filter.qs]
        )
