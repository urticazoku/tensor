from selenium import webdriver
import page
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\eshaymardanova\\Video 1\\tensor\\chromedriver.exe")
        self.driver.get("http://www.yandex.ru")

    def test_yandex(self):
        yandex_page = page.YandexPage(self.driver) #зайти на yandex.ru
        self.driver.implicitly_wait(20) #ввести капчу
        assert yandex_page.is_yandex_input(), True #проверить наличие поля поиска
        yandex_page.yandex_input("Тензор") #ввести в поиск тензор
        assert yandex_page.check_popup(), True #проверить, что появилась таблица с подсказками
        yandex_page.click_enter() #нажать Enter
        self.driver.implicitly_wait(20) #ввести капчу
        assert yandex_page.find_tensor(), True #проверить 1 ссылка ведет на сайт tensor.ru

    def test_pictures(self):
        pictures_page = page.PicturesPage(self.driver) #зайти на yandex.ru
        self.driver.implicitly_wait(20) #ввести капчу
        assert pictures_page.is_pictures(), True #проверить, что ссылка Картинки присутствует на странице
        pictures_page.pictures_click() #кликаем на ссылку Картинки
        assert pictures_page.check_pictures(), True #проверить. что перешли на yandex.ru/images
        pictures_page.click_picture() #открыть первую категорию
        assert pictures_page.check_name(), True #проверить, что название есть в поле поиска
        pictures_page.click_small_pic() #открыть первую картинку
        src_1 = pictures_page.check_picture() #проверить, что картинка открылась
        pictures_page.click_next() #нажать кнопку вперед
        src_2 = pictures_page.check_picture_2()
        assert not src_1 == src_2 #проверить, что картинка сменилась
        pictures_page.click_prev() #нажать кнопку назад
        src_3 = pictures_page.check_picture()
        assert src_1 == src_3 #проверить, что картинка осталась из шага 8


