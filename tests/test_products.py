__DEFAULT_NUMBER_OF_PRODUCTS = 6


def test_number_of_products(get_login_page):
    products_page = get_login_page.login_as_standard_user()
    assert products_page.get_number_of_products() == __DEFAULT_NUMBER_OF_PRODUCTS


def test_add_one_product_to_cart(get_login_page):
    products_page = get_login_page.login_as_standard_user()
    products_page.add_product_to_card()
    assert int(products_page.get_number_of_added_products()) == 1


