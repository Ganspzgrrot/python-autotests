import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

class TestCheckout:
    def test_checkout_validation(self, driver):
        driver.get('https://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-%d1%80%d0%b0%d0%b9/')
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        logger.info('Добавление товара и переход в корзину....')
        driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click(); time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="menu-item-29"]//a').click()

        logger.info('Начало оформления заказа....')
        driver.find_element(By.XPATH, "//a[contains(text(), 'ПЕРЕЙТИ К ОПЛАТЕ')]").click()
        driver.find_element(By.XPATH, "//a[text()='Авторизуйтесь']").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@name='login']"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="post-24"]//li')))
        current_text = driver.find_element(By.XPATH, '//*[@id="post-24"]//li').text

        logger.info('Запускаем процесс валидного возникновения ошибки, при отсутствии заполнения обязательных полей, будучи неавторизованным пользователем....')
        assert 'error: имя пользователя обязательно.' == current_text.lower()
        logger.info('Процесс валидации завершен, браузер закрыт.')