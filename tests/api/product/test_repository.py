from django.db.models import Prefetch

from api.models import AttributeProduct, Discount, InStock, Picture, Product
from api.repository import ProductRepository
from tests.base.base_test_case import BaseTestCase


class ProductRepositoryTest(BaseTestCase):
    def setUp(self) -> None:
        self.product_repository = ProductRepository()

    def test_product_model_property(self):
        self.assertEqual(self.product_repository.model, Product)

    def test_get_one_product(self):
        expected_result = self.product_repository.get_obj(self.product.pk)
        result = (
            Product.objects.filter(id=self.product.pk)
            .select_related('category', 'section', 'brand')
            .prefetch_related(
                Prefetch(
                    'product_images',
                    queryset=Picture.objects.select_related('product'),
                ),
                Prefetch(
                    'attributes',
                    queryset=AttributeProduct.objects.all(),
                ),
                Prefetch('discount', queryset=Discount.objects.all()),
            )
            .first()
        )

        self.assertEqual(expected_result, result)

    def test_get_all_products(self):
        expected_result = self.product_repository.get_all_objects_order_by_id()
        result = (
            Product.objects.select_related('category', 'brand', 'section')
            .prefetch_related(
                Prefetch(
                    'product_images',
                    queryset=Picture.objects.select_related('product'),
                ),
                Prefetch(
                    'attributes',
                    queryset=AttributeProduct.objects.all(),
                ),
                Prefetch('discount', queryset=Discount.objects.all()),
                Prefetch('in_stock', queryset=InStock.objects.all()),
            )
            .order_by('id')
        )

        self.assertEqual(list(expected_result), list(result))
