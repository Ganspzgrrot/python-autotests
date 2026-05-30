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

class ClickableSocialLinks:
    def __init__(self, driver):
        self.driver = driver
        self.MAIN_PAGE_URL = "https://pizzeria.skillbox.cc"
        #Для подвала сайта:
        self.SHARES_LINK = "//li[@class='page_item page-item-394']//a[contains(text(),'Акции')]"
        self.BONUS_PROGRAM_LINK = "//li[@class='page_item page-item-359']//a[contains(text(),'Бонусная программа')]"
        self.ALL_PRODUCTS_LINK = "//a[contains(text(),'Все товары')]"
        self.MAIN_PAGE_LINK = "//li[@class='page_item page-item-39 current_page_item']//a[contains(text(),'Главная')]"
        self.DELIVERY_AND_PAYMENT_LINK = "//li[@class='page_item page-item-376']//a[contains(text(),'Доставка и оплата')]"
        self.CART_LINK = "//li[@class='page_item page-item-20']//a[contains(text(),'Корзина')]"
        self.MY_ACCOUNT_LINK = "//li[@class='page_item page-item-22']//a[contains(text(),'Мой аккаунт')]"
        self.ABOUT_US_LINK = "//li[@class='page_item page-item-378']//a[contains(text(),'О нас')]"
        self.PLACE_ORDER_LINK = "li[class='page_item page-item-24'] a"
        self.REGISTRATION_LINK = "//a[contains(text(),'Регистрация')]"

    def open(self):
        with allure.step('Отрыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            self.driver.get(self.MAIN_PAGE_URL)

    def go_to_main_page(self):
        self.driver.get(self.MAIN_PAGE_URL)

    def max_win(self):
        self.driver.maximize_window()

    def validation_shares_link(self):
        with allure.step('Нажать ссылку "Акции"'):
            previous_url = self.driver.current_url
            wait_xpath(self.driver, self.SHARES_LINK).click()
            cur_url = self.driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/promo/"
            self.driver.get('https://pizzeria.skillbox.cc/')

    def validation_bonus_program_link(self):
        with allure.step('Нажать кнопку "Бонусная программа"'):
            previous_url = self.driver.current_url
            wait_xpath(self.driver, self.BONUS_PROGRAM_LINK).click()
            cur_url = self.driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/bonus/"
            self.driver.get('https://pizzeria.skillbox.cc/')

    def validation_all_products_link(self):
        with allure.step('Нажать кнопку "Все товары"'):
            previous_url = self.driver.current_url
            wait_xpath(self.driver, self.ALL_PRODUCTS_LINK).click()
            cur_url = self.driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/shop/"
            self.driver.get('https://pizzeria.skillbox.cc/')

    def validation_main_link(self):
        with allure.step('Нажать кнопку "Главная"'):
            previous_url = self.driver.current_url
            wait_xpath(self.driver, self.MAIN_PAGE_LINK).click()
            cur_url = self.driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url == cur_url and cur_url == "https://pizzeria.skillbox.cc/"
            self.driver.get('https://pizzeria.skillbox.cc/')

    def validation_delivery_and_payment_link(self):
        with allure.step('Нажать кнопку "Доставка и оплата"'):
            previous_url = self.driver.current_url
            wait_xpath(self.driver, self.DELIVERY_AND_PAYMENT_LINK).click()
            cur_url = self.driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/delivery/"
            self.driver.get('https://pizzeria.skillbox.cc/')

    def validation_cart_link(self):
        with allure.step('Нажать кнопку "Корзина"'):
            previous_url = self.driver.current_url
            wait_xpath(self.driver, self.CART_LINK).click()
            cur_url = self.driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/cart/"
            self.driver.get('https://pizzeria.skillbox.cc/')

    def validation_my_account_link(self):
        with allure.step('Нажать кнопку "Мой аккаунт"'):
            previous_url = self.driver.current_url
            wait_xpath(self.driver, self.MY_ACCOUNT_LINK).click()
            cur_url = self.driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/my-account/"
            self.driver.get('https://pizzeria.skillbox.cc/')

    def validation_about_us_link(self):
        with allure.step('Нажать кнопку "О нас"'):
            previous_url = self.driver.current_url
            wait_xpath(self.driver, self.ABOUT_US_LINK).click()
            cur_url = self.driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/about/"
            self.driver.get('https://pizzeria.skillbox.cc/')

    def validation_place_order(self):
        with allure.step('Нажать кнопку "Оформление заказа"'):
            previous_url = self.driver.current_url
            wait_css(self.driver, self.PLACE_ORDER_LINK).click()
            cur_url = self.driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/cart/"
            self.driver.get('https://pizzeria.skillbox.cc/')

    def validation_registration_link(self):
        with allure.step('Нажать кнопку "Регистрация"'):
            previous_url = self.driver.current_url
            wait_xpath(self.driver, self.REGISTRATION_LINK).click()
            cur_url = self.driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/register/"
            self.driver.get('https://pizzeria.skillbox.cc/')