import pytest
from selenium import webdriver


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "chrome_browser: mark test to run only with Chrome browser"
    )

@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()