

from abc import ABC
from dataclasses import FrozenInstanceError, dataclass, is_dataclass
import unittest
from unittest.mock import patch
import uuid
from src.domain.shared.exceptions import InvalidUuidException

from src.domain.shared.value_objects import UniqueEntityId, ValueObject


@dataclass(frozen=True)
class StubOneProp(ValueObject):
    prop: str


@dataclass(frozen=True)
class StubTwoProp(ValueObject):
    prop1: str
    prop2: str


class TestValueObjectUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(ValueObject))

    def test_if_is_a_abc(self):
        self.assertIsInstance(ValueObject(), ABC)

    def test_init_prop(self):
        value_object = StubOneProp(prop='value')
        self.assertEqual(value_object.prop, 'value')

        value1_object = StubTwoProp(prop1='value1', prop2='value2')
        self.assertEqual(value1_object.prop1, 'value1')
        self.assertEqual(value1_object.prop2, 'value2')

    def test_convert_to_string(self):
        value_object = StubOneProp(prop='value')
        self.assertEqual(value_object.prop, str(value_object))

        value1_object = StubTwoProp(prop1='value1', prop2='value2')
        self.assertEqual(
            '{"prop1": "value1", "prop2": "value2"}', str(value1_object))

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = StubOneProp(prop='value')
            value_object.prop = 'fake'


class TestUniqueEntityIdUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = UniqueEntityId()
            value_object.id = 'fake id'

    def test_throw_exception_when_uuid_is_invalid(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate 
        ) as mock_validate:
            with self.assertRaises(InvalidUuidException) as assert_error:
                UniqueEntityId('fake id')
            mock_validate.assert_called_once()
            self.assertEqual(mock_validate.call_count, 1)
            self.assertEqual(
                assert_error.exception.args[0], 'ID must be a valid UUID')
            
    def test_accept_uui_passed_in_init(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            value_object = UniqueEntityId(
                '8177e159-7ef3-4ee8-ac94-35ef1604905c')
            mock_validate.assert_called_once()
            self.assertEqual(
                value_object.id, '8177e159-7ef3-4ee8-ac94-35ef1604905c')

        uuid_value = uuid.uuid4()
        value_object = UniqueEntityId(uuid_value)
        self.assertEqual(value_object.id, str(uuid_value))

    def test_generate_id_when_no_passed_id_in_init(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            value_object = UniqueEntityId()
            uuid.UUID(value_object.id)
            mock_validate.assert_called_once()
