import pytest

from src.category import Category
from src.product import Product

@pytest.mark.parametrize(
    "name, description, category_count, product_count",
    [
        ("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни", 1, 2),
        ("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником", 1, None),
    ],
)
def test_category(
        category1: Category, category2: Category,
        name, description, category_count, product_count) -> None:
    """
    Проверяет, что функция верно выводит имя и описание категории,
    возвращает None, если список продуктов данной категории пуст,
    и верно ведет подсчет количества категорий
    :param category1:
    :param category2:
    :param name:
    :param description:
    :param category_count:
    :param product_count:
    :return:
    """

    assert category1.name, category2.name == name
    assert category1.description, category2.description == description
    assert category1.category_count, category2.category_count == category_count
    assert category1.product_count, category2.product_count == product_count


def test_category_without_products(category2: Category) -> None:
    """
    Проверяет, что функция возвращает None, если список продуктов
    данной категории пуст, и верно ведет подсчет количества категорий
    :param category2:
    :return:
    """

    assert category2.name == "Телевизоры"
    assert (
        category2.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert not category2.products
    assert category2.category_count == 1
    assert category2.products_in_list is None


def test_products_property(category1: Category):
    """
    Проверяет, что функция возвращает строку со списком продуктов
    в соответствии с установленным форматом
    :param category1:
    :return:
    """

    assert category1.products == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 10 шт.\n"
                                  "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 15 шт.\n")


def test_add_product(category1: Category) -> None:
    """
    Проверяет работу метода `add_product()`
    :param category1:
    :return:
    """
    assert len(category1.products_in_list) == 2
    category1.add_product(Product("Test", "Test", 1.0, 1))
    assert len(category1.products_in_list) == 3



