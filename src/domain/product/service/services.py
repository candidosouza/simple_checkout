from typing import List
from src.domain.product.entities import Product


class ProductService:

    @staticmethod
    def increasePrice(products: List[Product], percentage: float) -> None:
        """
        Metodo apenas exemplo, não usar em projeto real, não se deve mudar uma massa de dados
        de uma só vez, pois pode causar problemas de performance e de integridade de dados.
        """
        for product in products:
            price = product.price + (product.price * percentage / 100)
            product.change_price(price)
