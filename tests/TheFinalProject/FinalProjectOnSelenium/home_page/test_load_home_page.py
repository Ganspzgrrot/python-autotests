import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from tests.TheFinalProject.FinalProjectOnSelenium.Pages.home_page_page.load_home_page_models import LoadHomePage
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

@allure.feature('Главная страница сайта pizzeria')
class TestHomePage:
    @allure.title('Загрузка всех элементов страницы')
    def test_home_page_loaded(self, driver):
        load_home_page = LoadHomePage(driver)
        load_home_page.open()
        load_home_page.max_win()
        wait = WebDriverWait(driver, 10)

        logger.info('Создаем список всех локаторов - загружаемых элементов страницы....')
        main_page_locators = [
            (By.XPATH, "//aside[@id='accesspress_store_product-5']"), (By.XPATH, "//aside[@id='accesspress_store_product-6']"), (By.XPATH, "//aside[@id='accesspress_store_product-7']"),
            (By.CSS_SELECTOR, '.banner-text')
        ]

        with allure.step('Все элементы главной страницы сайта pizzeria загрузились корректно без преломлений и пустых картинок'):
            logger.info('Запускаем процесс валидации....')
            counter = 0
            for locator in main_page_locators:
                counter += 1
                assert wait.until(EC.presence_of_element_located(locator))
                logger.info(f'Элемент {counter}: загружен успешно')
            logger.info(f'Процесс валидации завершен, браузер закрыт. Загружено элементов: {counter}')