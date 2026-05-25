import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait

from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_on_css_selector import wait_css
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_on_xpath import wait_xpath
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

class TestSocialLInks:
    def test_bonus_system(self, driver):
        with allure.step('Отрыть бонусную систему сайта пиццерии https://pizzeria.skillbox.cc/bonus/'):
            driver.get("https://pizzeria.skillbox.cc/bonus/")
            logger.info('Запускаем браузер в полный экран....')
            driver.maximize_window()
            wait = WebDriverWait(driver, 10)

        with allure.step('В поле "Имя" ввести валидное значение, например, Хельмут'):
            wait_xpath(driver, "//input[@id='bonus_username']").send_keys('Хельмут')
        with allure.step('В поле "Телефон" ввести валидное значение, например, 89009009090'):
            wait_xpath(driver, "//input[@id='bonus_phone']").send_keys('89009009090')
        with allure.step('Нажать кнопку "Оформить карту"'):
            wait_xpath(driver, "//button[contains(text(),'Оформить карту')]").click()
        with allure.step('Сообщение об ошибке "Поле Имя обязательно для заполнения" и "Поле Телефон обязательно для заполнения"'):
            try:
                wait.until(EC.alert_is_present())
                driver.switch_to.alert.accept()
            except Exception:
                pass
            valid_text = wait_xpath(driver, "//h3[contains(text(),'Ваша карта оформлена!')]").text
            assert 'Ваша карта оформлена!' == valid_text

    def test_bonus_system_validation(self, driver):
        with allure.step('Отрыть бонусную систему сайта пиццерии https://pizzeria.skillbox.cc/bonus/'):
            driver.get("https://pizzeria.skillbox.cc/bonus/")
            logger.info('Запускаем браузер в полный экран....')
            driver.maximize_window()
            wait = WebDriverWait(driver, 10)

        with allure.step('Поле "Имя" оставить пустым'):
            wait_xpath(driver, "//input[@id='bonus_username']").send_keys('')
        with allure.step('Поле "Телефон" оставить пустым'):
            wait_xpath(driver, "//input[@id='bonus_phone']").send_keys('')
        with allure.step('Нажать кнопку "Оформить карту"'):
            wait_css(driver, "button[name='bonus']").click()
        with allure.step('Сообщение об ошибке "Поле Телефон обязательно для заполнения"'):
            error_text_phone = wait_xpath(driver, "(//div[@id='bonus_content'])[1]").text
            logger.info(error_text_phone)
            assert 'Поле "Телефон" обязательно для заполнения' in error_text_phone
