from abc import ABC
from dataclasses import asdict, dataclass, field
from typing import Any
from .value_objects import UniqueEntityId


@dataclass(frozen=True, slots=True)
class Entity(ABC):

    unique_entity_id: UniqueEntityId = field(
        default_factory=lambda: UniqueEntityId()
    )

    @property
    def id(self):
        return str(self.unique_entity_id)
    
    def _set(self, name: str, value: Any):
        """Set a value to a field of the entity."""
        object.__setattr__(self, name, value)
        return self
    
    def to_dict(self):
        entity_dict = asdict(self)
        entity_dict.pop('unique_entity_id')
        entity_dict['id'] = self.id
        return entity_dict