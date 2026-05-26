from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.wait import WebDriverWait

from src import actions
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
from selenium.webdriver.common.action_chains import ActionChains
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

@allure.feature('Выпадающее меню')
class TestDropdownMenu:
    @allure.title('Выпадающее меню: кликабельность и работоспособность кнопок "Пицца", "Десерты", "Напитки"')
    def test_dropdown_menu_with_elements(self, driver):
        with allure.step('Открыть главную страницу сайта Pizzeria'):
            driver.get('https://pizzeria.skillbox.cc/')
            logger.info('Запускаем браузер в полный экран....')
            driver.maximize_window()
            action = ActionChains(driver)

        with allure.step('Навести курсор мыши на дропдаун "Меню" и в выпадающем списке выбрать пункт "Пицца"'):
            dropdown_menu = wait_xpath(driver, "//a[contains(text(),'Меню')]")
            action.move_to_element(dropdown_menu).perform()
            previous_url = driver.current_url
            wait_xpath(driver, "//a[contains(text(),'Пицца')]").click()
            cur_url = driver.current_url
            logger.info(f"Прошлый URL: {previous_url} | Текущий URL {cur_url}")
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/product-category/menu/pizza/"
            wait_xpath(driver, "//li[@id='menu-item-26']//a[contains(text(),'Главная')]").click()

        with allure.step('Навести курсор мыши на дропдаун "Меню" и в выпадающем списке выбрать пункт "Десерты"'):
            dropdown_menu = wait_xpath(driver, "//a[contains(text(),'Меню')]")
            action.move_to_element(dropdown_menu).perform()
            previous_url = driver.current_url
            wait_xpath(driver, "//a[contains(text(),'Десерты')]").click()
            cur_url = driver.current_url
            logger.info(f"Прошлый URL: {previous_url} | Текущий URL {cur_url}")
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/product-category/menu/deserts/"
            wait_xpath(driver, "//li[@id='menu-item-26']//a[contains(text(),'Главная')]").click()

        with allure.step('Навести курсор мыши на дропдаун "Меню" и в выпадающем списке выбрать пункт "Напитки"'):
            dropdown_menu = wait_xpath(driver, "//a[contains(text(),'Меню')]")
            action.move_to_element(dropdown_menu).perform()
            previous_url = driver.current_url
            wait_xpath(driver, "//a[contains(text(),'Напитки')]").click()
            cur_url = driver.current_url
            logger.info(f"Прошлый URL: {previous_url} | Текущий URL {cur_url}")
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/product-category/menu/drinks/"

