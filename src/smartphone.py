from typing import Any

from src.product import Product


class Smartphone(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Конструктор, возвращающий категорию товаров 'Смартфоны'"""
        self.efficiency = efficiency
        self.memory = memory
        self.model = model
        self.color = color
        super().__init__(name, description, price, quantity)

    def __add__(self, other: Any) -> Any:
        """Метод, возвращает сумму произведений цены на количество у двух
        объектов, принадлежащих к классу 'Трава газонная' ('LawnGrass')"""
        if type(self) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
