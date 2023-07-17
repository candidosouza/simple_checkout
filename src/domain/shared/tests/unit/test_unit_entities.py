import unittest
from abc import ABC
from dataclasses import is_dataclass, dataclass

from src.domain.shared.entities import Entity
from src.domain.shared.value_objects import UniqueEntityId


@dataclass(frozen=True, kw_only=True)
class StubEntity(Entity):
    prop1: str
    prop2: str


class TestEntityUnit(unittest.TestCase):

    def test_if_is_dataclass(self):
        self.assertTrue(is_dataclass(Entity))

    def test_if_is_abstract_class(self):
        self.assertIsInstance(Entity(), ABC)

    def test_set_unique_entity_id_and_props(self):
        entity = StubEntity(prop1='value1', prop2='value2')
        self.assertEqual(entity.prop1, 'value1')
        self.assertEqual(entity.prop2, 'value2')
        self.assertIsInstance(entity.unique_entity_id, UniqueEntityId)
        self.assertEqual(str(entity.unique_entity_id), entity.id)

    def test_accept_a_valid_uuid(self):
        entity = StubEntity(
            unique_entity_id=UniqueEntityId(
                '6d19e09c-7232-4028-93ac-5a6dc32240f2'),
            prop1='value1',
            prop2='value2',
        )
        self.assertEqual(entity.id, '6d19e09c-7232-4028-93ac-5a6dc32240f2')

    def test_invalid_uuid(self):
        with self.assertRaises(Exception) as error:
            StubEntity(
                unique_entity_id=UniqueEntityId(
                    'xpto-e112-45fd-9088-8de0bce03dec'),
                prop1='value1',
                prop2='value2',
            )
        self.assertEqual(
            str(error.exception),
            'ID must be a valid UUID',
        )

    def test_to_dict_method(self):
        entity = StubEntity(
            unique_entity_id=UniqueEntityId(
                'af46842e-027d-4c91-b259-3a3642144ba4'),
            prop1='value1',
            prop2='value2',
        )
        self.assertDictEqual(entity.to_dict(), {
            'id': 'af46842e-027d-4c91-b259-3a3642144ba4',
            'prop1': 'value1',
            'prop2': 'value2'
        })

    def test_set_method(self):
        entity = StubEntity(prop1='value1', prop2='value2',)
        entity._set('prop1', 'changed')
        self.assertEqual(entity.prop1, 'changed')
