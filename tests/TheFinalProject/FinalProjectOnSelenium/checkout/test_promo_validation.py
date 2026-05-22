from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import pytest
from seleniumwire import webdriver


import logging.config
import logging
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
            wait = WebDriverWait(driver, 10)
            time.sleep(3)

        with allure.step('Нажать ссылку "Войти" в правом верхнем углу сайта пиццерии'):
            wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Войти')]"))).click()
        with allure.step('В поле "Имя пользователя или почта*" вписать "helmutpzh"'):
            driver.find_element(By.XPATH, "//input[@id='username']").send_keys('helmutpzh')
        with allure.step('В поле "Пароль*" вписать "1234567890-"'):
            driver.find_element(By.XPATH, "//input[@id='password']").send_keys('1234567890-')
        with allure.step('Нажать кнопку "ВОЙТИ"'):
            driver.find_element(By.XPATH, "//button[@name='login']").click()
        with allure.step('Нажать кнопку "КОРЗИНА" в меню пиццерии'):
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li[id='menu-item-29'] a"))).click()
        driver.get('https://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-4-%d0%b2-1/')
        with allure.step('Нажать кнопку "В КОРЗИНУ"'):
            driver.find_element(By.XPATH, "//button[contains(text(),'В корзину')]").click()
        with allure.step('Нажать кнопку "ПОДРОБНЕЕ" для перехода в корзину'):
            wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Подробнее')]"))).click()
        with allure.step('В поле "Введите код купона..." ввести промокод GIVEMEHALYAVA'):
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='coupon_code']"))).send_keys('GIVEMEHALYAVA')
        with allure.step('Нажать кнопку "ПРИМЕНИТЬ КУПОН" и перейти на страницу оформления заказа'):
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[value='Применить купон']"))).click()
            driver.get('https://pizzeria.skillbox.cc/checkout/')





