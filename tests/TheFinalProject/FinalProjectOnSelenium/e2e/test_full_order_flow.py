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


class TestFullOrderFlow:
    def test_full_order_flow(self, driver):
        logger.info('Подготовка браузера....')
        driver.get('https://pizzeria.skillbox.cc/my-account/')
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        timestamp = time.time()

        #logger.info('Запущен процесс регистрации нового пользователя....')                         # Раскомментируйте, если запускаете автотест в первый раз!
        #driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()             #
        #driver.find_element(By.XPATH, "//input[@id='reg_username']").send_keys('helmutpzh')        #
        #driver.find_element(By.XPATH, "//input[@id='reg_email']").send_keys(f'{timestamp}@test.ru')#
        #driver.find_element(By.XPATH, "//input[@id='reg_password']").send_keys('1234567890-')      #
        #driver.find_element(By.XPATH, "//button[@name='register']").click()                        # Как только при первом запуске пройдет успешная регистрация - просьба закомментировать строки, выделенные на конце кода решеткой

        logger.info('Авторизация раннее зарегистрированного пользователя....')
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys('helmutpzh')
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys('1234567890-')
        driver.find_element(By.XPATH, "//button[@name='login']").click()

        logger.info('Процесс перехода на главную страницу и в корзину, с добавленным товаром(Пиццей 4 в 1)....'); time.sleep(1.5)
        driver.get('https://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-4-%d0%b2-1/')
        driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click(); time.sleep(1.5)
        driver.find_element(By.XPATH, "//a[text()='Подробнее']").click()
        driver.find_element(By.XPATH, "//a[contains(text(), 'ПЕРЕЙТИ К ОПЛАТЕ')]").click(); time.sleep(1.5)

        logger.info('Процесс оформления заказа(Заполнение полей и выделение чек-боксов)....')
        driver.find_element(By.XPATH, "//input[@id='billing_first_name']").clear(); driver.find_element(By.XPATH, "//input[@id='billing_first_name']").send_keys('Хельмут')
        driver.find_element(By.XPATH, "//input[@id='billing_last_name']").clear(); driver.find_element(By.XPATH, "//input[@id='billing_last_name']").send_keys('Мюллер')
        driver.find_element(By.XPATH, "//input[@id='billing_address_1']").clear(); driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys('Улица петрозаводской остановки до 12')
        driver.find_element(By.XPATH, "//input[@id='billing_city']").clear(); driver.find_element(By.XPATH, "//input[@id='billing_city']").send_keys('Бранденбург')
        driver.find_element(By.XPATH, "//input[@id='billing_state']").clear(); driver.find_element(By.XPATH, "//input[@id='billing_state']").send_keys('Бранденбургская область')
        driver.find_element(By.XPATH, "//input[@id='billing_postcode']").clear(); driver.find_element(By.XPATH, "//input[@id='billing_postcode']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@id='terms']").click()
        driver.find_element(By.XPATH, '//button[@id="place_order"]').click()

        logger.info('Запуск процесса валидации об успешном создании и получения заказа....')
        validation_current_text = driver.find_element(By.XPATH, "//h2[text()='Заказ получен']").text
        assert 'заказ получен' == validation_current_text.lower()
        logger.info('Процесс валидации завершен, браузер закрыт.')

        logger.info('')


