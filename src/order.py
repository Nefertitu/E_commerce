from src.base_products import BaseProducts
from src.print_mixin import PrintMixin


class Order(BaseProducts, PrintMixin):

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Конструктор, определяющий экземпляр класса Order"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()

        total_price = self.price * self.quantity
        self.total_price = total_price

    def get_total_price(self) -> float:
        """Возвращает общую стоимость товара"""
        return self.total_price

    def __str__(self) -> str:
        """Метод возвращает строковое отображение для класса Order"""

        return f"""
        Наименование товара: {self.name},
        количество купленного товара: {self.quantity} шт.,
        итоговая стоимость товара: {self.total_price}
        """
