import unittest
from src.domain.customer.entities import Customer
from src.domain.customer.value_object import Address

from src.domain.shared.exceptions import ValidationException

class TestCustomerIntegration(unittest.TestCase):

    def test_create_with_invalid_cases_for_name_prop(self):
        with self.assertRaises(ValidationException) as assert_error:
            Customer(name=None, email='test@email.com')
        self.assertEqual(
            assert_error.exception.args[0], 'The name is required')

        with self.assertRaises(ValidationException) as assert_error:
            Customer(name='')
        self.assertEqual(
            assert_error.exception.args[0], 'The name is required')

        with self.assertRaises(ValidationException) as assert_error:
            Customer(name=5)
        self.assertEqual(
            assert_error.exception.args[0], 'The name must be a string')

        with self.assertRaises(ValidationException) as assert_error:
            Customer(name="t" * 256)
        self.assertEqual(
            assert_error.exception.args[0],
            'The name must be less than 255 characters'
        )

    def test_create_with_invalid_cases_for_email_prop(self):
        with self.assertRaises(ValidationException) as assert_error:
            Customer(name='Test', email=5)
        self.assertEqual(
            assert_error.exception.args[0],
            'The email must be a string'
        )

    def test_create_with__invalid_cases_for_is_active_prop(self):
        with self.assertRaises(ValidationException) as assert_error:
            Customer(name='Test', email='test@email.com', is_active=5)
        self.assertEqual(
            assert_error.exception.args[0],
            'The is_active must be a boolean'
        )

    def test_create_with_valid_cases(self):

        try:
            Customer(name='Test', email='test@email.com')
            Customer(name='Test', email='test@email.com', address=None)
            Customer(name='Test', email='test@email.com', address="")
            Customer(name='Test', email='test@email.com', is_active=True)
            Customer(name='Test', email='test@email.com', is_active=False)
        except ValidationException as exception:
            self.fail(f'Some prop is not valid. Error: {exception.args[0]}')

    def test_update_with_invalid_cases_for_name_prop(self):
        customer = Customer(name='Test', email='test@email.com')

        with self.assertRaises(ValidationException) as assert_error:
            customer.update_data(name=None)
        self.assertEqual(
            assert_error.exception.args[0], 'The name is required')

        with self.assertRaises(ValidationException) as assert_error:
            customer.update_data(name='')
        self.assertEqual(
            assert_error.exception.args[0], 'The name is required')

        with self.assertRaises(ValidationException) as assert_error:
            customer.update_data(name=5)
        self.assertEqual(
            assert_error.exception.args[0], 'The name must be a string')

        with self.assertRaises(ValidationException) as assert_error:
            customer.update_data(name="t" * 256, email=None)
        self.assertEqual(
            assert_error.exception.args[0],
            'The name must be less than 255 characters'
        )

        with self.assertRaises(ValidationException) as assert_error:
            customer.update_data(name="t", email=None)
        self.assertEqual(
            assert_error.exception.args[0],
            'The name must be greater than 3 characters'
        )

    def test_update_with_invalid_cases_for_email_prop(self):
        customer = Customer(name='Test', email='test@email.com')

        with self.assertRaises(ValidationException) as assert_error:
            customer.update_data(name='Test', email=5)
        self.assertEqual(
            assert_error.exception.args[0],
            'The email must be a string'
        )

    def test_add_address(self):
        data_address = {
            'street': 'fake street',
            'number': 123,
            'zip': '00000-000',
            'city': 'fake city'
        }
        customer = Customer(name='Test', email='test@email.com')
        customer.add_address(**data_address)
        self.assertEqual(
            customer.address,
            Address(**data_address)
        )                           
