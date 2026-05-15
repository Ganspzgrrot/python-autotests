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

class TestAddToCart:
    def test_add_pizza_to_cart(self, driver):
        driver.get('https://pizzeria.skillbox.cc')
        logger.info('Запускаем браузер в полный экран....')
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        logger.info('Ищем и нажимаем на карточку товара "Пицца «4 в 1»"....')
        driver.find_element(By.CSS_SELECTOR, "a[title='Пицца «4 в 1»']").click()
        logger.info('Ищем и нажимаем на кнопку "Добавить в корзину"....')
        driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
        logger.info('Ищем и нажимаем на кнопку "Корзина", и осуществляем в нее переход....')
        driver.find_element(By.XPATH, '//*[@id="menu-item-29"]//a').click()
        logger.info('Получаем список всех товаров из корзины....')
        product_list = driver.find_elements(By.CSS_SELECTOR, "td.product-name")

        logger.info('Запускаем процесс валидации ненулевого количества товаров в корзине')
        assert len(product_list) > 0
        logger.info('Процесс валидации завершен, браузер закрыт.')

    def test_add_pizza_and_verify_total_amount(self, driver):
        driver.get('https://pizzeria.skillbox.cc')
        logger.info('Запускаем бразуер в полный экран....')
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        logger.info('Ищем нужные элементы, которые пригодятся для процесса валидации.....')
        driver.find_element(By.CSS_SELECTOR, "a[title='Пицца «4 в 1»']").click()
        driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click(); time.sleep(1.3)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="menu-item-29"]//a'))).click()
        input_field = driver.find_element(By.CSS_SELECTOR, "input.qty")
        summ = driver.find_element(By.CSS_SELECTOR, 'strong > span.woocommerce-Price-amount.amount > bdi')
        current_text = driver.find_element(By.CSS_SELECTOR, "td.product-price span.woocommerce-Price-amount")
        step_value = input_field.get_attribute("step")

        logger.info('Запускаем процесс валидации....')
        assert int(current_text.text[0:3]) * int(step_value) == int(summ.text[0:3])
        logger.info('Процесс валидации завершен, браузер закрыт.')