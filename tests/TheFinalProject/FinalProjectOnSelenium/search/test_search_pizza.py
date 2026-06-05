import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
from tests.TheFinalProject.FinalProjectOnSelenium.Pages.search_pizza_page.search_pizza_models import SearchPizza
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

class TestSearchPizza:
    @allure.title("Поиск: соответствие карточек товаров поисковому запросу")
    def test_search_pizza_and_validate(self, driver):
        search_pizza = SearchPizza(driver)
        search_pizza.open()
        search_pizza.max_win()

        search_pizza.click_pizza_rai()
        current_text_title = search_pizza.pizza_rai_text()
        current_text_on_navigation_bar = search_pizza.pizza_rai_text_on_navigation_bar()

        logger.info('Запускаем процесс валидации соответствия пиццы раннее веденному запросу...')
        assert 'рай' in current_text_title
        assert 'рай' in current_text_on_navigation_bar
        logger.info('Процесс валидации завершен, браузер закрыт.')