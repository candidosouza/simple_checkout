import unittest
from unittest.mock import patch
from dataclasses import FrozenInstanceError, is_dataclass
from src.domain.product.entities import Product
from src.domain.shared.exceptions import ValidationException


class TestProductUnit(unittest.TestCase):

    def test_if_is_dataclass(self):
        self.assertTrue(is_dataclass(Product))

    def test_constructor(self):
        with patch.object(Product, 'validate') as mock_validate:
            product = Product(
                name='Product 1',
                price=10.0,
                status='enabled'
            )
            mock_validate.assert_called_once()
            self.assertEqual(product.name, 'Product 1')
            self.assertEqual(product.price, 10.0)
            self.assertEqual(product.id, product.unique_entity_id.id)

            product = Product(
                name='Product 2',
                price=10.0,
                status='enabled'
            )
            self.assertEqual(product.name, 'Product 2')
            self.assertEqual(product.price, 10.0)
            self.assertEqual(product.id, product.unique_entity_id.id)

    def test_is_immutable(self):
        with patch.object(Product, 'validate'):
            with self.assertRaises(FrozenInstanceError):
                value_object = Product(name='test', price=10.0, status='enabled')
                value_object.name = 'fake id'

    def test_throw_exception_when_name_is_invalid(self):
        with self.assertRaises(ValidationException) as assert_error:
            Product(name='', price='10.0')
        self.assertEqual(str(assert_error.exception), "The name is required")

        with self.assertRaises(ValidationException) as assert_error:
            Product(name=77, price='10.0')
        self.assertEqual(str(assert_error.exception), "The name must be a string")

        with self.assertRaises(ValidationException) as assert_error:
            Product(name='xp', price='10.0')
        self.assertEqual(str(assert_error.exception), "The name must be greater than 3 characters")

        with self.assertRaises(ValidationException) as assert_error:
            Product(name='xpto' * 255, price='10.0')
        self.assertEqual(str(assert_error.exception), "The name must be less than 255 characters")

    def test_throw_exception_when_price_is_invalid(self):
        with self.assertRaises(ValidationException) as assert_error:
            Product(name='Product 1', price='')
        self.assertEqual(str(assert_error.exception), "The price is required")
    
        with self.assertRaises(ValidationException) as assert_error:
            Product(name='Product 1', price='100')
        self.assertEqual(str(assert_error.exception), "The price must be a float")

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            Product(
                name='Product 1',
                price=10.0,
                status='enableddddd'
            )
