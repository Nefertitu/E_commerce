from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys) -> None:
    """
    Проверяются корректность работы метода печати информации(`__repr__()`)
    класса `PrintMixin`
    :return:
    """
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 10)
    message = capsys.readouterr()
    print(message)
    # assert message.out.strip() == "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 10)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    # assert message.out.strip() == "Smartphone('Iphone 15', '512GB, Gray space', 210000.0, 8)"

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    message = capsys.readouterr()
    # assert message.out.strip() == "LawnGrass('Газонная трава 2', 'Выносливая трава', 450.0, 15)"
