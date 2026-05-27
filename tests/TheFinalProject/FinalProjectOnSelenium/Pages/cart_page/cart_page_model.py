from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css_all_elements
import allure
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.MAIN_PAGE_URL = "https://pizzeria.skillbox.cc"
        self.PIZZA_ELEMENT = "a[title='Пицца «4 в 1»']"
        self.BUTTON_ADD_TO_CART = "//button[@name='add-to-cart']"
        self.CART_BUTTON = '//*[@id="menu-item-29"]//a'
        self.PRODUCT_LIST = "td.product-name"
        self.PRODUCT_QUANTITY = "input.qty"
        self.TOTAL_AMOUNT = "strong > span.woocommerce-Price-amount.amount > bdi"
        self.PRODUCT_PRICE = "td.product-price span.woocommerce-Price-amount"
        self.QUANTITY_PRODUCT_IN_CARD = "//input[@name='quantity']"
        self.COUPON_FIELD = "//input[@id='coupon_code']"
        self.APPLY_COUPON_BUTTON = "//button[@name='apply_coupon']"

    def max_win(self):
        self.driver.maximize_window()

    def open(self):
        with allure.step('Открыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            self.driver.get(self.MAIN_PAGE_URL)
            logger.info('Запускаем браузер в полный экран....')

    def click_pizza_card(self):
        with allure.step('Нажать на карточку товара'):
            logger.info('Ищем и нажимаем на карточку товара "Пицца «4 в 1»"....')
            wait_css(self.driver, self.PIZZA_ELEMENT).click()

    def add_to_cart(self):
        with allure.step('Нажать на кнопку "Добавить в корзину"'):
            logger.info('Ищем и нажимаем на кнопку "Добавить в корзину"....')
            wait_xpath(self.driver, self.BUTTON_ADD_TO_CART).click()

    def click_cart_button(self):
        with allure.step('Нажать на кнопку "Корзина" в меню сайта пиццерии'):
            logger.info('Ищем и нажимаем на кнопку "Корзина", и осуществляем в нее переход....')
            wait_xpath(self.driver, self.CART_BUTTON).click()

    def list_products(self):
        logger.info('Получаем список всех товаров из корзины....')
        return wait_css_all_elements(self.driver, self.PRODUCT_LIST)

    def product_quantity(self):
        return wait_css(self.driver, self.PRODUCT_QUANTITY)

    def total_amount(self):
        return wait_css(self.driver, self.TOTAL_AMOUNT)

    def product_price(self):
        return wait_css(self.driver, self.PRODUCT_PRICE)

    def clear_and_paste_value_in_field(self, quantity):
        with allure.step('Очистить поле и выставить количество товаров 3'):
            wait_xpath(self.driver, self.QUANTITY_PRODUCT_IN_CARD).clear()
            result = wait_xpath(self.driver, self.QUANTITY_PRODUCT_IN_CARD).send_keys(quantity)
        return result

    def coupon_application(self, coupon):
        with allure.step('Применение купона: в поле для ввода купона ввести промокод GIVEMEHALYAVA и нажать кнопку "Применить купон"'):
            logger.info('Применяем купон....')
            wait_xpath(self.driver, self.COUPON_FIELD).send_keys(coupon)
            wait_xpath(self.driver, self.APPLY_COUPON_BUTTON).click()
