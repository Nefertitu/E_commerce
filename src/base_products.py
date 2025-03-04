from abc import ABC, abstractmethod
from typing import Any


class BaseProducts(ABC):
    """
    Базовый класс для списков продуктов. Определяет общий интерфейс для всех
    списков (категории продуктов списки заказов)
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Конструктор для инициализации экземпляра класса BaseProducts
        :param args:
        :param kwargs:
        """
        super().__init__()

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод, возвращает строковое отображение для класса BaseProduct"""
        pass
