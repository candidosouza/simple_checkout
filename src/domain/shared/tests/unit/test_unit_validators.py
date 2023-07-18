import unittest
from dataclasses import dataclass, is_dataclass
from src.domain.shared.exceptions import ValidationException
from src.domain.shared.validators import ValidatorRules

class TestValidatorRulesUnit(unittest.TestCase):
    
    def test_is_dataclass(self):
        self.assertTrue(is_dataclass(ValidatorRules))

    def test_values_method(self):
        validator = ValidatorRules.values('some value', 'prop')
        self.assertIsInstance(validator, ValidatorRules)
        self.assertEqual(validator.value, 'some value')
        self.assertEqual(validator.prop, 'prop')

    def test_required_rules(self):

        invalid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': '', 'prop': 'prop'},
        ]
        for data in invalid_data:
            message = f'value: {data["value"]}, prop: {data["prop"]}'
            with self.assertRaises(ValidationException, msg=message) as error:
                self.assertIsInstance(
                    ValidatorRules.values(data['value'], data['prop']).required(),
                    ValidatorRules
                )
            self.assertEqual(
                'The prop is required',
                str(error.exception.args[0]),
            )

        valid_data = [
            {'value': 'Some value', 'prop': 'prop'},
            {'value': 5, 'prop': 'prop'},
            {'value': False, 'prop': 'prop'},
        ]
        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(data['value'], data['prop']).required(),
                ValidatorRules
            )

    def test_string_rules(self):
        invalid_data = [
            {'value': 5, 'prop': 'prop'},
            {'value': True, 'prop': 'prop'},
            {'value': {}, 'prop': 'prop'},
        ]
        for data in invalid_data:
            message = f'value: {data["value"]}, prop: {data["prop"]}'
            with self.assertRaises(ValidationException, msg=message) as assert_rules:
                ValidatorRules.values(
                    data['value'], data['prop']
                ).string()
            self.assertEqual(
                f'The {data["prop"]} must be a string',
                assert_rules.exception.args[0],
            )

        valid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': "", 'prop': 'prop'},
            {'value': "some value", 'prop': 'prop'},
        ]
        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(
                    data['value'], data['prop']
                ).string(),
                ValidatorRules
            )

    def test_integer_rules(self):
        invalid_data = [
            {'value': 'string', 'prop': 'prop'},
            {'value': 1.3, 'prop': 'prop'},
        ]
        for data in invalid_data:
            message = f'value: {data["value"]}, prop: {data["prop"]}'
            with self.assertRaises(ValidationException, msg=message) as assert_rules:
                ValidatorRules.values(
                    data['value'], data['prop']
                ).integer()
            self.assertEqual(
                f'The {data["prop"]} must be a int',
                assert_rules.exception.args[0],
            )

        valid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': True, 'prop': 'prop'},
            {'value': 1234567, 'prop': 'prop'},
        ]
        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(
                    data['value'], data['prop']
                ).integer(),
                ValidatorRules
            )

    def test_float_rules(self):
        invalid_data = [
            {'value': 'string', 'prop': 'prop'},
            {'value': True, 'prop': 'prop'},
        ]
        for data in invalid_data:
            message = f'value: {data["value"]}, prop: {data["prop"]}'
            with self.assertRaises(ValidationException, msg=message) as assert_rules:
                ValidatorRules.values(
                    data['value'], data['prop']
                ).float()
            self.assertEqual(
                f'The {data["prop"]} must be a float',
                assert_rules.exception.args[0],
            )

        valid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': 1.3, 'prop': 'prop'},
            {'value': 12345.67, 'prop': 'prop'},
        ]
        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(
                    data['value'], data['prop']
                ).float(),
                ValidatorRules
            )

    def test_max_length_rules(self):
        invalid_data = [
            {'value': "x" * 5, 'prop': 'prop'},
        ]
        for data in invalid_data:
            message = f'value: {data["value"]}, prop: {data["prop"]}'
            with self.assertRaises(ValidationException, msg=message) as assert_rules:
                ValidatorRules.values(  # pylint: disable=expression-not-assigned
                    data['value'], data['prop']
                ).max_length(4)
            self.assertEqual(
                f'The {data["prop"]} must be less than 4 characters',
                assert_rules.exception.args[0],
            )

        valid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': "x" * 5, 'prop': 'prop'},
        ]
        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(
                    data['value'], data['prop']
                ).max_length(5),
                ValidatorRules
            )

    def test_min_length_rules(self):
        invalid_data = [
            {'value': "x", 'prop': 'prop'},
        ]
        for data in invalid_data:
            message = f'value: {data["value"]}, prop: {data["prop"]}'
            with self.assertRaises(ValidationException, msg=message) as assert_rules:

                ValidatorRules.values(  # pylint: disable=expression-not-assigned
                    data['value'], data['prop']
                ).min_length(3)
            self.assertEqual(
                f'The {data["prop"]} must be greater than 3 characters',
                assert_rules.exception.args[0],
            )

        valid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': "x" * 5, 'prop': 'prop'},
        ]
        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(
                    data['value'], data['prop']
                ).min_length(4),
                ValidatorRules
            )

    def test_bollean_rules(self):
        invalid_data = [
            {'value': "x", 'prop': 'prop'},
            {'value': "", 'prop': 'prop'},
            {'value': 5, 'prop': 'prop'},
            {'value': {}, 'prop': 'prop'},
        ]
        for data in invalid_data:
            message = f'value: {data["value"]}, prop: {data["prop"]}'
            with self.assertRaises(ValidationException, msg=message) as assert_rules:
                ValidatorRules.values(  # pylint: disable=expression-not-assigned
                    data['value'], data['prop']
                ).boolean()
            self.assertEqual(
                f'The {data["prop"]} must be a boolean',
                assert_rules.exception.args[0],
            )

        valid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': True, 'prop': 'prop'},
            {'value': False, 'prop': 'prop'},
        ]
        for data in valid_data:
            self.assertIsInstance(
                ValidatorRules.values(
                    data['value'], data['prop']
                ).boolean(),
                ValidatorRules
            )

    def test_throw_a_validation_exception_when_combine_two_or_more_rules(self):
        with self.assertRaises(ValidationException) as assert_rules:
            ValidatorRules.values(  # pylint: disable=expression-not-assigned
                None, 'prop'
            ).required().string().max_length(5)
        self.assertEqual(
            'The prop is required',
            assert_rules.exception.args[0],
        )

        with self.assertRaises(ValidationException) as assert_rules:
            ValidatorRules.values(  # pylint: disable=expression-not-assigned
                5, 'prop'
            ).required().string().max_length(5)
        self.assertEqual(
            'The prop must be a string',
            assert_rules.exception.args[0],
        )

        with self.assertRaises(ValidationException) as assert_rules:
            ValidatorRules.values(  # pylint: disable=expression-not-assigned
                "x" * 6, 'prop'
            ).required().string().max_length(5)
        self.assertEqual(
            'The prop must be less than 5 characters',
            assert_rules.exception.args[0],
        )

        with self.assertRaises(ValidationException) as assert_rules:
            ValidatorRules.values(
                "x" * 4, 'prop'
            ).required().string().min_length(5)
        self.assertEqual(
            'The prop must be greater than 5 characters',
            assert_rules.exception.args[0],
        )

        with self.assertRaises(ValidationException) as assert_rules:
            ValidatorRules.values(
                None, 'prop'
            ).required().boolean()
        self.assertEqual(
            'The prop is required',
            assert_rules.exception.args[0],
        )

        with self.assertRaises(ValidationException) as assert_rules:
            ValidatorRules.values(
                5, 'prop'
            ).required().boolean()
        self.assertEqual(
            'The prop must be a boolean',
            assert_rules.exception.args[0],
        )

    def test_valid_cases_for_combination_between_rules(self):
        ValidatorRules.values('test', 'prop').required().string()
        ValidatorRules.values(
            'x' * 5, 'prop').required().string().max_length(5)

        ValidatorRules.values(True, 'prop').required().boolean()
        ValidatorRules.values(False, 'prop').required().boolean()
