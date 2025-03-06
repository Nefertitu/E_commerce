from src.product import Product


def test_smartphone(lawngrass1) -> None:
    """
    Тест инициализации объекта Smartphone с конкретными атрибутами.
    Проверяет, что объект Smartphone корректно инициализирован с
    ожидаемыми именем, описанием, ценой, количеством, производительностью,
    наименованием модели, объемом встроенной памяти, цветом.
    Проверяет, что класс Smartphone является дочерним по отношению
    к классу Product
    :param lawngrass1:
    :return:
    """

    assert lawngrass1.name == "Газонная трава"
    assert lawngrass1.description == "Элитная трава для газона"
    assert lawngrass1.price == 500.0
    assert lawngrass1.quantity == 20
    assert lawngrass1.country == "Россия"
    assert lawngrass1.germination_period == "7 дней"
    assert lawngrass1.color == "Зеленый"
    assert issubclass(type(lawngrass1), Product) is True


def test_smartphone_add(lawngrass1, lawngrass2) -> None:
    """
    Проверяет, что метод __add__() класса Smartphone корректно
    считает общую стоимость товаров двух наименований продуктов
    :param lawngrass1:
    :param lawngrass2:
    :return:
    """

    assert isinstance(lawngrass1, Product) is True
    assert isinstance(lawngrass2, Product) is True
    assert lawngrass1.price == 500.0
    assert lawngrass2.price == 450.0
    assert lawngrass1.quantity == 20
    assert lawngrass2.quantity == 15
    cost_lawngrass1 = lawngrass1.price * lawngrass1.quantity
    cost_lawngrass2 = lawngrass2.price * lawngrass2.quantity
    total_cost = cost_lawngrass1 + cost_lawngrass2
    assert cost_lawngrass1 + cost_lawngrass2 == 16750.0
    assert cost_lawngrass1 + cost_lawngrass2 == total_cost
