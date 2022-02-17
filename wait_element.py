from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait
from browser_alone import WebDriverFactory

browser = WebDriverFactory().driver


def wait_presence(how, what):
    try:
        element = WebDriverWait(browser, 10, ignored_exceptions=
        [NoSuchElementException,
         ElementNotVisibleException,
         ElementNotSelectableException]
                                ).until(
            EC.presence_of_element_located((how, what))
        )
        return element
    except:
        browser.quit()
        print('\n', how, what, ": ", "Element not found!")


def wait_click(how, what):
    try:
        element = WebDriverWait(browser, 10, ignored_exceptions=
        [NoSuchElementException,
         ElementNotVisibleException,
         ElementNotSelectableException]
                                ).until(
            EC.element_to_be_clickable((how, what))
        )
        return element
    except:
        browser.quit()
        print('\n', how, what, ": ", "Element not clickable!")


def wait_download_button(how, what):
    try:
        element = WebDriverWait(browser, 100, ignored_exceptions=
        [NoSuchElementException,
         ElementNotVisibleException,
         ElementNotSelectableException]
                                ).until(
            EC.visibility_of_element_located((how, what))
        )
        return element
    except:
        browser.quit()
        print('\n', how, what, ": ", "Element not found!")
