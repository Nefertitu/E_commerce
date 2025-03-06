from src.base_products import BaseProducts
from src.order import Order


def test_base_products(category1, order1):
    """
    Проверяет, что полученные экземпляры классов `Category` и `Order`
    являются экземплярами базового класса `BaseProducts`
    :param category1:
    :param order1:
    :return:
    """

    category_products = category1
    assert issubclass(type(category_products), BaseProducts) is True
    assert isinstance(category_products, BaseProducts) is True

    order_sample = order1
    assert issubclass(type(order_sample), Order) is True
    assert isinstance(order_sample, BaseProducts) is True
