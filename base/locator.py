from collections import namedtuple

from selenium.webdriver.common.by import By


class Locators:
    """
    Class of Locator object builder
    """
    Locator = namedtuple("Locator", ["by", "value"])

    @staticmethod
    def id(value: str) -> Locator:
        """
        Building Locator object by id selector
        """
        return Locators.Locator(By.ID, value)

    @staticmethod
    def css_selector(value: str) -> Locator:
        """
        Building Locator object by class name selector
        """
        return Locators.Locator(By.CSS_SELECTOR, value)
