from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css_all_elements
import allure
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')
from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.MAIN_PAGE_URL = "https://pizzeria.skillbox.cc"
        self.PIZZA_CARD_PAGE_URL = "https://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-%d1%80%d0%b0%d0%b9/"
        self.LOGIN_PAGE_URL = "https://pizzeria.skillbox.cc/my-account/"
        self.ADD_TO_CART = "//button[@name='add-to-cart']"
        self.CART_IN_MENU = '//*[@id="menu-item-29"]//a'
        self.GO_TO_PAYMENT_BUTTON = "//a[contains(text(), 'ПЕРЕЙТИ К ОПЛАТЕ')]"
        self.LOGIN_LINK = "//a[text()='Авторизуйтесь']"
        self.LOGIN_BUTTON = "//button[@name='login']"
        self.ERROR_TEXT = '//*[@id="post-24"]//li'
        self.FIELD_USERNAME_OR_EMAIL = "//input[@id='username']"
        self.PASSWORD_FIELD = "//input[@id='password']"
        self.LEARN_MORE_BUTTON = "//a[contains(text(),'Подробнее')]"
        self.COUPON_CODE_FIELD = "//input[@id='coupon_code']"
        self.CLICK_ON_LINK_TO_ENTER_COUPON = "//a[contains(text(),'Нажмите для ввода купона')]"
        self.APPLY_COUPON_BUTTON = "//button[contains(text(),'Применить купон')]"
        self.COUPON_CODE_ALREADY_APPLIED_TEXT = "//li[normalize-space()='Coupon code already applied!']"

    def max_win(self):
        self.driver.maximize_window()

    def open(self):
        with allure.step('Открыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            self.driver.get(self.MAIN_PAGE_URL)
            logger.info('Запускаем браузер в полный экран....')

    def open_login_page(self):
        with allure.step('Перейти на страница авторизации на сайте Pizzeria по URL: https://pizzeria.skillbox.cc/my-account/'):
            self.driver.get(self.LOGIN_PAGE_URL)

    def open_pizza_card_page(self):
        with allure.step('Открыть картосчку товара "Пицца 4 в 1"'):
            logger.info('Запускаем и настраиваем загрузку браузера....')
            self.driver.get(self.PIZZA_CARD_PAGE_URL)

    def add_to_cart(self):
        with allure.step('Нажать кнопку "В КОРЗИНУ"'):
            logger.info('Добавление товара и переход в корзину....')
            wait_xpath(self.driver, self.ADD_TO_CART).click()

    def click_cart_button_in_menu(self):
        with allure.step('Нажать кнопку "Корзина" в верхнем меню сайта пиццерии'):
            wait_xpath(self.driver, self.CART_IN_MENU).click()

    def click_go_to_payment_button(self):
        logger.info('Начало оформления заказа....')
        with allure.step('Нажать кнопку "Перейти к оплате"'):
            wait_xpath(self.driver, self.GO_TO_PAYMENT_BUTTON).click()

    def click_login_link(self):
        with allure.step('Нажать ссылку "Авторизуйтесь"'):
            wait_xpath(self.driver, self.LOGIN_LINK).click()

    def click_login_button(self):
        with allure.step('Нажать кнопку "ВОЙТИ"'):
            wait_xpath(self.driver, self.LOGIN_BUTTON).click()

    def get_error_text(self):
        return wait_xpath(self.driver, self.ERROR_TEXT).text

    def fill_username_or_email_field(self, username_or_email):
        with allure.step('В поле "Имя пользователя или почта*" вписать "helmutpzh"'):
            return wait_xpath(self.driver, self.FIELD_USERNAME_OR_EMAIL).send_keys(username_or_email)
    def fill_password_field(self, password):
        with allure.step('В поле "Пароль*" вписать "1234567890-"'):
            return wait_xpath(self.driver, self.PASSWORD_FIELD).send_keys(password)
    def press_learn_more_button(self):
        with allure.step('Нажать кнопку "ПОДРОБНЕЕ" для перехода в корзину'):
            wait_xpath(self.driver, self.LEARN_MORE_BUTTON).click()

    def fill_coupon_code_field(self, coupon):
        with allure.step('В поле "Введите код купона..." ввести промокод GIVEMEHALYAVA'):
            wait_xpath(self.driver, self.COUPON_CODE_FIELD).send_keys(coupon)

    def click_on_link_for_enter_coupon(self):
        with allure.step('На форме оформления заказа нажать кнопку "Нажмите для ввода купона"'):
            wait_xpath(self.driver, self.CLICK_ON_LINK_TO_ENTER_COUPON).click()

    def apply_coupon(self):
        with allure.step('Нажать кнопку "Применить купон"'):
            wait_xpath(self.driver, self.APPLY_COUPON_BUTTON).click()

    def get_text_code_already_applied(self):
        return wait_xpath(self.driver, self.COUPON_CODE_ALREADY_APPLIED_TEXT).text