from typing import Generator, List, Optional

import pytest

from src.category import Category
from src.product import Product
from src.products_iterator import ProductsIterator


@pytest.fixture(autouse=True)
def reset_category_count() -> Generator:
    """
    Обнуляет значение атрибута 'количество категорий'
    :return:
    """
    Category.category_count = 0
    yield
    Category.category_count = 0


@pytest.fixture
def product_() -> Optional[List[Product]]:
    """
    Возвращает экземпляр класса Product
    :return:
    """
    return [
        Product(
            name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=10
        )
    ]


@pytest.fixture
def product1() -> Product:
    """
    Возвращает экземпляр класса Product
    :return:
    """
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=10
    )


@pytest.fixture
def product2() -> Product:
    """
    Возвращает экземпляр класса Product
    :return:
    """
    return Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=15)


@pytest.fixture
def category1(product1: Product, product2: Product) -> Category:
    """
    Возвращает экземпляр класса Category
    :return:
    """
    return Category(
        name="Смартфоны",
        description="Карманный ПК с функциями мобильного телефона.",
        products=[product1, product2],
    )


@pytest.fixture
def products_iterator(category1) -> ProductsIterator:
    products_list = category1.products_in_list
    return ProductsIterator(list(products_list))


@pytest.fixture
def category2() -> Category:
    """
    Возвращает экземпляр класса Category
    :return:
    """
    return Category(
        name="Телевизоры",
        description="Приёмник ТВ сигналов изображения и звука.",
    )


@pytest.fixture
def data_for_test_json() -> str:
    """
    Возвращает строку JSON
    :return:
    """
    return """
[
  {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, серый цвет, 200MP камера",
        "price": "180000",
        "quantity": 5
      }
    ]
  }
]
"""


@pytest.fixture
def data_for_test_create_objects() -> list[dict]:
    return [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        }
    ]
