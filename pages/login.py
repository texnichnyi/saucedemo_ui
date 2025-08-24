from base.base_page import BasePage
from pages.products import Products


class Login(BasePage):
    """
    Login page
    """
    __STANDARD_USER_NAME = "standard_user"
    __PASSWORD = "secret_sauce"

    def __init__(self, driver):
        super().__init__(driver)
        self.user_name_field = self.find_element(self.locator_id("user-name"))
        self.password_field = self.find_element(self.locator_id("password"))
        self.login_button = self.find_element(self.locator_id("login-button"))

    def login_as_standard_user(self) -> Products:
        self.user_name_field.send_keys(self.__STANDARD_USER_NAME)
        self.password_field.send_keys(self.__PASSWORD)
        self.login_button.click()
        return Products(driver=self.driver)
