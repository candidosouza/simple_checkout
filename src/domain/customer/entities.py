from dataclasses import dataclass
from typing import Optional
from src.domain.customer.value_object import Address

from src.domain.shared.entities import Entity
from src.domain.shared.validators import ValidatorRules as Validator


@dataclass(frozen=True, kw_only=True, slots=True)
class Customer(Entity):
    name: str
    email: str
    address: Optional[Address] = None
    is_active: Optional[bool] = True

    def __new__(cls, **kwargs):
        cls.validate(
            name=kwargs.get('name'),
            email=kwargs.get('email'),
            is_active=kwargs.get('is_active'),
        )
        return super(Customer, cls).__new__(cls)
    
    def update_data(self, **kwargs):
        self.validate(
            name=kwargs.get('name'),
            email=kwargs.get('email'),
            is_active=kwargs.get('is_active'),
        )
        self._set('name', kwargs.get('name'))
        self._set('email', kwargs.get('email'))
        self._set('is_active', kwargs.get('is_active'))

    def add_address(self, **kwargs):
        self._set('address', Address(**kwargs))

    def activate(self):
        self._set('is_active', True)

    def deactivate(self):
        self._set('is_active', False)

    @classmethod
    def validate(cls, name: str, email: str, is_active: bool = None):
        Validator.values(name, 'name').required().string().min_length(3).max_length(255)
        Validator.values(email, 'email').required().string().min_length(5).max_length(255)
        Validator.values(is_active, 'is_active').boolean()
