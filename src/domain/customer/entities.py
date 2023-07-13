from dataclasses import dataclass
from typing import Optional

from src.domain.shared.entities import Entity


@dataclass(frozen=True, kw_only=True)
class Customer(Entity):
    name: str
    email: str
    address: str
    is_active: Optional[bool] = True

    def activate(self):
        self._set('is_active', True)

    def deactivate(self):
        self._set('is_active', False)

    def validate(self):
        pass