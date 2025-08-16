import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "chrome_browser: mark test to run only with Chrome browser"
    )

@pytest.fixture()
def chrome_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()