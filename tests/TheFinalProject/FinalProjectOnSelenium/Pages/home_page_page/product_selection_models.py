from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css_all_elements
from selenium.webdriver.common.action_chains import ActionChains
import allure
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')
from selenium.webdriver.common.by import By

class ProductSelection:
    def __init__(self, driver):
        self.driver = driver
        self.MAIN_PAGE_URL = "https://pizzeria.skillbox.cc"
        self.PIZZA_CARD_4_IN_1 = "a[title='Пицца «4 в 1»']"
        self.TEXT_CURRENT_PIZZA = "//span[text()='Пицца «4 в 1»']"

    def open(self):
        with allure.step('Отрыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            self.driver.get(self.MAIN_PAGE_URL)

    def max_win(self):
        self.driver.maximize_window()

    def pizza_card_text_validation(self):
        with allure.step('На главной странице пиццерии нажать на карточку товара, например, "Пицца «4 в 1" и запоминаем это название'):
            logger.info('Ищем карточку товара с пиццей «4 в 1» и нажимаем на эту карточку....')
            self.driver.get("https://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-4-%d0%b2-1/")
            current_text = wait_xpath(self.driver, self.TEXT_CURRENT_PIZZA)
        with allure.step('Сравнить ожидаемое название карточки товара внутри нее'):
            logger.info('Запускаем процесс валидации текста в панели навигации "Все товары"....')
            assert 'пицца «4 в 1»' in current_text.text.lower()
            logger.info('Процесс валидации завершен, браузер закрыт.')