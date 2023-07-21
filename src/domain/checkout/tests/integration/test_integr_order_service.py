import unittest

from src.domain.checkout.entities import Order, OrderItem
from src.domain.checkout.service.services import OrderService
from src.domain.customer.entities import Customer


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

    def test_get_total_of_all_order_with_one_item(self):
        data = {
            'customer_id': '123',
            'items': [
                OrderItem(
                    name='Product 1',
                    product_id='123',
                    quantity=1,
                    price=10.00,
                )
            ]
        }
        order = Order(**data)
        total = OrderService.total(order)
        self.assertEqual(total, 10.00)

    def test_get_total_of_all_order_without_item(self):
        data = {
            'customer_id': '123',
            'items': []
        }
        order = Order(**data)
        total = OrderService.total(order)
        self.assertEqual(total, 0.00)

    def test_place_an_order(self):
        customer = Customer(
            name='Jhon Doe',
            email='jhondow@email.com',
        )
        data = {
            'customer': customer,
            'items': [
                OrderItem(
                    name='Product 1',
                    product_id='123',
                    quantity=1,
                    price=10.00,
                )
            ]
        }
        order = OrderService.place_order(**data)
        total = OrderService.total(order)
        self.assertEqual(customer.reward_point, 5)
        self.assertEqual(total, 10.00)

        customer = Customer(
            name='Jhon Doe',
            email='jhondow@email.com',
        )
        data = {
            'customer': customer,
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
        order = OrderService.place_order(**data)
        total = OrderService.total(order)
        self.assertEqual(customer.reward_point, 40)
        self.assertEqual(total, 80.00)

    def test_place_an_order_without_items(self):
        customer = Customer(
            name='Jhon Doe',
            email='jhondoe@email.com'
        )
        data = {
            'customer': customer,
            'items': []
        }
        with self.assertRaises(ValueError) as context:
            OrderService.place_order(**data)
        self.assertEqual(str(context.exception), 'Order must have at least one item')
