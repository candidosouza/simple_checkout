import unittest
from src.domain.product.service.services import ProductService
from src.domain.product.entities import Product, ProductStatus


class TestProductServiceIntegr(unittest.TestCase):

    def test_change_the_prices_of_all_products(self):
        product1 = Product(name='Product 1', price=10.00, status="enabled")
        product2 = Product(name='Product 2', price=20.00, status=ProductStatus.ENABLED.value)
        ProductService.increasePrice(products=[product1, product2], percentage=100)
        self.assertEqual(product1.price, 20.00)
        self.assertEqual(product2.price, 40.00)
