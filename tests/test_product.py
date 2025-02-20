from unittest.mock import patch

import pytest

from src.product import Product


def test_product_init(product1: Product) -> None:
    """
    Тест инициализации объекта Product с конкретными атрибутами.
    Проверяет, что объект Product корректно инициализирован с
    ожидаемыми именем, описанием, ценой и количеством
    """

    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 10


def test_product_init_types(product1: Product) -> None:
    """
    Проверяет, что объект Product корректно инициализирован с
    ожидаемыми типами данных имени, описания, цены и количества
    """

    assert isinstance(product1.name, str)
    assert isinstance(product1.description, str)
    assert isinstance(product1.price, float)
    assert isinstance(product1.quantity, int)


def test_new_product_classmethod() -> None:
    """Проверяет, что метод корректно создает новый экземпляр
    продукта класса Product"""

    new_product = Product.new_product({"name": "Test", "description": "Test", "price": 1.0, "quantity": 1})
    assert new_product.name == "Test"
    assert new_product.description == "Test"
    assert new_product.price == 1.0
    assert new_product.quantity == 1


def test_add_product_value_error(capsys) -> None:
    """
    Проверяет работу метода `add_product()` в случае,
    когда при создании экземпляра продукта класса Product
    были переданы не все ключи (метод вызывает ValueError)
    :param capsys:
    :return:
    """

    with pytest.raises(ValueError):
        new_product = Product.new_product({"name": "Test", "description": "Test", "price": 0})
        print(new_product)
        captured = capsys.readouterr()
        assert captured.out == "Словарь должен содержать ключи 'name', 'description', 'price' и 'quantity'"


def test_price_setter(product1) -> None:
    """
    Проверяет что цена поменяется на новую, если она выше
    старой цены
    :param product1:
    :return:
    """
    product = product1
    old_price = product1.price
    product.price = 190000.0
    assert product.price == 190000.0
    assert product.price > old_price


@pytest.mark.parametrize(
    "new_price, input_response, expected_price",
    [
        (120000.0, "Y", 120000.0),
        (120000.0, "N", 180000.0),
    ],
)
@patch("builtins.input", side_effect="input_response")
def test_price_setter_lower_price(product1, new_price, input_response, expected_price, capsys) -> None:
    """
    Проверяет, что цена меняется на более низкую,
    в случае положительного ответа пользователя и остается прежней
    в случае иного ответа
    :param product1:
    :param new_price:
    :param input_response:
    :param expected_price:
    :param capsys:
    :return:
    """
    product1.price = new_price
    product1.price = expected_price
    print(product1.price)
    captured = capsys.readouterr()
    assert product1.price == expected_price
    assert captured.out == f"{expected_price}\n"


@pytest.mark.parametrize(
    "new_price, expected_price",
    [
        (0.0, 180000.0),
        (-120000.0, 180000.0),
    ],
)
def test_price_setter_negative(product1, new_price, expected_price, capsys) -> None:
    """
    Проверяет, что цена не может быть отрицательной или
    быть равной нулю
    :param product1:
    :return:
    """

    product1.price = new_price
    captured = capsys.readouterr()
    print(product1.price)
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert product1.price == expected_price
