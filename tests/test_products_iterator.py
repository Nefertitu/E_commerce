import pytest

from src.products_iterator import ProductsIterator


def test_products_iterator(products_iterator: ProductsIterator) -> None:
    """
    Проверяет, что корректно осуществляется итерация
    по списку продуктов
    :param products_iterator:
    :return:
    """

    iter(products_iterator)
    assert products_iterator.index == 0
    assert next(products_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(products_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(products_iterator)