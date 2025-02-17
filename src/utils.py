import json
import os
from json import JSONDecodeError
from typing import Any

from src.category import Category
from src.product import Product


def get_read_json(path: str) -> Any | str:
    """
    Чтение JSON - файла
    :param path:
    :return:
    """

    full_path = os.path.abspath(path)
    try:
        with open(full_path, "r", encoding="utf-8") as file:
            data = json.load(file)

    except JSONDecodeError:
        return "JSONDecodeError: Invalid JSON data."

    except FileNotFoundError:
        return "FileNotFoundError: Файл не найден."

    return data


# print(get_read_json("../data/products.json"))


def create_objects_from_json(data: list[dict]) -> list[Category]:
    """
    Загрузка данных для создания объектов классов
    Product и Category
    :param data:
    :return:
    """

    categories = []
    for category_data in data:
        products = []
        for product_data in category_data["products"]:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            products.append(product)
        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products,
        )
        categories.append(category)
    return categories


# raw_data = get_read_json("../data/products.json")
# raw_data = res
# categories_data = create_objects_from_json(raw_data)
# print(categories_data)
# print(categories_data[0])
# print(categories_data[1].name)
# print(categories_data[1].description)
# print(categories_data[0].products)
