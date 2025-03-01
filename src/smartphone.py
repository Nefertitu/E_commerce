from src.product import Product


class Smartphone(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: int, color: str) -> None:
        """Конструктор, возвращающий категорию товаров 'Смартфоны'"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.memory = memory
        self.model = model
        self.color = color

    def __add__(self, other):
        """Метод, возвращает сумму произведений цены на количество у двух
        объектов, принадлежащих к классу 'Трава газонная' ('LawnGrass')"""
        if type(self) == Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

