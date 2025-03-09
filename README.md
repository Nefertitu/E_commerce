# Проект "E_commerce"

Этот проект представляет собой реализацию основной функциональности 
платформы электронной торговли, или электронной коммерции. 

В настоящее время проект включает пять основных классов и несколько классов - наследников: 
1. class PrintMixin.
2. class BaseProduct(ABC):
2.1. class Product(BaseProduct, PrintMixin):
2.1.1. class Smartphone(Product);
2.1.2. class LawnGrass(Product).
3. class BaseProducts(ABC):
3.1. class Category(BaseProducts);
3.2. class Order(BaseProducts, PrintMixin).
4. class ProductIterator.
5. class ZeroQuantityProduct.

 
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
│   │   exeptions.py
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
    │   test_exeptions.py
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
  4. `exeptions.py`: Определяет класс исключений `class ZeroQuantityProduct`.
  Содержит следующие методы:
  - `__init__()` - метод для инициализации экземпляра класса ZeroQuantityProduct.
  5.`product.py`: Определяет `class Product`.
  Содержит следующие методы:
  - `__init__()` - метод для инициализации экземпляра класса Product,
  при инициализации экземпляра класса Product c нулевым количеством, вызывается 
  пользовательское исключение `ZeroQuantityProduct`(наследуется от `ValueError`);
  - `__str__()` - возвращает строковое представление продукта;
  - `__add__()` - метод возвращает сумму произведений цены на количество 
  у двух объектов (общую стоимость товаров двух наименований);
  - `@classmethod new_product()` - класс-метод (возвращает экземпляр класса Product 
  на основе получаемых данных о новом продукте);
  - `@property price()` - геттер (возвращает значение атрибута цена);
  - `@price.setter price()` - сеттер (метод срабатывает при присваивании новой цены).
  6.`product_iterator.py`: Определяет класс `class ProductIterator`.
  Содержит следующие методы:
  - `__init__()` - метод для инициализации экземпляра класса ProductIterator;
  - `__iter__()` - метод, который возвращает итератор;
  - `__next__()` - метод, который возвращает следующий элемент последовательности. 
  7. `smartphone.py`: Определяет класс `class Smartphone`.
  Содержит следующие методы:
  - `__init__()` - метод для инициализации экземпляра класса "Смартфоны" (Smartphone);
  - `__add__()` - метод возвращает сумму произведений цены на количество.
  8. `lawngrass.py`: Определяет класс `class LawnGrass`.
  Содержит следующие методы:
  - `__init__()` - метод для инициализации экземпляра класса "Зеленая трава" (LawnGrass);
  - `__add__()` - метод возвращает сумму произведений цены на количество.
  9. `order.py` : Определяет класс `class Order`.
  Содержит следующие методы:
  - `__init__()` - метод для инициализации экземпляра класса "Заказ" (Order),
  при инициализации экземпляра класса Order c нулевым количеством, вызывается 
  пользовательское исключение `ZeroQuantityProduct`(наследуется от `ValueError`);
  - `get_total_price()` - возвращает общую стоимость товара;
  - `__str__()` - возвращает строковое отображение для класса Order;
  - `add_order()` - метод для добавления заказов в список заказов;
  - `orders_str()` - метод для представления строкового отображения списка заказов;
  - `new_order()` - возвращает экземпляр класса Order на основе получаемых данных 
  о новом продукте.
  10. `print_mixin.py`: Определяет класс `class PrintMixin`.
  Содержит следующие методы:
  - `__init__()` - метод для инициализации экземпляра класса PrintMixin;
  - `__repr__()` - dозвращает строковое представление объекта PrintMixin 
  для печати в консоль.
  11. `utils.py`: Вспомогательные функции для чтения и обработки данных JSON.
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
  12. `test_exeptions.py`: Тесты для модуля `exeptions.py`.
  
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
---------- coverage: platform win32, python 3.13.1-final-0 -----------
Name                              Stmts   Miss  Cover
-----------------------------------------------------
src\__init__.py                       0      0   100%
src\base_product.py                   8      1    88%
src\base_products.py                  8      1    88%
src\category.py                      57     13    77%
src\exceptions.py                     3      0   100%
src\lawngrass.py                     12      3    75%
src\order.py                         49     14    71%
src\print_mixin.py                    5      0   100%
src\product.py                       46     10    78%
src\products_iterator.py             14      0   100%
src\smartphone.py                    13      3    77%
src\utils.py                         27      0   100%
tests\__init__.py                     0      0   100%
tests\conftest.py                    56      0   100%
tests\test_base_product.py           11      0   100%
tests\test_base_products.py           9      0   100%
tests\test_category.py               22      0   100%
tests\test_exeptions.py              13      1    92%
tests\test_lawngrass.py              22      0   100%
tests\test_order.py                  28      0   100%
tests\test_print_mixin.py             9      0   100%
tests\test_product.py                63      3    95%
tests\test_products_iterator.py       9      0   100%
tests\test_smartphone.py             23      0   100%
tests\test_utils.py                  32      0   100%
-----------------------------------------------------
TOTAL                               539     49    91%


============================= 39 passed in 0.58s ====================

```

# Примеры работы основных функций:

1. Пример создания экземпляра класса `Product`:

```
Product(
            name="Samsung Galaxy S23 Ultra", 
            description="256GB, 
            Серый цвет, 200MP 
            камера", price=180000.0, 
            quantity=10
        )
```
Строковое отображение экземпляра класса `Product` (с помощью PrintMixin):
```
Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 10)  
```

2. Пример создания экземпляра класса `Category`:
```
Category(
        name="Смартфоны",
        description="Карманный ПК с функциями мобильного телефона.",
        products=[product1],
    )
```
Строковое оторажение класса Category:
```
Смартфоны, количество продуктов: 10 шт.
```

3. Пример создания экземпляра класса `Smartphone`:
```
Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый",
    )
```
Строковое отображение экземпляра класса  `Smartphone` (с помощью PrintMixin):
```
Smartphone('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
```

4. Пример создания экземпляра класса `LawnGrass`:
```
lawngrass1() -> LawnGrass:
    """Возвращает экземпляр класса LawnGrass"""
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )
```
Строковое отображение экземпляра класса `LawnGrass` (с помощью PrintMixin):
```
.LawnGrass('Газонная трава', 'Элитная трава для газона', 500.0, 20)
```

5. Пример создания экземпляра класса `Order`:
```
Order(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=5
    )
```
Строковое отображение экземпляра класса `Order` (с помощью PrintMixin):
```
Order('Iphone 15', '512GB, Gray space', 210000.0, 5)
```

# Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE.txt).