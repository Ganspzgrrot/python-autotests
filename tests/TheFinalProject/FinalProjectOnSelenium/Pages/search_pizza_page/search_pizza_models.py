from selenium.webdriver import Keys

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

class SearchPizza:
    def __init__(self, driver):
        self.driver = driver
        self.MAIN_PAGE_URL = "https://pizzeria.skillbox.cc"
        self.PIZZA_RAI = "//input[@name='s']"
        self.CURRENT_TEXT_PIZZA_RAI = "//h1[text()='Пицца «Рай»']"
        self.CURRENT_TEXT_ON_NAVIGATION_BAR = "//span[text()='Пицца «Рай»']"

    def open(self):
        with allure.step('Отрыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            self.driver.get(self.MAIN_PAGE_URL)
    def max_win(self):
        self.driver.maximize_window()

    def click_pizza_rai(self):
        logger.info('Ищем локатор поля поиска и вводим в него значение "Рай...."')
        wait_xpath(self.driver, self.PIZZA_RAI).send_keys('Рай', Keys.ENTER)

    def pizza_rai_text(self):
        logger.info('Извлекаем текст из заголовка пиццы(Пицца «Рай»)....')
        return wait_xpath(self.driver, self.CURRENT_TEXT_PIZZA_RAI).text.lower()

    def pizza_rai_text_on_navigation_bar(self):
        logger.info('Извлекаем текст "Пицца «Рай»" из меню навигации "Все товары"')
        return wait_xpath(self.driver, self.CURRENT_TEXT_ON_NAVIGATION_BAR).text.lower()