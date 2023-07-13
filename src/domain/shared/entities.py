from abc import ABC
from dataclasses import dataclass, field
from .value_objects import UniqueEntityId


@dataclass(frozen=True, slots=True)
class Entity(ABC):

    unique_entity_id: UniqueEntityId = field(
        default_factory=lambda: UniqueEntityId()
    )

    @property
    def id(self):
        return str(self.unique_entity_id)