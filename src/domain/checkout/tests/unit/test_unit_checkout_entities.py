import unittest
from unittest.mock import patch
from dataclasses import FrozenInstanceError, is_dataclass
from src.domain.checkout.entities import Order, OrderItem


class TestOrderUnit(unittest.TestCase):

    def test_if_is_dataclass(self):
        self.assertTrue(is_dataclass(Order))

    def test_constructor(self):
        order = Order(
            customer_id='123',
            items=[
                {
                    'name': 'Product 1',
                    'product_id': '123',
                    'quantity': 1,
                    'price': 10.00,
                },
                {
                    'name': 'Product 2',
                    'product_id': '456',
                    'quantity': 2,
                    'price': 20.00,
                },
            ]
        )
        self.assertEqual(order.customer_id, '123')
        self.assertEqual(len(order.items), 2)


class TestOrderItemUnit(unittest.TestCase):

    def test_if_is_dataclass(self):
        self.assertTrue(is_dataclass(OrderItem))

    def test_constructor(self):
        with patch.object(OrderItem, 'validate') as mock_validate:
            data = {
                'name': 'Product 1',
                'product_id': '123',
                'quantity': 1,
                'price': 10.00,
            }
            order_item = OrderItem(**data)
            mock_validate.assert_called_once()
            self.assertEqual(order_item.name, 'Product 1')
            self.assertEqual(order_item.product_id, '123')
            self.assertEqual(order_item.quantity, 1)
            self.assertEqual(order_item.price, 10.00)

    def test_total(self):
        with patch.object(OrderItem, 'validate'):
            order_item = OrderItem(
                name='Product 1',
                product_id='123',
                quantity=1,
                price=10.00,
            )
            self.assertEqual(order_item.total(), 10.00)
            order_item = OrderItem(
                name='Product 2',
                product_id='1234',
                quantity=7,
                price=17.00,
            )
            self.assertEqual(order_item.total(), 119.00)
            order_item = OrderItem(
                name='Product 3',
                product_id='1234',
                quantity=7,
                price=1.00,
            )
            self.assertEqual(order_item.total(), 7.00)


