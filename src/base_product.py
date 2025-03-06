from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """
    Базовый класс для продуктов.  Определяет общий интерфейс для всех продуктов
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Инициализирует базовый продукт.  Аргументы зависят от конкретного продукта
        """
        super().__init__()

    @abstractmethod
    def __add__(self, *args: Any, **kwargs: Any) -> None:
        """Оператор сложения для продуктов"""
        pass
