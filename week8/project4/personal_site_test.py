import pytest
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


site_url = "https://www.ben-merritt.com/"

@pytest.mark.chrome_browser
def test_prolog_emulator(chrome_browser):  
    """
    Test to ensure that my personal site executes Prolog queries with information about my career
    """
    chrome_browser.get(site_url)
    wait = WebDriverWait(chrome_browser, 10)

    proceed_button = wait.until(expected_conditions.element_to_be_clickable((
        By.XPATH,
        "//*/button[contains(text(), 'Proceed')]"
    )))
    proceed_button.click()

    form = wait.until(expected_conditions.element_to_be_clickable((
        By.TAG_NAME,
        'form'
    )))
    input = form.find_element(By.TAG_NAME, 'input')
    input.send_keys("skill(X, language).")
    input.submit()
    
    time.sleep(2)

    terminal = chrome_browser.find_element(
        By.XPATH,
        'html/body/div/div/div/div/div'
    )

    assert terminal.find_elements(By.CLASS_NAME, 'MuiTypography-root')[-1].text == """X = typescript
X = python
X = sql
X = go
X = prolog
X = java"""

@pytest.mark.chrome_browser
def test_download_resume(chrome_browser):
    """
    Test to ensure that my resume is available
    """
    chrome_browser.get(site_url)
    actions = ActionChains(chrome_browser)
    actions.key_down(Keys.CONTROL).send_keys("s").key_up(Keys.CONTROL).perform()

    all_tabs = chrome_browser.window_handles
    chrome_browser.switch_to.window(all_tabs[-1])

    assert chrome_browser.current_url == 'https://www.ben-merritt.com/ben_merritt_resume.pdf'


@pytest.mark.chrome_browser
def test_links_to_linkedin(chrome_browser):
    """
    Test to ensure that my site links to my LinkedIn profile
    """
    chrome_browser.get(site_url)
    actions = ActionChains(chrome_browser)
    actions.key_down(Keys.CONTROL).send_keys("o").key_up(Keys.CONTROL).perform()

    all_tabs = chrome_browser.window_handles
    chrome_browser.switch_to.window(all_tabs[-1])

    assert 'LinkedIn' in chrome_browser.title
