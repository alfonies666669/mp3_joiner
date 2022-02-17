import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from browser_alone import WebDriverFactory
from page_methods import wait_for_open
from wait_element import *
from file_work import list_books
from locators import *
from after_download import *

url = "https://audio-joiner.com/ru/"
browser = WebDriverFactory().driver


def get_url(link):
    browser.get(link)
    if wait_for_open():
        return True
    else:
        return False


def drag_and_drop_mp3file(pathed):
    if wait_presence(*Locators.add):
        browser.find_element(*Locators.add).send_keys(pathed)  # field_drag_and_drop


def cross_off():
    list_cross = browser.find_elements(*Locators.cross_on)  # cross_off
    for i in list_cross:
        browser.find_element(i).click()


def check_exists_by_xpath(how, what):
    try:
        browser.find_element(how, what)
    except NoSuchElementException:
        return False
    return True


def main(how_much=3):
    path = ''
    # print("Input path folder:")
    # input(path)
    # print("How much files?")
    # input(int(how_much))
    list_book = list_books(r"C:\Users\Serafim\Downloads\man_who_laughs")
    if get_url("https://audio-joiner.com/ru/"):
        for i in range(0, how_much):
            drag_and_drop_mp3file(list_book[i])
        browser.find_element(*Locators.save_button).click()
        wait_download_button(*Locators.download_button)
        browser.find_element(*Locators.download_button).click()
        while not find_the_file():
            continue
        path_to_mp3 = find_the_file()
        replace_file(path_to_mp3, rename("test"), '1')
    browser.quit()
    print("File already downloaded")


main()
