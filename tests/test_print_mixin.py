import pytest
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.mark.parametrize(
    "value, expected_out",
    [
        (
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 10),
            "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 10 шт.",
        ),
        (
            Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"),
            "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        ),
        (
            LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый"),
            "Газонная трава 2, 450.0 руб. Остаток: 15 шт.",
        ),
    ],
)
def test_print_mixin_product(value, expected_out, capsys) -> None:
    """
    Проверяются корректность работы метода печати информации(`__repr__()`)
    класса `PrintMixin`
    :return:
    """
    print(value)
    message = capsys.readouterr()
    assert message.out.strip() == expected_out
