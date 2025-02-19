def test_category(category1):
    assert category1.name == "Смартфоны"
    assert (
        category1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category1.category_count == 1
    assert category1.product_count == 2


def test_category_without_products(category2):
    assert category2.name == "Телевизоры"
    assert (
        category2.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert not category2.products
    assert category2.category_count == 1
    assert category2.product_count
