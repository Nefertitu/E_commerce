from turtledemo.clock import current_day
from typing import Any, Optional, List

from pydantic import Field


class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    price: float
    quantity: int = Field(
        ..., ge=0, description="Целое число, большее или равное нулю"
    )  # Количество должно быть больше или равно 0

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
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
        self.__price = price
        self.quantity = quantity


    @property
    def price(self) -> float:
        """
        Возвращает значение атрибута цена
        :return:
        """

        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Метод срабатывает при присваивании новой цены
        :param new_price:
        :return:
        """

        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")

        else:
            current_price = self.__price
            if new_price < current_price:
                print("Новая цена товара ниже предыдущей. Снизить цену товара?")
                answer = input("Если да, - введите Y, нет, - N или любой другой символ: ")
                if answer.lower() == "y":
                    self.__price = new_price
                if answer.lower() != "y":
                    print("Цена остается прежней")
                    new_price = current_price

            self.__price = new_price

    @classmethod
    def new_product(cls, new_product: dict, existing_products: Optional[List["Product"]]) -> "Product":
        """
        Возвращает экземпляр класса Product на основе получаемых данных о новом продукте
        :param new_product:
        :return:
        """

        if not all(key in new_product for key in ["name", "description", "price", "quantity"]):
            raise ValueError("Словарь должен содержать ключи 'name', 'description', 'price' и 'quantity'")

        new_product = cls(**new_product)

        for existing_product in existing_products:
            if existing_product.name == new_product.name:
                existing_product.quantity += new_product.quantity
                existing_product.price = new_product.price

                return existing_product

        return new_product
