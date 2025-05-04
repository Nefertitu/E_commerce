from typing import Any


class ZeroQuantityProduct(ValueError):
    """Класс для исключений"""

    def __init__(self, message: Any = None):
        """Конструктор для определения экземпляра класса `ZeroQuantityProduct`"""
        super().__init__(message)
