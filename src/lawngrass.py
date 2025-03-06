from typing import Any

from src.product import Product


class LawnGrass(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Конструктор, возвращающий категорию товаров 'Трава газонная'"""
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __add__(self, other: Any) -> Any:
        """Метод, возвращает сумму произведений цены на количество у двух
        объектов, принадлежащих к классу 'Трава газонная' ('LawnGrass')"""
        if type(self) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
