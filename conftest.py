import pytest

from base.driver import Driver
from pages.login import Login


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope='function')
def get_login_page(request):
    """
    Setup and delete driver
    :return: driver
    """
    driver = Driver(browser=request.config.option.browser)
    login_page = Login(driver.get_driver())
    yield login_page
    driver.close_driver()
    del driver