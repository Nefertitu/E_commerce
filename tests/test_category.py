from src.category import Category
from src.product import Product


def test_category(category1: Category, category_count=None) -> None:
    """
    Проверяет, что функция верно выводит имя и описание категории,
    возвращает None, если список продуктов данной категории пуст,
    и верно ведет подсчет количества категорий
    :param category1:
    :return:
    """

    assert category1.name == "Смартфоны"
    assert category1.description == "Карманный ПК с функциями мобильного телефона."
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_without_products(category2: Category) -> None:
    """
    Проверяет, что функция возвращает пустой список, если список продуктов
    данной категории пуст, и верно ведет подсчет количества категорий
    :param category2:
    :return:
    """

    assert category2.name == "Телевизоры"
    assert category2.description == "Приёмник ТВ сигналов изображения и звука."
    assert not category2.products
    assert Category.category_count == 1
    assert Category.product_count == 0
    assert category2.products_in_list == []


def test_products_property(category1: Category):
    """
    Проверяет, что функция возвращает строку со списком продуктов
    в соответствии с установленным форматом
    :param category1:
    :return:
    """

    assert category1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 10 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 15 шт.\n"
    )


def test_add_product(category1: Category) -> None:
    """
    Проверяет работу метода `add_product()`
    :param category1:
    :return:
    """
    assert len(category1.products_in_list) == 2
    category1.add_product(Product("Test", "Test", 1.0, 1))
    assert len(category1.products_in_list) == 3


def test_category_str(category1: Category) -> None:
    assert str(category1) == "Смартфоны, количество продуктов: 25 шт."
