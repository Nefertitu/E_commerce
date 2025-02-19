from mypy.checkexpr import replace_callable_return_type

from src.product import Product


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
        self.__products = products or None
        self.category_count = 1

        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0



    def add_product(self, product):
        """
        Метод для добавления товаров в категорию список товаров
        :return:
        """

        self.__products.append(Product(name=product.name, description=product.description,price=product.price, quantity=product.quantity))

        Category.product_count += 1



    @property
    def products(self):
        """
        Возвращает строку со списком продуктов
        :return:
        """
        products = ""
        if self.__products:
            for product in self.__products:
                products += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

            return products
        return ""


    @property
    def products_in_list(self):
        """
        Возвращает список продуктов
        :return:
        """
        return self.__products

