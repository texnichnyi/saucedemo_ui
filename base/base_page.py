import os
from typing import List

from wait_for import wait_for
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from base.locator import Locators


class BasePage:
    """
    Class for working with pages
    """

    def __init__(self, driver):
        self.driver = driver
        self.locator_id = Locators.id
        self.locator_css_selector = Locators.css_selector

    def find_element(self, locator: Locators.Locator) -> WebElement:
        return self.driver.find_element(locator.by, locator.value)

    def find_elements(self, locator: Locators.Locator) -> List[WebElement]:
        return self.driver.find_elements(locator.by, locator.value)

