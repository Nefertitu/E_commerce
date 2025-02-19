from pydantic import Field


class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    price: float
    quantity: int = Field(
        ..., ge=0, description="Целое число, большее или равное нулю"
    )  # Количество должно быть больше или равно 0

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
