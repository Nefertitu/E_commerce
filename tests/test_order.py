import pytest
from src.order import Order


def test_order(order1) -> None:
    """
    Тест инициализации объекта Order с конкретными атрибутами.
    Проверяет, что объект Order корректно инициализирован с
    ожидаемыми именем, описанием, ценой и количеством
    :param order1:
    :return:
    """

    sample_order = order1
    assert sample_order.name == "Samsung Galaxy S23 Ultra"
    assert sample_order.description == "256GB, Серый цвет, 200MP камера"
    assert sample_order.price == 180000.0
    assert sample_order.quantity == 2
    assert sample_order.total_price == 360000.0
    assert isinstance(sample_order, Order) is True


def test_order_error() -> None:
    """Проверяет, что при добавлении заказа с нулевым количеством
    срабатывает `ValueError`"""
    with pytest.raises(ValueError) as excinfo:
        Order("Test order", "Test description", 1, 0)

    assert str(excinfo.value) == "Товар с нулевым количеством не может быть добавлен в заказ.\n"


def test_order_str(order1, capsys) -> None:
    """Проверяет вывод в консоль строкового отображения экземпляра класса `Order`"""
    sample_order = order1
    print(sample_order)
    message = capsys.readouterr()
    assert message.out.strip() == """Наименование товара: Samsung Galaxy S23 Ultra,
            количество купленного товара: 2 шт.,
            итоговая стоимость товара: 360000.0"""


def test_add_order_1(order1):
    """Проверяет, что метод `add_order` корректно добавляет заказ в список заказов"""

    sample_order = order1

    assert sample_order.orders_str() == """
            Наименование товара: Samsung Galaxy S23 Ultra,
            количество купленного товара: 2 шт.,
            итоговая стоимость товара: 360000.0
            """
    assert sample_order.order_count == 1


def test_add_order_2(order1, order2):
    """Проверяет, что метод `add_order` корректно добавляет заказ в список заказов"""

    sample_order = order1
    sample_order.add_order(order2)

    assert sample_order.orders_str() == """
            Наименование товара: Samsung Galaxy S23 Ultra,
            количество купленного товара: 2 шт.,
            итоговая стоимость товара: 360000.0
            \n
            Наименование товара: Iphone 15,
            количество купленного товара: 5 шт.,
            итоговая стоимость товара: 1050000.0
            """
    assert sample_order.order_count == 2