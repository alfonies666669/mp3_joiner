from selenium.webdriver.common.by import By


class Locators:
    add = (By.CSS_SELECTOR, 'input.file-input')
    bars_wrapper = (By.CSS_SELECTOR, 'div.control-bars-wrapper')
    cross_on = (By.XPATH, "//div[@class='btn-fade fade-cross active']")
    save_button = (By.CSS_SELECTOR, "div.save-label")
    file_size = (By.XPATH, "//div[@class = 'file-size']")
    download_button = (By.XPATH, "//div[@class = 'md-dropdown-label']/a")
