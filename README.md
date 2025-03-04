# Проект "E_commerce"

Этот проект представляет собой реализацию основной функциональности 
платформы электронной торговли, или электронной коммерции. 

В настоящее время проект включает четыре основных класса и несколько дочерних классов: 
1. class PrintMixin.
2. class BaseProduct(ABC):
2.1. class Product(BaseProduct, PrintMixin):
2.1.1. class Smartphone(Product);
2.1.2. class LawnGrass(Product).
3. class BaseProducts(ABC):
3.1. class Category(BaseProducts);
3.2. class Order(BaseProducts, PrintMixin).
4. ProductIterator.

 
Цель проекта состоит в том, чтобы создать основу, которую в будущем 
можно расширить различными интерфейсами, такими как веб-сайты или боты 
в Telegram.

# Структура проекта:
```
E_commerce
│   .venv
│
├───.coverage
│   .flake8
│   .gitignore
│   LICENSE.txt
│   main.py
│   poetry.lock
│   pyproject.toml
│   README.md
│
├───data
│       products.json
│
├───htmlcov
│       index.html
│
├───src
│   │   __init__.py
│   │   base_product.py
│   │   base_products.py
│   │   category.py
│   │   lawngrass.py
│   │   order.py
│   │   print_mixin.py
│   │   product.py
│   │   products_iterator.py
│   │   smartphone.py
│   │   utils.py
│
└───tests
    │   __init__.py
    │   conftest.py
    │   test_base_product.py
    │   test_base_products.py
    │   test_category.py
    │   test_lawngrass.py
    │   test_order.py
    │   test_print_mixin.py
    │   test_product.py
    │   test_products_iterator.py
    │   test_utils.py

```
# Каталоги и файлы

- `/data`: Содержит образец данных в формате JSON (`products.json`), 
используемых для загрузки категорий и продуктов.
- `/src`:
  1. `base_product.py`: Определяет абстрактный класс `class BaseProduct(ABC)`.
  Содержит следующие методы:
  - `__init__()`- метод для инициализации экземпляра абстрактного класса BaseProduct;
  - `@abstractmethod __add__()` - абстрактный метод, оператор сложения для продуктов.
  2. `base_products.py`: Определяет абстрактный класс `class BaseProducts(ABC)`.
  Содержит следующие методы:
  - `__init__()`- метод для инициализации экземпляра абстрактного класса BaseProducts;
  - `@abstractmethod __str__()` - абстрактный метод, возвращает строковое 
  отображение для класса BaseProduct.
  3. `category.py`: Определяет класс `class Category`.
  Содержит следующие методы:
  - `__init__()`- метод для инициализации экземпляра класса Category;
  - `__str__()` - метод возвращает строковое отображение для класса Category;
  - `add_product()` - метод для добавления товаров в категорию список товаров;
  - `@property products()` - геттер (возвращает строку со списком продуктов);
  - `@property products_in_list()` - геттер (возвращает список продуктов).
  2. `product.py`: Определяет `class Product`.
  Содержит следующие методы:
  - `__init__()` - метод для инициализации экземпляра класса Product;
  - `__str__()` - возвращает строковое представление продукта;
  - `__add__()` - метод возвращает сумму произведений цены на количество 
  у двух объектов (общую стоимость товаров двух наименований);
  - `@classmethod new_product()` - классметод (возвращает экземпляр класса Product 
  на основе получаемых данных о новом продукте);
  - `@property price()` - геттер (возвращает значение атрибута цена);
  - `@price.setter price()` - сеттер (метод срабатывает при присваивании новой цены).
  3. `product_iterator.py`: Определяет класс `class ProductIterator`.
  Содержит следующие методы:
  - `__init__()` - метод для инициализации экземпляра класса ProductIterator;
  - `__iter__()` - метод, который возвращает итератор;
  - `__next__()` - метод, который возвращает следующий элемент последовательности. 
  4. `smartphone.py`: Определяет класс `class Smartphone`.
  Содержит следующие методы:
  - `__init__()` - метод для инициализации экземпляра класса "Смартфоны" (Smartphone);
  - `__add__()` - метод возвращает сумму произведений цены на количество.
  5. `lawngrass.py`: Определяет класс `class LawnGrass`.
  Содержит следующие методы:
  - `__init__()` - метод для инициализации экземпляра класса "Зеленая трава" (LawnGrass);
  - `__add__()` - метод возвращает сумму произведений цены на количество.
  6. `order.py` : Определяет класс `class Order`.
  Содержит следующие методы:
  - `__init__()` - метод для инициализации экземпляра класса "Заказ" (Order);
  - `get_total_price()` - возвращает общую стоимость товара;
  - `__str__()` - возвращает строковое отображение для класса Order.
  7. `print_mixin.py`: Определяет класс `class PrintMixin`.
  Содержит следующие методы:
  - `__init__()` - метод для инициализации экземпляра класса PrintMixin;
  - `__repr__()` - dозвращает строковое представление объекта PrintMixin 
  для печати в консоль.
  8. `utils.py`: Вспомогательные функции для чтения и обработки данных JSON.
  Содержит следующие функции:
  - `get_read_json()` - чтение JSON-файла;
  - `create_objects_from_json()` - загрузка данных для создания объектов 
