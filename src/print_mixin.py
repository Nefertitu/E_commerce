class PrintMixin:
    """
    Mixin, добавляющий функциональность печати информации о продукте
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализирует PrintMixin"""
        self.name = name
        self. description = description
        self.price = price
        self.quantity = quantity
        print(repr(self))

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта PrintMixin
        для печати в консоль"""
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"
