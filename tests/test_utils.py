from unittest.mock import mock_open, patch

import pytest

from src.utils import create_objects_from_json, get_read_json


def test_get_read_json_success(data_for_test_json: str) -> None:
    """Проверяет, что функция читает файл и возвращает список словарей
    с данными о финансовых транзакциях"""

    mocked_open = mock_open(read_data=data_for_test_json)
    with patch("builtins.open", mocked_open):
        result = get_read_json("builtins.open")
        assert result == [
            {
                "name": "Смартфоны",
                "description": "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                "products": [
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, серый цвет, 200MP камера",
                        "price": "180000",
                        "quantity": 5,
                    }
                ],
            }
        ]


def test_get_read_json_empty() -> None:
    """Проверяет, что функция читает файл и возвращает список словарей
    с данными о финансовых транзакциях"""

    mocked_open = mock_open(read_data=None)
    with patch("builtins.open", mocked_open):
        result = get_read_json("builtins.open")
        assert result == "JSONDecodeError: Invalid JSON data."


def test_get_read_json_file_not_found() -> None:
    """Проверяет, что функция читает файл и возвращает список словарей
    с данными о финансовых транзакциях"""

    result = get_read_json("sample.json")
    assert result == "FileNotFoundError: Файл не найден."


def test_create_objects_from_json(data_for_test_create_objects: list[dict]) -> None:
    """
    Тест проверяет, что функция `objects_from_json()` корректно
    создает объекты Product и Category.
    Тестируются следующие сценарии:
    - Создание объекта Product с валидными значениями name, price и category.
    - Проверка типов данных атрибутов Product.
    - Создание объекта Category с валидными значениями name и description.
    - Проверка типа данных атрибута name объекта Category.
    :param data_for_test_create_objects:
    :return:
    """
    result = create_objects_from_json(data_for_test_create_objects)
    print(result)
    assert len(result) == 1
    assert result[0].name == "Телевизоры"
    assert isinstance(result[0].name, str)
    assert isinstance(result[0].description, str)
    assert result[0].description == "Современный телевизор"
    assert len(result[0].products_in_list) == 1


@pytest.mark.parametrize(
    "error_message, expected_out",
    [
        ("JSONDecodeError: Invalid JSON data.", "JSONDecodeError: Invalid JSON data.\n"),
        ("FileNotFoundError: Файл не найден.", "FileNotFoundError: Файл не найден.\n"),
    ],
)
def test_create_objects_from_json_negative(capsys, error_message: str, expected_out: str) -> None:
    """
    Тест проверяет, что функция `objects_from_json()` возвращает
    пустой список и строку с описанием ошибки в случае
    получения некорректных входных данных
    :param capsys:
    :param error_message:
    :param expected_out:
    :return:
    """

    result = create_objects_from_json(error_message)
    captured = capsys.readouterr()
    print(result)
    assert result == []
    assert captured.out == expected_out
