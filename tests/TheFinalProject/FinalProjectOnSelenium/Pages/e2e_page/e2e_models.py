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

class E2E:
    def __init__(self, driver):
        #Для авторизации пользователя и добавления товара в корзину
        self.driver = driver
        self.MAIN_PAGE_URL = "https://pizzeria.skillbox.cc"
        self.PIZZA_PAGE_URL = "https://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-4-%d0%b2-1/"
        self.FIELD_USERNAME = "//input[@id='username']"
        self.FIELD_PASSWORD = "//input[@id='password']"
        self.LOGIN_BUTTON = "//button[@name='login']"
        self.BUTTON_ADD_TO_CART = "//button[@name='add-to-cart']"
        self.BUTTON_LEARN_MORE = "//a[text()='Подробнее']"
        self.BUTTON_PROCEED_TO_PAYMENT = "//a[contains(text(), 'ПЕРЕЙТИ К ОПЛАТЕ')]"
        self.LOGIN_PAGE_LINK = "//a[contains(text(),'Войти')]"

        #Для оформления заказа:
        self.FIELD_FIRST_NAME = "//input[@id='billing_first_name']"
        self.FIELD_LAST_NAME = "//input[@id='billing_last_name']"
        self.FIELD_ADDRESS = "//input[@id='billing_address_1']"
        self.FIELD_CITY = "//input[@id='billing_city']"
        self.FIELD_STATE = "//input[@id='billing_state']"
        self.FIELD_POSTCODE = "//input[@id='billing_postcode']"
        self.FIELD_PHONE = "//input[@id='billing_phone']"
        self.CHECKBOX_TERMS = "//input[@id='terms']"
        self.BUTTON_PLACE_ORDER = '//button[@id="place_order"]'

        #Для регистрации пользователя
        self.BUTTON_START_REGISTRATION = "//button[text()='Зарегистрироваться']"
        self.FIELD_USERNAME_FOR_REGISTRATION = "//input[@id='reg_username']"
        self.FIELD_EMAIL_FOR_REGISTRATION = "//input[@id='reg_email']"
        self.FIELD_PASSWORD_FOR_REGISTRATION = "//input[@id='reg_password']"
        self.BUTTON_END_REGISTRATION = "//button[@name='register']"

    def open(self):
        with allure.step('Открыть главную страницу сайта Pizzeria'):
            self.driver.get(self.MAIN_PAGE_URL)

    def max_win(self):
        logger.info('Запускаем браузер в полный экран....')
        self.driver.maximize_window()

    def login(self):
        logger.info('Авторизация раннее зарегистрированного пользователя....')
        with allure.step('Перейти на страницу авторизации пользователя'):
            wait_xpath(self.driver, self.LOGIN_PAGE_LINK).click()
        with allure.step('В поле "Имя пользователя или почта*" вписать "helmutpzh"'):
            wait_xpath(self.driver, self.FIELD_USERNAME).send_keys('helmutpzh')
        with allure.step('В поле "Пароль*" вписать "1234567890-"'):
            wait_xpath(self.driver, self.FIELD_PASSWORD).send_keys('1234567890-')
        with allure.step('Нажать кнопку "ВОЙТИ"'):
            wait_xpath(self.driver, self.LOGIN_BUTTON).click()

    def add_product_in_cart(self):
        with allure.step('Открыть карточку товара "Пицца 4 в 1"'):
            logger.info('Процесс перехода на главную страницу и в корзину, с добавленным товаром(Пиццей 4 в 1)....')
            self.driver.get(self.PIZZA_PAGE_URL)
        with allure.step('Нажать кнопку "В корзину"'):
            wait_xpath(self.driver, self.BUTTON_ADD_TO_CART).click()
        with allure.step('Нажать кнопку "Подробнее"'):
            wait_xpath(self.driver, self.BUTTON_LEARN_MORE).click()
        with allure.step('Нажать кнопку "Перейти к оплате"'):
            wait_xpath(self.driver, self.BUTTON_PROCEED_TO_PAYMENT).click()

    def user_registration(self):
        logger.info('Запущен процесс регистрации нового пользователя....')
        with allure.step('Нажать кнопку "Зарегистрироваться"'):
            wait_xpath(self.driver, self.BUTTON_START_REGISTRATION).click()
        with allure.step('В поле "Имя пользователя*" вписать "helmutpzh'):
            wait_xpath(self.driver, self.FIELD_USERNAME_FOR_REGISTRATION).send_keys('helmutpzh')
        with allure.step('В поле "Адрес почты*" вписать "helmutpzh@test.ru"'):
            wait_xpath(self.driver, self.FIELD_EMAIL_FOR_REGISTRATION).send_keys(f'helmutpzh@test.ru')
        with allure.step('В поле "Пароль*" вписать "1234567890-"'):
            wait_xpath(self.driver, self.FIELD_PASSWORD_FOR_REGISTRATION).send_keys('1234567890-')
        with allure.step('Нажать кнопку "Зарегистрироваться"'):
            wait_xpath(self.driver, self.BUTTON_END_REGISTRATION).click()

    def making_an_order(self):
        logger.info('Процесс оформления заказа(Заполнение полей и выделение чек-боксов)....')
        with allure.step('В поле "Имя*" ввести значение "Хельмут"'):
            wait_xpath(self.driver, self.FIELD_FIRST_NAME).clear(); wait_xpath(self.driver, self.FIELD_FIRST_NAME).send_keys('Хельмут')
        with allure.step('В поле "Фамилия*" ввести значение "Мюллер"'):
            wait_xpath(self.driver, self.FIELD_LAST_NAME).clear(); wait_xpath(self.driver, self.FIELD_LAST_NAME).send_keys('Мюллер')
        with allure.step('В поле "Адрес*" ввести значение "Улица петрозаводской остановки дом 12"'):
            wait_xpath(self.driver, self.FIELD_ADDRESS).clear(); wait_xpath(self.driver, self.FIELD_ADDRESS).send_keys('Улица петрозаводской остановки дом 12')
        with allure.step('В поле "Город/Населенный пункт*" ввести значение "Бранденбург"'):
            wait_xpath(self.driver, self.FIELD_CITY).clear(); wait_xpath(self.driver, self.FIELD_CITY).send_keys('Бранденбург')
        with allure.step('В поле "Область*" ввести значение "Бранденбургская область"'):
            wait_xpath(self.driver, self.FIELD_STATE).clear(); wait_xpath(self.driver, self.FIELD_STATE).send_keys('Бранденбургская область')
        with allure.step('В поле "Почтовый индекс*" ввести значение "123456"'):
            wait_xpath(self.driver, self.FIELD_POSTCODE).clear(); wait_xpath(self.driver, self.FIELD_POSTCODE).send_keys('123456')
        with allure.step('В поле "Телефон*" ввести значение "89009009090"'):
            wait_xpath(self.driver, self.FIELD_PHONE).clear(); wait_xpath(self.driver, self.FIELD_PHONE).send_keys('89009009090')
        with allure.step('Выделить чекбокс "I have read and agree to the website terms and conditions*"'):
            wait_xpath(self.driver, self.CHECKBOX_TERMS).click()
            wait_xpath(self.driver, self.BUTTON_PLACE_ORDER).click()
