from selenium.webdriver.common.by import By

class YandexPageLocators(object):
    INPUT = (By.XPATH, '//input[@id="text"]')
    POPUP = (By.XPATH, '//ul[@class="mini-suggest__popup-content"]')
    ENTER = (By.XPATH, '//div[@class="mini-suggest__button-text"]')
    RESULT = (By.XPATH, '//a[@href="https://tensor.ru/"]')

class PicturesPageLocators(object):
    PICTURES = (By.XPATH, '//a[@data-id="images"]')
    LINK = (By.XPATH, '//a[@class="PopularRequestList-Preview"]')
    INPUT = (By.XPATH, '//input[@class="input__control mini-suggest__input"]')
    PICTURE = (By.XPATH, '//a[@class="Link PopularRequestList-Preview"]')
    SMALL_PIC = (By.XPATH,'//img[@class="serp-item__thumb justifier__thumb"]')
    IMG = (By.XPATH, '//img[@class="MMImage-Origin"]')
    NEXT = (By.XPATH, '//i[@class="CircleButton-Icon"]')
    PREV = (By.XPATH, '//i[@class="CircleButton-Icon"]')