классов Product и Category.
  
- `/tests`:
  1. `conftest.py`: Файл конфигурации для фикстур pytest.
  2. `test_category.py`: Тесты для модуля `category.py`.
  3. `test_product.py`: Тесты для модуля `product.py`.
  4. `test_utils.py`: Тесты для модуля `utils.py`.
  5. `test_products_iterator.py`: Тесты ля модуля `products_iterator.py`.
  6. `test_smartphone.py`: Тесты для модуля `smartphone.py`.
  7. `test_lawngross.py`: Тесты для модуля `lawngross.py`.
  8. `test_base_product.py`: Тесты для модуля `base_product.py`.
  9. `test_base_products.py`: Тесты для модуля `base_products.py`.
  10. `test_order.py`: Тесты для модуля `order.py`.
  11. `test_print_mixin.py`: Тесты для модуля `print_mixin.py`.
  
# Основные файлы

- `.coverage`: Отчёт о покрытии кода, созданный инструментами покрытия.
- `.gitignore`: Указывает файлы и директории, которые следует 
игнорировать при коммитах в Git.
- `main.py`: Точка входа для запуска приложения.
- `poetry.lock`: Файл блокировки зависимостей для управления 
зависимостями с помощью Poetry.
- `pyproject.toml`: Конфигурационный файл для Poetry.
- `.flake8`: Конфигурационный файл для линтера Flake8

# Установка

1. Клонируйте репозиторий:
```
git clone git@github.com:Nefertitu/E-commerce.git
```
2. Установите зависимости:
```
poetry install
```


# Использование

Чтобы запустить приложение, выполните следующую команду из корневого 
каталога:

```
python main.py
```

# Тестирование

Проект включает юнит-тесты pytest.

Для запуска тестов выполните команду:
- при активированном виртуальном окружении:
```
pytest --cov
 
```
- через poetry:
```
poetry run pytest --cov
```
*Текущие результаты тестирования:*
```
----------- coverage: platform win32, python 3.13.1-final-0 -----------
Name                              Stmts   Miss  Cover
-----------------------------------------------------
src\__init__.py                       0      0   100%
src\base_product.py                   8      1    88%
src\base_products.py                  7      1    86%
src\category.py                      41      2    95%
src\lawngrass.py                     12      3    75%
src\order.py                         15      2    87%
src\print_mixin.py                    5      0   100%
src\product.py                       46     10    78%
src\products_iterator.py             14      0   100%
src\smartphone.py                    14      3    79%
src\utils.py                         27      0   100%
tests\__init__.py                     0      0   100%
tests\conftest.py                    53      0   100%
tests\test_base_product.py           11      0   100%
tests\test_base_products.py          10      0   100%
tests\test_category.py               22      0   100%
tests\test_lawngrass.py              22      0   100%
tests\test_order.py                   9      0   100%
tests\test_print_mixin.py            11      0   100%
tests\test_product.py                59      3    95%
tests\test_products_iterator.py       9      0   100%
tests\test_smartphone.py             23      0   100%
tests\test_utils.py                  32      0   100%
-----------------------------------------------------
TOTAL                               450     25    94%


======================= 31 passed in 0.84s ==========================

```

# Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE.txt).