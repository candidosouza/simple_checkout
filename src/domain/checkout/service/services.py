
from typing import List
from src.domain.checkout.entities import Order, OrderItem
from src.domain.customer.entities import Customer


class OrderService:
    @staticmethod
    def total(order: Order) -> float:
        return sum(item.price * item.quantity for item in order.items)
    
    @staticmethod
    def place_order(customer: Customer, items: List[OrderItem]) -> Order:
        if not items:
            raise ValueError('Order must have at least one item')
        order = Order(customer_id=customer.id, items=items)
        customer.add_reward_point(int(OrderService.total(order)) / 2)
        return order
        
