import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from tests.TheFinalProject.FinalProjectOnSelenium.Pages.home_page_page import product_selection_models
from tests.TheFinalProject.FinalProjectOnSelenium.Pages.home_page_page.product_selection_models import ProductSelection
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
        product_selections = ProductSelection(driver)
        product_selections.open()
        product_selections.max_win()

        product_selections.pizza_card_text_validation()
