from dataclasses import dataclass, field
from typing import List
import uuid
from src.domain.shared.entities import Entity
from src.domain.shared.validators import ValidatorRules


@dataclass(frozen=True, kw_only=True, slots=True)
class Order(Entity):
    customer_id: str
    items: List['OrderItem']


@dataclass(frozen=True, kw_only=True, slots=True)
class OrderItem(Entity):
    name: str
    product_id: str
    quantity: int
    price: float

    def __new__(cls, **kwargs):
        cls.validate(
            name=kwargs.get('name'),
            product_id=kwargs.get('product_id'),
            quantity=kwargs.get('quantity'),
            price=kwargs.get('price'),
        )
        return super(OrderItem, cls).__new__(cls)

    @classmethod
    def validate(cls, name: str, product_id: str, quantity: int, price: float):
        ValidatorRules.values(name, 'name').required().string().min_length(3).max_length(255)
        ValidatorRules.values(product_id, 'product_id').required().string().min_length(3).max_length(255)
        ValidatorRules.values(quantity, 'quantity').required().integer()
        ValidatorRules.values(price, 'price').required()

    def total(self):
        return self.quantity * self.price
