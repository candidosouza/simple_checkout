
from dataclasses import FrozenInstanceError, is_dataclass
import unittest
from unittest.mock import patch

from src.domain.customer.value_object import Address
from src.domain.shared.exceptions import ValidationException


class TestCustomerValueObjectUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Address))

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = Address(
                street='fake street',
                number=123,
                zip='00000-000',
                city='fake city'
            )
            value_object.street = 'fake street'
            value_object.number = 123
            value_object.zip = '00000-000'
            value_object.city = 'fake city'

    def test_validate(self):
        with patch.object(Address, 'validate') as mock_validate:
            data = {
                'street': 'fake street',
                'number': 123,
                'zip': '00000-000',
                'city': 'fake city'
            }
            Address(**data)
            mock_validate.assert_called_once()

    def test_throw_exception_when_street_is_invalid(self):
        invalid_data = [
            {
                'street': True,
                'number': 123,
                'zip': '00000-000',
                'city': 'fake city'
            },
            {
                'street': False,
                'number': 123,
                'zip': '00000-000',
                'city': 'fake city'
            },
            {
                'street': 777,
                'number': 123,
                'zip': '00000-000',
                'city': 'fake city'
            },
        ]
        for data in invalid_data:
            with self.assertRaises(ValidationException) as assert_error:
                Address(**data)
            self.assertEqual(assert_error.exception.args[0], 'The street must be a string')

    def test_throw_exception_when_number_is_invalid(self):
        invalid_data = [
            {
                'street': 'fake street',
                'number': '123',
                'zip': '00000-000',
                'city': 'fake city'
            },
            {
                'street': 'fake street',
                'number': 1.23,
                'zip': '00000-000',
                'city': 'fake city'
            },
            {
                'street': 'fake street',
                'number': 'True',
                'zip': '00000-000',
                'city': 'fake city'
            },
        ]
        for data in invalid_data:
            with self.assertRaises(ValidationException) as assert_error:
                Address(**data)
            self.assertEqual(assert_error.exception.args[0], 'The number must be a int')

    def test_throw_exception_when_zip_is_invalid(self):
        invalid_data = [
            {
                'street': 'fake street',
                'number': 123,
                'zip': 00000000,
                'city': 'fake city'
            },
            {
                'street': 'fake street',
                'number': 123,
                'zip': 00000-000,
                'city': 'fake city'
            },
            {
                'street': 'fake street',
                'number': 123,
                'zip': 00000.000,
                'city': 'fake city'
            },
        ]
        for data in invalid_data:
            with self.assertRaises(ValidationException) as assert_error:
                Address(**data)
            self.assertEqual(assert_error.exception.args[0], 'The zip must be a string')

    def test_throw_exception_when_city_is_invalid(self):
        invalid_data = [
            {
                'street': 'fake street',
                'number': 123,
                'zip': '00000-000',
                'city': 123
            },
            {
                'street': 'fake street',
                'number': 123,
                'zip': '00000-000',
                'city': True
            },
            {
                'street': 'fake street',
                'number': 123,
                'zip': '00000-000',
                'city': False
            },
        ]
        for data in invalid_data:
            with self.assertRaises(ValidationException) as assert_error:
                Address(**data)
            self.assertEqual(assert_error.exception.args[0], 'The city must be a string')

    def test_to_dict(self):
        data = {
            'street': 'fake street',
            'number': 123,
            'zip': '00000-000',
            'city': 'fake city'
        }
        value_object = Address(**data)
        self.assertDictEqual(value_object.to_dict(), data)
        
