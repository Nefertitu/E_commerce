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
