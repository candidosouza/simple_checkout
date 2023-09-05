from abc import ABC
from enum import Enum
from dataclasses import dataclass
from src.domain.shared.entities import Entity
from src.domain.shared.validators import ValidatorRules


class ProductStatus(Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"


@dataclass(frozen=True, kw_only=True, slots=True)
class Product(Entity):
    name: str
    price: float
    status: ProductStatus

    def __new__(cls, **kwargs):
        cls.validate(
            name=kwargs.get('name'),
            price=kwargs.get('price'),
            status=kwargs.get('status')
        )
        return super(Product, cls).__new__(cls)
    
    def change_price(self, price: float):
        self._set('price', price)
        return self

    @classmethod
    def validate(cls, name: str, price: float, status: ProductStatus):
        ValidatorRules.values(name, 'name').required().string().min_length(3).max_length(255)
        ValidatorRules.values(price, 'price').required().float()

        if status not in ProductStatus._value2member_map_:
            raise ValueError(f"Invalid status value: {status}")
            