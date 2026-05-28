from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.wait import WebDriverWait

from src import actions
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
from tests.TheFinalProject.FinalProjectOnSelenium.Pages.dropdown_menu_page.dropdown_menu_model import DropdownMenu
from selenium.webdriver.common.action_chains import ActionChains
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

@allure.feature('Выпадающее меню')
class TestDropdownMenu:
    @allure.title('Выпадающее меню: кликабельность и работоспособность кнопок "Пицца", "Десерты", "Напитки"')
    def test_dropdown_menu_with_elements(self, driver):
        dropdown_menu = DropdownMenu(driver)
        dropdown_menu.open()
        dropdown_menu.max_win()
        action = ActionChains(driver)

        dropdown_menu.cursor_move_to_menu()
        previous_url = driver.current_url
        dropdown_menu.select_pizza_item()
        cur_url = driver.current_url
        logger.info(f"Прошлый URL: {previous_url} | Текущий URL {cur_url}")
        assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/product-category/menu/pizza/"
        wait_xpath(driver, "//li[@id='menu-item-26']//a[contains(text(),'Главная')]").click()

        dropdown_menu.cursor_move_to_menu()
        previous_url = driver.current_url
        dropdown_menu.select_deserts_item()
        cur_url = driver.current_url
        logger.info(f"Прошлый URL: {previous_url} | Текущий URL {cur_url}")
        assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/product-category/menu/deserts/"
        wait_xpath(driver, "//li[@id='menu-item-26']//a[contains(text(),'Главная')]").click()

        dropdown_menu.cursor_move_to_menu()
        previous_url = driver.current_url
        dropdown_menu.select_drinks_item()
        cur_url = driver.current_url
        logger.info(f"Прошлый URL: {previous_url} | Текущий URL {cur_url}")
        assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/product-category/menu/drinks/"

