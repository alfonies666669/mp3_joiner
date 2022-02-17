from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from browser_alone import WebDriverFactory

browser = WebDriverFactory().driver


def wait_for_open():
    try:
        WebDriverWait(browser, timeout=5).until(
            lambda x: browser.execute_script('return document.readyState') == 'complete')
        return True
    except TimeoutException:
        return False
