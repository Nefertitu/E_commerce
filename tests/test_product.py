def test_product_init(product1):
    """
    Тест инициализации объекта Product с конкретными атрибутами.
    Проверяет, что объект Product корректно инициализирован с
    ожидаемыми именем, описанием, ценой и количеством
    """

    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 10


def test_product_init_types(product1):
    """
    Проверяет, что объект Product корректно инициализирован с
    ожидаемыми типами данных имени, описания, цены и количества
    """

    assert isinstance(product1.name, str)
    assert isinstance(product1.description, str)
    assert isinstance(product1.price, float)
    assert isinstance(product1.quantity, int)
