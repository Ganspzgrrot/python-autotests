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
        self.MENU_PIZZA_URL = "https://pizzeria.skillbox.cc/product-category/menu/pizza/"
        self.ITEM_DESERTS = "//li[@class='cat-item cat-item-31']//a[contains(text(),'Десерты')]"
        self.ITEM_CATALOG = "//a[contains(text(),'Каталог')]"
        self.ITEM_MENU = "//li[@class='cat-item cat-item-29']//a[contains(text(),'Меню')]"
        self.ITEM_DRINKS = "//li[@class='cat-item cat-item-32']//a[contains(text(),'Напитки')]"

    def open(self):
        with allure.step('Открыть главную страницу сайта Pizzeria'):
            self.driver.get(self.MENU_PIZZA_URL)

    def max_win(self):
        logger.info('Запускаем браузер в полный экран....')
        self.driver.maximize_window()

    def click_and_validate_item_deserts(self):
        previous_url = self.driver.current_url
        wait_xpath(self.driver, self.ITEM_DESERTS).click()
        cur_url = self.driver.current_url
        assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/product-category/menu/deserts/"
        self.driver.get(self.MENU_PIZZA_URL)

    def click_and_validate_item_catalog(self):
        previous_url = self.driver.current_url
        wait_xpath(self.driver, self.ITEM_CATALOG).click()
        cur_url = self.driver.current_url
        assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/product-category/catalog/"
        self.driver.get(self.MENU_PIZZA_URL)

    def click_and_validate_item_menu(self):
        previous_url = self.driver.current_url
        wait_xpath(self.driver, self.ITEM_MENU).click()
        cur_url = self.driver.current_url
        assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/product-category/menu/"
        self.driver.get(self.MENU_PIZZA_URL)

    def click_and_validate_item_drinks(self):
        previous_url = self.driver.current_url
        wait_xpath(self.driver, self.ITEM_DRINKS).click()
        cur_url = self.driver.current_url
        assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/product-category/menu/drinks/"