from typing import Any, Optional, List

from src.base_products import BaseProducts
from src.print_mixin import PrintMixin
from src.exceptions import ZeroQuantityProduct


class Order(BaseProducts, PrintMixin):
    """Класс для представления заказов"""

    order_count = 0

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Конструктор, определяющий экземпляр класса Order"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        if self.quantity <= 0:
            raise ZeroQuantityProduct("Товар с нулевым количеством не может быть добавлен в заказ.\n")
        self.total_price = self.price * self.quantity
        self.orders = []
        super().__init__()

        Order.order_count = len(self.orders)


    def get_total_price(self) -> float:
        """Возвращает общую стоимость товара"""
        return self.total_price


    def __str__(self) -> str:
        """Метод возвращает строковое отображение для класса Order"""
        Order.order_count += 1
        return f"""
            Наименование товара: {self.name},
            количество купленного товара: {self.quantity} шт.,
            итоговая стоимость товара: {self.total_price}
            """


    def add_order(self, order: "Order"):
        """Метод для добавления заказов в список заказов"""
        if self.orders == []:
            self.orders.append(self)
            # Order.order_count += 1
        if isinstance(order, Order):
            try:
               if order.quantity <= 0:
                   raise ValueError("Нельзя добавить в заказ товар с нулевым количеством.")
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.orders.append(order)
                # Order.order_count += 1
            finally:
                print("Обработка добавления заказа завершена.")
        else:
            print("Товар не соответствует параметрам экземпляра класса `Order`")


    def orders_str(self) -> str:
        """Метод для представления строкового отображения списка заказов"""
        if self.orders != []:
            return "\n".join(str(order) for order in self.orders)
        return f"{str(self)}"


    @classmethod
    def new_order(cls, new_order: dict, existing_orders: Optional[List["Order"]]) -> "Order":
        """
        Возвращает экземпляр класса Order на основе получаемых данных о новом продукте
        :param new_order:
        :return:
        """

        if not all(key in new_order for key in ["name", "description", "price", "quantity"]):
            raise ValueError("Словарь должен содержать ключи 'name', 'description', 'price' и 'quantity'")

        order = cls(**new_order)

        for existing_order in existing_orders or []:
            if existing_order.name == order.name:
                existing_order.quantity += order.quantity
                existing_order.price = order.price

                return existing_order

        return order
