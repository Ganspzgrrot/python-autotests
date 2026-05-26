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

@allure.feature('Категория товаров')
class TestDropdownMenu:
    @allure.title('Категория товаров: кликабельность и работоспособность кнопок "Десерты", "Каталог", "Меню", "Напитки"')
    def test_dropdown_menu_with_elements(self, driver):
        with allure.step('Открыть страницу по URL https://pizzeria.skillbox.cc/product-category/menu/pizza/'):
            driver.get('https://pizzeria.skillbox.cc/product-category/menu/pizza/')
            logger.info('Запускаем браузер в полный экран....')
            driver.maximize_window()

        with allure.step('Нажать кнопку "Десерты"'):
            previous_url = driver.current_url
            wait_xpath(driver, "//li[@class='cat-item cat-item-31']//a[contains(text(),'Десерты')]").click()
            cur_url = driver.current_url
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/product-category/menu/deserts/"
            driver.get('https://pizzeria.skillbox.cc/product-category/menu/pizza/')
        with allure.step('Нажать кнопку "Каталог"'):
            previous_url = driver.current_url
            wait_xpath(driver, "//a[contains(text(),'Каталог')]").click()
            cur_url = driver.current_url
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/product-category/catalog/"
            driver.get('https://pizzeria.skillbox.cc/product-category/menu/pizza/')
        with allure.step('Нажать кнопку "Меню"'):
            previous_url = driver.current_url
            wait_xpath(driver, "//li[@class='cat-item cat-item-29']//a[contains(text(),'Меню')]").click()
            cur_url = driver.current_url
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/product-category/menu/"
            driver.get('https://pizzeria.skillbox.cc/product-category/menu/pizza/')
        with allure.step('Нажать кнопку "Напитки"'):
            previous_url = driver.current_url
            wait_xpath(driver, "//li[@class='cat-item cat-item-32']//a[contains(text(),'Напитки')]").click()
            cur_url = driver.current_url
            assert previous_url != cur_url and cur_url == "https://pizzeria.skillbox.cc/product-category/menu/drinks/"
