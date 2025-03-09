from src.exceptions import ZeroQuantityProduct
from src.product import Product


def test_custom_exeption(category2, capsys):
    """Проверяет, что при попытке добавить товар с нулевым количеством,
    срабатывает вызов исключения ZeroQuantityProduct"""
    empty_category = category2
    try:
        empty_category.add_product(Product("Test name", "Test description", 5000.0, 0))
    except ZeroQuantityProduct as e:
        print(f"Ошибка: {e}")
        assert str(e) == "Товар с нулевым количеством не может быть добавлен.\n"
        assert type(e) is ZeroQuantityProduct
    else:
        assert False, "Исключение ZeroQuantityProduct не было вызвано"
    message = capsys.readouterr()
    assert message.out.strip() == "Ошибка: Товар с нулевым количеством не может быть добавлен."

