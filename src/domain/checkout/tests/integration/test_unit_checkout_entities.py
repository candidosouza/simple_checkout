import unittest
from unittest.mock import patch
from dataclasses import FrozenInstanceError, is_dataclass
from src.domain.checkout.entities import Order, OrderItem
from src.domain.customer.entities import Customer
from src.domain.customer.value_object import Address


class TestOrderIntegr(unittest.TestCase):
    def test_create_order(self):
        data_address = {
            'street': 'fake street',
            'number': 123,
            'zip': '00000-000',
            'city': 'fake city'
        }
        customer = Customer(name='Test', email='test@email.com')
        address = Address(**data_address)
        customer.add_address(address)
        items = [
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
            )
        ]
        data = {
            'customer_id': customer.id,
            'items': items
        }
        order = Order(**data)
        self.assertEqual(order.customer_id, customer.id)
        self.assertEqual(order.items, items)
        
        self.assertEqual(order.items[0].name, items[0].name)
        self.assertEqual(order.items[0].product_id, items[0].product_id)
        self.assertEqual(order.items[0].quantity, items[0].quantity)
        self.assertEqual(order.items[0].price, items[0].price)
        self.assertEqual(order.items[0].total(), 10.00)

        self.assertEqual(order.items[1].name, items[1].name)
        self.assertEqual(order.items[1].product_id, items[1].product_id)
        self.assertEqual(order.items[1].quantity, items[1].quantity)
        self.assertEqual(order.items[1].price, items[1].price)
        self.assertEqual(order.items[1].total(), 40.00)
