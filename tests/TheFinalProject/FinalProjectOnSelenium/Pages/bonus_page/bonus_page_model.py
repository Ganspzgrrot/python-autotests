from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
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
        self.driver.get(self.BONUS_PAGE_URL)

    def enter_username(self, name):
        wait_xpath(self.driver, self.USERNAME_FIELD).send_keys(name)

    def enter_phone(self, phone):
        wait_xpath(self.driver, self.PHONE_FIELD).send_keys(phone)

    def click_submit(self):
        wait_xpath(self.driver, self.SUBMIT_BUTTON).click()

    def get_success_message(self):
        return wait_xpath(self.driver, self.SUCCESS_TEXT).text

    def get_error_message(self):
        return wait_xpath(self.driver, self.ERROR_MESSAGE).text

