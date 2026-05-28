import time
from selenium.webdriver.common.by import By
import allure
import logging.config
import logging
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
from tests.TheFinalProject.FinalProjectOnSelenium.Pages.checkout_page.checkout_page_model import CheckoutPage

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

@allure.feature('Оформление заказа')
class TestCheckout:
    @allure.title('Оформление заказа: пустые обязательные поля "Имя пользователя или почта*" и "Пароль*"')
    def test_checkout_validation(self, driver):
        checkout_page = CheckoutPage(driver)
        checkout_page.open_pizza_card_page()
        checkout_page.max_win()

        checkout_page.add_to_cart()
        checkout_page.click_cart_button_in_menu()

        logger.info('Начало оформления заказа....')
        checkout_page.click_go_to_payment_button()
        checkout_page.click_login_link()
        checkout_page.click_login_button()
        current_text = checkout_page.get_error_text()

        logger.info('Запускаем процесс возникновения ошибки, при отсутствии заполнения обязательных полей, будучи неавторизованным пользователем....')
        with allure.step('Появляется ошибка "Error: Имя пользователя обязательно."'):
            assert 'error: имя пользователя обязательно.' == current_text.lower()
            logger.info('Процесс валидации завершен, браузер закрыт.')

