import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_on_xpath import wait_until
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
            wait_until(driver, "//input[@id='bonus_username']").send_keys('Хельмут')
        with allure.step('В поле "Телефон" ввести валидное значение, например, 89009009090'):
            wait_until(driver, "//input[@id='bonus_phone']").send_keys('89009009090')
        with allure.step('Нажать кнопку "Оформить карту"'):
            wait_until(driver, "//button[contains(text(),'Оформить карту')]")
        time.sleep(3)
