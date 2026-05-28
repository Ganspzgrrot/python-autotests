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

        checkout_page.fill_username_or_email_field('helmutpzh')
        checkout_page.fill_password_field('1234567890-')
        checkout_page.click_login_button()
        checkout_page.click_cart_button_in_menu()
        checkout_page.open_pizza_card_page()
        checkout_page.add_to_cart()
        checkout_page.press_learn_more_button()
        checkout_page.fill_coupon_code_field('GIVEMEHALYAVA')
        checkout_page.click_go_to_payment_button()
        checkout_page.click_on_link_for_enter_coupon()
        checkout_page.fill_coupon_code_field('GIVEMEHALYAVA')
        driver.find_element(By.XPATH, "//button[contains(text(),'Применить купон')]").click()
        error_text = checkout_page.get_text_code_already_applied()

        logger.info('Запускаем процесс валидации')
        with allure.step('Убедиться, что появилась ошибка при вводе уже примененного ранее промокода "Coupon code already applied!"'):
            assert "coupon code already applied!" == error_text.lower()
        logger.info('Процесс валидации завершен, браузер закрыт.')







