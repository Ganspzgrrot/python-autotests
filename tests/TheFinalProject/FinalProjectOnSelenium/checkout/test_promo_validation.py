import time
from selenium.webdriver.common.by import By
import allure
import logging.config
import logging
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_css_selector import wait_css

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

@allure.feature("Валидация промокода")
class TestPromoValidation:
    @allure.title('Поведение системы при вводе некорректного промокода')
    def test_invalid_promo_blocked(self, driver):
        with allure.step('Открыть карточку товара(Пицца 4 в 1)'):
            driver.get('https://pizzeria.skillbox.cc/')
            logger.info('Запускаем браузер в полный экран....')
            driver.maximize_window()

            time.sleep(3)

        with allure.step('Нажать ссылку "Войти" в правом верхнем углу сайта пиццерии'):
            wait_xpath(driver, "//a[contains(text(),'Войти')]").click()
        with allure.step('В поле "Имя пользователя или почта*" вписать "helmutpzh"'):
            driver.find_element(By.XPATH, "//input[@id='username']").send_keys('helmutpzh')
        with allure.step('В поле "Пароль*" вписать "1234567890-"'):
            driver.find_element(By.XPATH, "//input[@id='password']").send_keys('1234567890-')
        with allure.step('Нажать кнопку "ВОЙТИ"'):
            driver.find_element(By.XPATH, "//button[@name='login']").click()
        with allure.step('Нажать кнопку "КОРЗИНА" в меню пиццерии'):
            wait_css(driver, "li[id='menu-item-29'] a").click()
        driver.get('https://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-4-%d0%b2-1/')
        with allure.step('Нажать кнопку "В КОРЗИНУ"'):
            driver.find_element(By.XPATH, "//button[contains(text(),'В корзину')]").click()
        with allure.step('Нажать кнопку "ПОДРОБНЕЕ" для перехода в корзину'):
            wait_xpath(driver, "//a[contains(text(),'Подробнее')]").click()
        with allure.step('В поле "Введите код купона..." ввести промокод GIVEMEHALYAVA'):
            wait_xpath(driver, "//input[@id='coupon_code']").send_keys('GIVEMEHALYAVA')
            wait_xpath(driver, "//a[contains(text(),'ПЕРЕЙТИ К ОПЛАТЕ')]").click()

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







