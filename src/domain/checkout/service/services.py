
from src.domain.checkout.entities import Order


class OrderService:
    @staticmethod
    def total(order: Order) -> float:
        return sum(item.price * item.quantity for item in order.items)
