import pytest
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.chrome_browser
def test_marketplace(chrome_browser):  
    """
    Test to ensure that the price on the product is the same that shows up during checkout
    """
    url = "https://cymbal-shops.retail.cymbal.dev/"
    product_text = "Sunglasses"

    chrome_browser.get(url)
    wait = WebDriverWait(chrome_browser, 10)

    product_element = wait.until(expected_conditions.presence_of_element_located((
        By.XPATH,
        f"//div[normalize-space(.)='{product_text}']"
    )))

    price_element = wait.until(expected_conditions.presence_of_element_located((
        By.XPATH,
        f"//div[normalize-space(.)='{product_text}']/following-sibling::div[1]"
    )))
    price_text = price_element.text

    product_anchor = wait.until(expected_conditions.element_to_be_clickable((
        By.XPATH,
        f"//div[normalize-space(.)='{product_text}']/ancestor::div[1]/preceding-sibling::a[1]"
    )))
    product_anchor.click()

    wait.until(expected_conditions.staleness_of(product_element))

    add_to_cart_button = wait.until(expected_conditions.element_to_be_clickable((
        By.XPATH,
        "//*/button[contains(text(), 'Add To Cart')]"
    )))
    add_to_cart_button.click()

    time.sleep(2)

    cart_button = wait.until(expected_conditions.element_to_be_clickable((
        By.CLASS_NAME, "cart-link"
    )))
    cart_button.click()

    wait.until(expected_conditions.staleness_of(add_to_cart_button))

    cart_price = wait.until(expected_conditions.presence_of_element_located((
        By.XPATH,
        f"//div[normalize-space(.)='{price_text}']"
    )))

    assert cart_price.text == price_text
