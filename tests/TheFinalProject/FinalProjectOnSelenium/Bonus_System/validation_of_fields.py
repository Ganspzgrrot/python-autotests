import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
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

        with allure.step('В поле "Имя" ввести валидное значение, например, Хельмут'):
            wait_xpath(driver, "//input[@id='bonus_username']").send_keys('Хельмут')
        with allure.step('В поле "Телефон" ввести валидное значение, например, 89009009090'):
            wait_xpath(driver, "//input[@id='bonus_phone']").send_keys('89009009090')
        with allure.step('Нажать кнопку "Оформить карту"'):
            wait_xpath(driver, "//button[contains(text(),'Оформить карту')]")
        with allure.step('Сообщение об ошибке "Поле Имя обязательно для заполнения" и "Поле Телефон обязательно для заполнения"'):
            error_text = wait_xpath(driver, "//div[@id='bonus_content']/text()[contains(., 'Имя')]").text
            logger.info(error_text)
            assert '24135' == error_text
