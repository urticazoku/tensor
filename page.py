from elements import BasePageElement
from locators import YandexPageLocators, PicturesPageLocators
from selenium import webdriver

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class YandexPage(BasePage):
    def is_yandex_input(self):
        element = self.driver.find_element(*YandexPageLocators.INPUT)
        if element:
            return True
        else:
            return False

    def yandex_input(self, text):
        element = self.driver.find_element(*YandexPageLocators.INPUT)
        element.send_keys(text)

    def check_popup(self):
        element = self.driver.find_element(*YandexPageLocators.POPUP)
        if element:
            return True
        else:
            return False

    def click_enter(self):
        element = self.driver.find_element(*YandexPageLocators.ENTER)
        element.click()

    def find_tensor(self):
        element = self.driver.find_element(*YandexPageLocators.RESULT)
        if element: 
            return True
        else:
            return False

class PicturesPage(BasePage):
    def is_pictures(self):
        element = self.driver.find_element(*PicturesPageLocators.PICTURES)
        if element:
            return True
        else:
            return False

    def pictures_click(self):
        element = self.driver.find_element(*PicturesPageLocators.PICTURES)
        element.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_pictures(self):
        if "images" in self.driver.current_url:
            return True
        else:
            return False

    def open_link(self):
        element = self.driver.find_element(*PicturesPageLocators.LINK)
        element.click()

    def check_name(self):
        element = self.driver.find_element(*PicturesPageLocators.INPUT)
        if element.get_attribute('value'):
            return True
        else:
            return False

    def click_picture(self):
        element = self.driver.find_element(*PicturesPageLocators.PICTURE)
        element.click()

    def check_picture(self):
        element = self.driver.find_element(*PicturesPageLocators.IMG)
        return element.get_attribute('src')

    def check_picture_2(self):
        element = self.driver.find_element(*PicturesPageLocators.IMG)
        return element.get_attribute('src')

    def click_next(self):
        button_element = self.driver.find_element(*PicturesPageLocators.NEXT)
        self.driver.execute_script("arguments[0].click();", button_element)

    def click_prev(self):
        button_element = self.driver.find_element(*PicturesPageLocators.PREV)
        self.driver.execute_script("arguments[0].click();", button_element)

    def click_small_pic(self):
        element = self.driver.find_element(*PicturesPageLocators.SMALL_PIC)
        element.click()
    