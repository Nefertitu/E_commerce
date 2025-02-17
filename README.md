# Проект "E_commerce"

Этот проект представляет собой реализацию основной функциональности 
платформы электронной торговли, или электронной коммерции. 

В настоящее время проект включает два созданных класса: 
- Product
- Category. 
 
Цель проекта состоит в том, чтобы создать основу, которую в будущем 
можно расширить различными интерфейсами, такими как веб-сайты или боты 
в Telegram.

# Структура проекта:
```
E_commerce
│   .coverage
│   .gitignore
│   main.py
│   poetry.lock
│   pyproject.toml
│
├───data
│       products.json
│
├───htmlcov
│       index.html
│
└───src
│   │   __init__.py
│   │
│   ├───category.py
│   ├───product.py
│   └───utils.py
│
└───tests
    │   __init__.py
    │   conftest.py
    │   test_category.py
    │   test_product.py

```
# Каталоги и файлы

- `/data`: Содержит образец данных в формате JSON (`products.json`), 
используемых для загрузки категорий и продуктов.
- `/src`:
  - `category.py`: Определяет `class Category`.
  - `product.py`: Определяет `class Product`.
  - `utils.py`: Вспомогательные функции для чтения и обработки 
данных JSON.
- `/tests`:
  - `conftest.py`: Файл конфигурации для фикстур pytest.
  - `test_category.py`: Тесты для модуля `category.py`.
  - `test_product.py`: Тесты для модуля `product.py`.
  
# Основные файлы

- `.coverage`: Отчёт о покрытии кода, созданный инструментами покрытия.
- `.gitignore`: Указывает файлы и директории, которые следует 
игнорировать при коммитах в Git.
- `main.py`: Точка входа для запуска приложения.
- `poetry.lock`: Файл блокировки зависимостей для управления 
зависимостями с помощью Poetry.
- `pyproject.toml`: Конфигурационный файл для Poetry.

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
---------- coverage: platform win32, python 3.13.1-final-0 ------------------
Name                     Stmts   Miss  Cover
--------------------------------------------
src\__init__.py              0      0   100%
src\category.py             13      0   100%
src\product.py              10      0   100%
src\utils.py                26      0   100%
tests\__init__.py            0      0   100%
tests\conftest.py           21      0   100%
tests\test_category.py      12      0   100%
tests\test_product.py        6      0   100%
tests\test_utils.py         29      0   100%
--------------------------------------------
TOTAL                      117      0   100%


================================================== 7 passed in 0.35s ========
```

# Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE.txt).