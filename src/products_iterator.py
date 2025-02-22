class ProductsIterator:

    def __init__(self, products_list: list):
        """конструктор принимающий список элементов
        и инициализирующий объект класса ProductsIterator"""
        self.products_list = products_list
        self.index = 0

    def __iter__(self):
        """метод, который возвращает итератор"""
        self.index = 0
        return self

    def __next__(self):
        """
        метод, который возвращает следующий элемент последовательности
        """
        if self.index < len(self.products_list):
            product = self.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration