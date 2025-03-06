from typing import Any, Iterator


class ProductsIterator:

    def __init__(self, products_list: list[Any]):
        """Конструктор принимающий список элементов
        и инициализирующий объект класса ProductsIterator"""
        self.products_list = products_list
        self.index = 0

    def __iter__(self) -> Iterator[Any]:
        """Метод, который возвращает итератор"""
        self.index = 0
        return self

    def __next__(self) -> Any:
        """
        Метод, который возвращает следующий элемент последовательности
        """
        if self.index < len(self.products_list):
            product = self.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
