from src.product import Product


def test_smartphone(smartphone1) -> None:
    """
    Тест инициализации объекта Smartphone с конкретными атрибутами.
    Проверяет, что объект Smartphone корректно инициализирован с
    ожидаемыми именем, описанием, ценой, количеством, производительностью,
    наименованием модели, объемом встроенной памяти, цветом.
    Проверяет, что класс Smartphone является дочерним по отношению
    к классу Product
    :param smartphone1:
    :return:
    """

    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"
    assert issubclass(type(smartphone1), Product) == True


def test_smartphone_add(smartphone1, smartphone2) -> None:
    """
    Проверяет, что метод __add__() класса Smartphone корректно
    считает общую стоимость товаров двух наименований продуктов
    :param smartphone1:
    :param smartphone2:
    :return:
    """

    assert isinstance(smartphone1, Product) == True
    assert isinstance(smartphone2, Product) == True
    assert smartphone1.price == 180000.0
    assert smartphone2.price == 210000.0
    assert smartphone1.quantity == 5
    assert smartphone2.quantity == 8
    cost_smartphone1 = smartphone1.price * smartphone1.quantity
    cost_smartphone2 = smartphone2.price * smartphone2.quantity
    total_cost = cost_smartphone1 + cost_smartphone2
    assert cost_smartphone1 + cost_smartphone2 == 2580000.0
    assert cost_smartphone1 + cost_smartphone2 == total_cost
