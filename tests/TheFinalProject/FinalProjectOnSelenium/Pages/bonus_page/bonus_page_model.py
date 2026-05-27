from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
import allure
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')
from selenium.webdriver.common.by import By

class BonusPage:
    def __init__(self, driver):
        self.driver = driver
        self.BONUS_PAGE_URL = "https://pizzeria.skillbox.cc/bonus/"
        self.USERNAME_FIELD = "//input[@id='bonus_username']"
        self.PHONE_FIELD = "//input[@id='bonus_phone']"
        self.SUBMIT_BUTTON = "//button[contains(text(),'Оформить карту')]"
        self.SUCCESS_TEXT = "//h3[contains(text(),'Ваша карта оформлена!')]"
        self.ERROR_MESSAGE = "(//div[@id='bonus_content'])[1]"

    def open(self):
        with allure.step('Отрыть бонусную систему сайта пиццерии https://pizzeria.skillbox.cc/bonus/'):
            self.driver.get(self.BONUS_PAGE_URL)

    def max_win(self):
        logger.info('Запускаем браузер в полный экран....')
        self.driver.maximize_window()

    def enter_username(self, name):
        with allure.step('В поле "Имя" ввести валидное значение, например, Хельмут'):
            wait_xpath(self.driver, self.USERNAME_FIELD).send_keys(name)
    def enter_username_without_allure_step(self):
        with allure.step('Поле "Имя" оставить пустым'):
            wait_xpath(self.driver, self.USERNAME_FIELD).send_keys('')

    def enter_phone(self, phone):
        with allure.step('В поле "Телефон" ввести валидное значение, например, 89009009090'):
            wait_xpath(self.driver, self.PHONE_FIELD).send_keys(phone)
    def enter_phone_without_allure_step(self):
        with allure.step('Поле "Телефон" оставить пустым'):
            wait_xpath(self.driver, self.PHONE_FIELD).send_keys('')

    def click_submit(self):
        with allure.step('Нажать кнопку "Оформить карту"'):
            wait_xpath(self.driver, self.SUBMIT_BUTTON).click()

    def get_success_message(self):
        return wait_xpath(self.driver, self.SUCCESS_TEXT).text

    def get_error_message(self):
        return wait_xpath(self.driver, self.ERROR_MESSAGE).text

