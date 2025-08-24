from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    """
      Class for working with driver
    """
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = self.__get_chrome_driver()
        else:
            # add as many drivers as your app needs
            pass
        self.driver.implicitly_wait(3)
        self.driver.get('https://www.saucedemo.com/')

    def __get_chrome_driver(self):
        options = webdriver.ChromeOptions()
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()
