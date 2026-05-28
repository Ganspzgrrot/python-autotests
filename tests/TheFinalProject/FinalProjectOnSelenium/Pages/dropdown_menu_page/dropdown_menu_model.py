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

class DropdownMenu:
    def __init__(self, driver):
        self.driver = driver
        self.MAIN_PAGE_URL = "https://pizzeria.skillbox.cc"
        self.DROPDOWN_MENU = "//a[contains(text(),'Меню')]"
        self.ITEM_PIZZA = "//a[contains(text(),'Пицца')]"
        self.ITEM_DESERTS = "//a[contains(text(),'Десерты')]"
        self.ITEM_DRINKS = "//a[contains(text(),'Напитки')]"

    def open(self):
        with allure.step('Открыть главную страницу сайта Pizzeria'):
            self.driver.get(self.MAIN_PAGE_URL)

    def max_win(self):
        logger.info('Запускаем браузер в полный экран....')
        self.driver.maximize_window()

    def cursor_move_to_menu(self):
        with allure.step('Навести курсор мыши на дропдаун "Меню" и в выпадающем списке выбрать пункт "Пицца"'):
            action = ActionChains(self.driver)
            dropdown_menu = wait_xpath(self.driver, self.DROPDOWN_MENU)
            action.move_to_element(dropdown_menu).perform()

    def select_pizza_item(self):
        wait_xpath(self.driver, self.ITEM_PIZZA).click()

    def select_deserts_item(self):
        with allure.step('Навести курсор мыши на дропдаун "Меню" и в выпадающем списке выбрать пункт "Десерты"'):
            wait_xpath(self.driver, self.ITEM_DESERTS).click()

    def select_drinks_item(self):
        with allure.step('Навести курсор мыши на дропдаун "Меню" и в выпадающем списке выбрать пункт "Напитки"'):
            wait_xpath(self.driver, self.ITEM_DRINKS).click()