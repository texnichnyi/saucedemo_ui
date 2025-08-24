from base.base_page import BasePage


class Products(BasePage):
    """
    Products page /inventory.html
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.product_items = self.find_elements(self.locator_css_selector("[data-test='inventory-item']"))
        self.product_button = self.find_element(self.locator_css_selector("[data-test='add-to-cart-sauce-labs-bike-light']"))

    def get_number_of_products(self):
        return len(self.product_items)

    def add_product_to_card(self):
        self.product_button.click()

    def get_number_of_added_products(self):
        number_added_products_icon = self.find_element(self.locator_css_selector("[data-test='shopping-cart-badge']"))
        return number_added_products_icon.text
