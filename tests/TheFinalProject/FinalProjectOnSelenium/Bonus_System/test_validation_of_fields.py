from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.wait import WebDriverWait
from tests.TheFinalProject.FinalProjectOnSelenium.Pages.bonus_page.bonus_page_model import BonusPage
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

class TestSocialLInks:
    def test_bonus_system(self, driver):
        bonus_page = BonusPage(driver)
        bonus_page.open()
        bonus_page.max_win()
        wait = WebDriverWait(driver, 10)

        bonus_page.enter_username('Хельмут')
        bonus_page.enter_phone('89009009090')
        bonus_page.click_submit()
        with allure.step('Сообщение об ошибке "Поле Имя обязательно для заполнения" и "Поле Телефон обязательно для заполнения"'):
            try:
                wait.until(EC.alert_is_present())
                driver.switch_to.alert.accept()
            except Exception:
                pass
            valid_text = bonus_page.get_success_message()
            assert 'Ваша карта оформлена!' == valid_text

    def test_bonus_system_validation(self, driver):
        bonus_page = BonusPage(driver)
        bonus_page.open()
        bonus_page.max_win()

        bonus_page.enter_username_without_allure_step()
        bonus_page.enter_phone_without_allure_step()
        bonus_page.click_submit()
        with allure.step('Сообщение об ошибке "Поле Телефон обязательно для заполнения"'):
            error_text_phone = bonus_page.get_error_message()
            logger.info(error_text_phone)
            assert 'Поле "Телефон" обязательно для заполнения' in error_text_phone
