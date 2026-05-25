import time
from selenium.webdriver.common.by import By
import allure
import logging.config
import logging
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_until

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

@allure.feature('Оформление заказа')
class TestCheckout:
    @allure.title('Оформление заказа: пустые обязательные поля "Имя пользователя или почта*" и "Пароль*"')
    def test_checkout_validation(self, driver):
        logger.info('Запускаем и настраиваем загрузку браузера....')
        with allure.step('Открыть картосчку товара "Пицца 4 в 1"'):
            driver.get('https://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-%d1%80%d0%b0%d0%b9/')
            driver.maximize_window()

        logger.info('Добавление товара и переход в корзину....')
        with allure.step('Нажать кнопку "В КОРЗИНУ"'):
            driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click(); time.sleep(1)
        with allure.step('Нажать кнопку "Корзина" в верхнем меню сайта пиццерии'):
            driver.find_element(By.XPATH, '//*[@id="menu-item-29"]//a').click()

        logger.info('Начало оформления заказа....')
        with allure.step('Нажать кнопку "Перейти к оплате"'):
            driver.find_element(By.XPATH, "//a[contains(text(), 'ПЕРЕЙТИ К ОПЛАТЕ')]").click()
        with allure.step('Нажать ссылку "Авторизуйтесь"'):
            driver.find_element(By.XPATH, "//a[text()='Авторизуйтесь']").click()
        with allure.step('Нажать кнопку "ВОЙТИ"'):
            wait_until(driver, "//button[@name='login']").click()
        wait_until(driver, '//*[@id="post-24"]//li')
        current_text = driver.find_element(By.XPATH, '//*[@id="post-24"]//li').text

        logger.info('Запускаем процесс возникновения ошибки, при отсутствии заполнения обязательных полей, будучи неавторизованным пользователем....')
        with allure.step('Появляется ошибка "Error: Имя пользователя обязательно."'):
            assert 'error: имя пользователя обязательно.' == current_text.lower()
            logger.info('Процесс валидации завершен, браузер закрыт.')

