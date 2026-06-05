from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.wait import WebDriverWait

from src import actions
from tests.TheFinalProject.FinalProjectOnSelenium import dropdown_menu
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
from tests.TheFinalProject.FinalProjectOnSelenium.Pages.dropdown_menu_page.product_categories_models import DropdownMenu
from selenium.webdriver.common.action_chains import ActionChains
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

@allure.feature('Категория товаров')
class TestDropdownMenu:
    @allure.title('Категория товаров: кликабельность и работоспособность кнопок "Десерты", "Каталог", "Меню", "Напитки"')
    def test_dropdown_menu_with_elements(self, driver):
        dropdown_menu = DropdownMenu(driver)
        with allure.step('Открыть страницу по URL https://pizzeria.skillbox.cc/product-category/menu/pizza/'):
            dropdown_menu.open()
            dropdown_menu.open()

        with allure.step('Нажать кнопку "Десерты"'):
            dropdown_menu.click_and_validate_item_deserts()
        with allure.step('Нажать кнопку "Каталог"'):
            dropdown_menu.click_and_validate_item_catalog()
        with allure.step('Нажать кнопку "Меню"'):
            dropdown_menu.click_and_validate_item_menu()
        with allure.step('Нажать кнопку "Напитки"'):
            dropdown_menu.click_and_validate_item_drinks()
            