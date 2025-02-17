class Category:
    """Класс для представления категорий продуктов"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """
        Метод для инициализации экземпляра класса.
        Задаем значения атрибутам экземпляра.
        :param name:
        :param description:
        :param products:
        """
        self.name = name
        self.description = description
        self.products = products or None
        self.category_count = 1

        Category.category_count += 1
        Category.product_count += len(products) if products else 0
