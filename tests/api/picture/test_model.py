from tests.base.base_test_case import BaseTestCase


class PictureModelTest(BaseTestCase):

    def test_str_representation(self):
        expected_tr = 'Product: image.png'
        self.assertEqual(expected_tr, str(self.picture))
