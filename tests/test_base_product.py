from src.base_product import BaseProduct
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_base_product() -> None:
    """
    Проверяет, что полученные экземпляры классов `Product`, `Smartphone`,
    ` LawnGrass` являются экземплярами базового класса `BaseProduct`
    :return:
    """
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 10)
    assert issubclass(type(product), BaseProduct)

    smartphone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    assert issubclass(type(smartphone), BaseProduct)

    lawngrass = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    assert issubclass(type(lawngrass), BaseProduct)
