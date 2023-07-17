from dataclasses import asdict, dataclass
from src.domain.shared.value_objects import ValueObject
from src.domain.shared.validators import ValidatorRules as Validator


@dataclass(frozen=True)
class Address(ValueObject):
    street: str
    number: int
    zip: str
    city: str

    def __new__(cls, **kwargs):
        cls.validate(
            street=kwargs.get('street'),
            number=kwargs.get('number'),
            zip=kwargs.get('zip'),
            city=kwargs.get('city'),
        )
        return super(Address, cls).__new__(cls)

    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def validate(cls, street: str, number: int, zip: str, city: str):
        Validator.values(street, 'street').required().string().min_length(3).max_length(100)
        Validator.values(number, 'number').required().integer()
        Validator.values(zip, 'zip').required().string().min_length(8).max_length(9)
        Validator.values(city, 'city').required().string().min_length(3).max_length(100)
