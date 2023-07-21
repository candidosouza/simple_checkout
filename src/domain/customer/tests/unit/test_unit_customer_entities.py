import unittest
from unittest.mock import patch
from dataclasses import FrozenInstanceError, is_dataclass
from src.domain.customer.entities import Customer


class TestCustomerUnit(unittest.TestCase):

    def test_if_is_dataclass(self):
        self.assertTrue(is_dataclass(Customer))

    def test_constructor(self):
        with patch.object(Customer, 'validate') as mock_validate:
            customer = Customer(
                name='John Doe',
                email='jhondoe@rmail.com',
            )
            mock_validate.assert_called_once()
            self.assertEqual(customer.name, 'John Doe')
            self.assertEqual(customer.email, 'jhondoe@rmail.com')
            self.assertEqual(customer.id, customer.unique_entity_id.id)
            self.assertEqual(customer.is_active, True)

            customer = Customer(
                name='John Doe',
                email='jhondoe@rmail.com',
                is_active=False,
            )
            self.assertEqual(customer.name, 'John Doe')
            self.assertEqual(customer.email, 'jhondoe@rmail.com')
            self.assertEqual(customer.id, customer.unique_entity_id.id)
            self.assertEqual(customer.is_active, False)

    def test_is_immutable(self):
        with patch.object(Customer, 'validate'):
            with self.assertRaises(FrozenInstanceError):
                value_object = Customer(name='test', email='test@rmail.com')
                value_object.name = 'fake id'

    def test_activate(self):
        with patch.object(Customer, 'validate'):
            customer = Customer(name='test', email='test@rmail.com', is_active=False)
            customer.activate()
            self.assertTrue(customer.is_active)

    def test_deactivate(self):
        with patch.object(Customer, 'validate'):
            customer = Customer(name='test', email='test@rmail.com')
            customer.deactivate()
            self.assertFalse(customer.is_active)

    def test_reward_point(self):
        with patch.object(Customer, 'validate'):
            customer = Customer(
                name='Jhon Doe',
                email='jhondoe@email.com'
            )
            self.assertEqual(customer.reward_point, 0)
            customer.add_reward_point(5)
            self.assertEqual(customer.reward_point, 5)
            customer.add_reward_point(5)
            self.assertEqual(customer.reward_point, 10)
            customer.add_reward_point(50)
            self.assertEqual(customer.reward_point, 60)
