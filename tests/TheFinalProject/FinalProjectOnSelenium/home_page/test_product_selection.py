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

class TestMainPage:
    @allure.title('Название карточки товара соответствует с текстом внутри нее')
    def test_open_product_details(self, driver):
        with allure.step('Открыть главную страницу пиццерии https://pizzeria.skillbox.cc/'):
            driver.get("https://pizzeria.skillbox.cc/")
            logger.info('Запускаем браузер во весь экран....')
            driver.maximize_window()
            wait = WebDriverWait(driver, 10)

        with allure.step('На главной странице пиццерии нажать на карточку товара, например, "Пицца «4 в 1" и запоминаем это название'):
            logger.info('Ищем карточку товара с пиццей «4 в 1» и нажимаем на эту карточку....')
            driver.find_element(By.CSS_SELECTOR, "a[title='Пицца «4 в 1»']").click()
            logger.info('Ищем текст "Пицца «4 в 1»" из панели навигации "Все товары"....')
            current_text = driver.find_element(By.XPATH, "//span[text()='Пицца «4 в 1»']")

        with allure.step('Сравнить ожидаемое название карточки товара внутри нее'):
            logger.info('Запускаем процесс валидации текста в панели навигации "Все товары"....')
            assert 'пицца «4 в 1»' in current_text.text.lower()
            logger.info('Процесс валидации завершен, браузер закрыт.')