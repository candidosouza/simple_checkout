import unittest

from src.domain.checkout.entities import Order, OrderItem
from src.domain.checkout.service.services import OrderService


class TestOrderServiceIntegr(unittest.TestCase):

    def test_get_total_of_all_order(self):
        data = {
            'customer_id': '123',
            'items': [
                OrderItem(
                    name='Product 1',
                    product_id='123',
                    quantity=1,
                    price=10.00,
                ),
                OrderItem(
                    name='Product 2',
                    product_id='456',
                    quantity=2,
                    price=20.00,
                ),
                OrderItem(
                    name='Product 3',
                    product_id='789',
                    quantity=3,
                    price=10.00,
                )
            ]
        }
        order = Order(**data)
        total = OrderService.total(order)
        self.assertEqual(total, 80.00)

