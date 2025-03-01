from src.product import Product


class LawnGrass(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: float, color: str) -> None:
        """Конструктор, возвращающий категорию товаров 'Трава газонная'"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Метод, возвращает сумму произведений цены на количество у двух
        объектов, принадлежащих к классу 'Трава газонная' ('LawnGrass')"""
        if type(self) == LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

