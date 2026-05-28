import time
from selenium.webdriver.common.by import By
import allure
import logging.config
import logging
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css
from tests.TheFinalProject.FinalProjectOnSelenium.Pages.checkout_page.checkout_page_model import CheckoutPage

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

@allure.feature("Валидация промокода")
class TestPromoValidation:
    @allure.title('Поведение системы при вводе некорректного промокода')
    def test_invalid_promo_blocked(self, driver):
        checkout_page = CheckoutPage(driver)
        checkout_page.open_login_page()
        checkout_page.max_win()
        with allure.step('В поле "Имя пользователя или почта*" вписать "helmutpzh"'):
            driver.find_element(By.XPATH, "//input[@id='username']").send_keys('helmutpzh')
        with allure.step('В поле "Пароль*" вписать "1234567890-"'):
            driver.find_element(By.XPATH, "//input[@id='password']").send_keys('1234567890-')
        checkout_page.click_login_button()
        checkout_page.click_cart_button_in_menu()
        checkout_page.open_pizza_card_page()
        checkout_page.add_to_cart()
        with allure.step('Нажать кнопку "ПОДРОБНЕЕ" для перехода в корзину'):
            wait_xpath(driver, "//a[contains(text(),'Подробнее')]").click()
        with allure.step('В поле "Введите код купона..." ввести промокод GIVEMEHALYAVA'):
            wait_xpath(driver, "//input[@id='coupon_code']").send_keys('GIVEMEHALYAVA')
            checkout_page.click_go_to_payment_button()

        with allure.step('На форме оформления заказа нажать кнопку "Нажмите для ввода купона"'):
            wait_xpath(driver, "//a[contains(text(),'Нажмите для ввода купона')]").click()
            input_promo_code = wait_xpath(driver, "//input[@id='coupon_code']")
            input_promo_code.send_keys('GIVEMEHALYAVA')
            driver.find_element(By.XPATH, "//button[contains(text(),'Применить купон')]").click()
            error_text = wait_xpath(driver, "//li[normalize-space()='Coupon code already applied!']").text
        logger.info('Запускаем процесс валидации')
        with allure.step('Убедиться, что появилась ошибка при вводе уже примененного ранее промокода "Coupon code already applied!"'):
            assert "coupon code already applied!" == error_text.lower()
        logger.info('Процесс валидации завершен, браузер закрыт.')







