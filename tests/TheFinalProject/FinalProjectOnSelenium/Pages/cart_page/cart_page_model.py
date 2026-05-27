from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css_all_elements
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.MAIN_PAGE_URL = "https://pizzeria.skillbox.cc"
        self.PIZZA_ELEMENT = "a[title='Пицца «4 в 1»']"
        self.BUTTON_ADD_TO_CART = "//button[@name='add-to-cart']"
        self.CART_BUTTON = '//*[@id="menu-item-29"]//a'
        self.PRODUCT_LIST = "td.product-name"

    def open(self):
        self.driver.get(self.MAIN_PAGE_URL)

    def click_pizza_card(self):
        wait_css(self.driver, self.PIZZA_ELEMENT).click()

    def add_to_cart(self):
        wait_xpath(self.driver, self.BUTTON_ADD_TO_CART).click()

    def click_cart_button(self):
        wait_xpath(self.driver, self.CART_BUTTON).click()

    def list_products(self):
        return wait_css_all_elements(self.driver, self.PRODUCT_LIST)
