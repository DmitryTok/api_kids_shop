from rest_framework.test import APITestCase

from api.filters import SectionFilter
from api.models import Section


class SectionFilterTest(APITestCase):
    def setUp(self) -> None:
        self.filter = SectionFilter(data={}, queryset=Section.objects.all())
        self.filter_none = SectionFilter(
            data={'name': 'Unexpected Name'}, queryset=Section.objects.all()
        )

        Section.objects.create(name='Test_1')
        Section.objects.create(name='Test_2')
        Section.objects.create(name='Test_3')

    def test_name_filter(self):
        self.assertIn('Test_1', [section.name for section in self.filter.qs])
        self.assertEqual(self.filter.qs.count(), 3)

    def test_name_not_exists(self):
        self.assertEqual(self.filter_none.qs.count(), 0)

    def test_empty_name_filter(self):
        expected_result = ['Test_1', 'Test_2', 'Test_3']
        self.assertEqual(
            expected_result, [section.name for section in self.filter.qs]
        )
