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

class TestSearchPizza:
    def test_search_pizza_and_validate(self, driver):
        driver.get('https://pizzeria.skillbox.cc')
        driver.maximize_window()

        logger.info('Ищем локатор поля поиска и вводим в него значение "Рай...."')
        driver.find_element(By.XPATH, "//input[@name='s']").send_keys('Рай', Keys.ENTER)
        logger.info('Извлекаем текст из заголовка пиццы(Пицца «Рай»)....')
        current_text_title = driver.find_element(By.XPATH, "//h1[text()='Пицца «Рай»']")
        logger.info('Извлекаем текст "Пицца «Рай»" из меню навигации "Все товары"')
        current_text_on_navigation_bar = driver.find_element(By.XPATH, "//span[text()='Пицца «Рай»']")

        logger.info('Запускаем процесс валидации соответствия пиццы раннее веденному запросу...')
        assert 'рай' in current_text_title.text.lower()
        assert 'рай' in current_text_on_navigation_bar.text.lower()
        logger.info('Процесс валидации завершен, браузер закрыт.')