from typing import List, Optional

from src.base_products import BaseProducts
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


class Category(BaseProducts):
    """Класс для представления категорий продуктов"""

    name: str
    description: str
    # products: Optional[List[Product]] = None

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product] | None] = None) -> None:
        """
        Метод для инициализации экземпляра класса.
        Задаем значения атрибутам экземпляра.
        :param name:
        :param description:
        :param products:
        """
        super().__init__()
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count = len(self.__products)

    def __str__(self) -> str:
        """Метод возвращает строковое отображение для класса Category"""
        amount_products = 0
        for product in self.__products:
            amount_products += product.quantity

        return f"{self.name}, количество продуктов: {amount_products} шт."

    def add_product(self, product: Product) -> None:
        """
        Метод для добавления товаров в категорию список товаров
        """
        if issubclass(Smartphone, Product) or issubclass(LawnGrass, Product):
            if self.__products:
                self.__products.append(product)
                if isinstance(self, Smartphone):
                    Category.product_count += 1
                elif isinstance(self, LawnGrass):
                    Category.product_count += 1

    @property
    def products(self) -> str:  # type: ignore
        """
        Возвращает строку со списком продуктов
        :return:
        """
        products_str = ""
        if self.__products:
            for product in self.__products:
                products_str += str(product)

            return products_str
        return ""

    @property
    def products_in_list(self) -> list | None:
        """
        Возвращает список продуктов
        :return:
        """
        return self.__products


# category = Category("Electronics", "Приборы",[Product("Смартфон", "Средство связи", 10.0, 15)])
# print(category.name)
# print(category.products)
# # print(type(category.products_in_list))
# product_data1 = {'name': 'Laptop', 'description': 'Модель...', 'price': 1000.0, 'quantity': 3}
# product1 = Product.new_product(product_data1, category.products_in_list)
#
# category.add_product(product1)
# print(category.products)
#
# product_data2 = {'name': 'Laptop', 'description': 'Модель...', 'price': 900.0, 'quantity': 2}
# product2 = Product.new_product(product_data2, category.products_in_list)
# print(product2.price)
# category.add_product(product2) # Эта строка не нужна, так как продукт уже добавлен в список
# print(category.products)
#
# product_data3 = {'name': 'Mouse', 'description': 'Модель...', 'price': 20.0, 'quantity': 2}
# product3 = Product.new_product(product_data3, category.products_in_list)
# category.add_product(product3)
#
# print(category.products)
