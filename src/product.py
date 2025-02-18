from pydantic import BaseModel, Field
from decimal import Decimal


class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    price: Decimal = Field(..., gt=0)  # Цена должна быть больше, чем 0
    quantity: int = Field(..., ge=0)  # Количество должно быть больше или равно 0

    def __init__(self, name, description, price, quantity):
        """
        Метод для инициализации экземпляра класса.
        Задаем значения атрибутам экземпляра.
        :param name:
        :param description:
        :param price:
        :param quantity:
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
