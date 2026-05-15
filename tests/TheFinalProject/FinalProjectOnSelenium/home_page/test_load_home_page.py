import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

class TestHomePage:
    def test_home_page_loaded(self, driver):
        driver.get("https://pizzeria.skillbox.cc")
        wait = WebDriverWait(driver, 10)

        logger.info('Создаем список всех локаторов - загружаемых элементов страницы....')
        main_page_locators = [
            (By.XPATH, "//aside[@id='accesspress_store_product-5']"), (By.XPATH, "//aside[@id='accesspress_store_product-6']"), (By.XPATH, "//aside[@id='accesspress_store_product-7']"),
            (By.CSS_SELECTOR, '.banner-text')
        ]

        logger.info('Запускаем процесс валидации....')
        counter = 0
        for locator in main_page_locators:
            counter += 1
            assert wait.until(EC.presence_of_element_located(locator))
            logger.info(f'Элемент {counter}: загружен успешно')
        logger.info('Процесс валидации завершен, браузер закрыт.')