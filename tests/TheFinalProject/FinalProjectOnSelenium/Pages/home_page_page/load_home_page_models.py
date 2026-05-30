from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css_all_elements
from selenium.webdriver.common.action_chains import ActionChains
import allure
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')
from selenium.webdriver.common.by import By

class LoadHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.MAIN_PAGE_URL = "https://pizzeria.skillbox.cc"

    def open(self):
        with allure.step('Отрыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            self.driver.get(self.MAIN_PAGE_URL)
    def max_win(self):
        self.driver.maximize_window()

