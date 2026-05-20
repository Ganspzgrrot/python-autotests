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

@allure.feature('Оформление заказа')
class TestFullOrderFlow:
    @allure.title('Регистрация, авторизация пользователя и оформление нового заказа')
    def test_full_order_flow(self, driver):
        with allure.step('Запускаем процесс'):
            logger.info('Подготовка браузера....')
            driver.get('https://pizzeria.skillbox.cc/my-account/')
            driver.maximize_window()
            wait = WebDriverWait(driver, 10)

        #logger.info('Запущен процесс регистрации нового пользователя....')                            # Раскомментируйте, если запускаете автотест в первый раз!
        #with allure.step('Нажать кнопку "Зарегистрироваться"'):                                       #
        #    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()            #
        #with allure.step('В поле "Имя пользователя*" вписать "helmutpzh'):                            #
        #    driver.find_element(By.XPATH, "//input[@id='reg_username']").send_keys('helmutpzh')       #
        #with allure.step('В поле "Адрес почты*" вписать "helmutpzh@test.ru"'):                        #
        #    driver.find_element(By.XPATH, "//input[@id='reg_email']").send_keys(f'helmutpzh@test.ru') #
        #with allure.step('В поле "Пароль*" вписать "1234567890-"'):                                   #
        #    driver.find_element(By.XPATH, "//input[@id='reg_password']").send_keys('1234567890-')     #
        #with allure.step('Нажать кнопку "Зарегистрироваться"'):                                       #
        #    driver.find_element(By.XPATH, "//button[@name='register']").click()                       # Как только при первом запуске пройдет успешная регистрация - просьба закомментировать строки, выделенные на конце кода решеткой

        logger.info('Авторизация раннее зарегистрированного пользователя....')
        with allure.step('В поле "Имя пользователя или почта*" вписать "helmutpzh"'):
            driver.find_element(By.XPATH, "//input[@id='username']").send_keys('helmutpzh')
        with allure.step('В поле "Пароль*" вписать "1234567890-"'):
            driver.find_element(By.XPATH, "//input[@id='password']").send_keys('1234567890-')
        with allure.step('Нажать кнопку "ВОЙТИ"'):
            driver.find_element(By.XPATH, "//button[@name='login']").click()

        with allure.step('Открыть карточку товара "Пицца 4 в 1"'):
            logger.info('Процесс перехода на главную страницу и в корзину, с добавленным товаром(Пиццей 4 в 1)....'); time.sleep(1.5)
            driver.get('https://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-4-%d0%b2-1/')
        with allure.step('Нажать кнопку "В корзину"'):
            driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click(); time.sleep(1.5)
        with allure.step('Нажать кнопку "Подробнее"'):
            driver.find_element(By.XPATH, "//a[text()='Подробнее']").click()
        with allure.step('Нажать кнопку "Перейти к оплате"'):
            driver.find_element(By.XPATH, "//a[contains(text(), 'ПЕРЕЙТИ К ОПЛАТЕ')]").click(); time.sleep(1.5)

        logger.info('Процесс оформления заказа(Заполнение полей и выделение чек-боксов)....')
        with allure.step('В поле "Имя*" ввести значение "Хельмут"'):
            driver.find_element(By.XPATH, "//input[@id='billing_first_name']").clear(); driver.find_element(By.XPATH, "//input[@id='billing_first_name']").send_keys('Хельмут')
        with allure.step('В поле "Фамилия*" ввести значение "Мюллер"'):
            driver.find_element(By.XPATH, "//input[@id='billing_last_name']").clear(); driver.find_element(By.XPATH, "//input[@id='billing_last_name']").send_keys('Мюллер')
        with allure.step('В поле "Адрес*" ввести значение "Улица петрозаводской остановки дом 12"'):
            driver.find_element(By.XPATH, "//input[@id='billing_address_1']").clear(); driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys('Улица петрозаводской остановки дом 12')
        with allure.step('В поле "Город/Населенный пункт*" ввести значение "Бранденбург"'):
            driver.find_element(By.XPATH, "//input[@id='billing_city']").clear(); driver.find_element(By.XPATH, "//input[@id='billing_city']").send_keys('Бранденбург')
        with allure.step('В поле "Область*" ввести значение "Бранденбургская область"'):
            driver.find_element(By.XPATH, "//input[@id='billing_state']").clear(); driver.find_element(By.XPATH, "//input[@id='billing_state']").send_keys('Бранденбургская область')
        with allure.step('В поле "Почтовый индекс*" ввести значение "123456"'):
            driver.find_element(By.XPATH, "//input[@id='billing_postcode']").clear(); driver.find_element(By.XPATH, "//input[@id='billing_postcode']").send_keys('123456')
        with allure.step('В поле "Телефон*" ввести значение "89009009090"'):
            driver.find_element(By.XPATH, "//input[@id='billing_phone']").clear(); driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys('89009009090')
        with allure.step('Выделить чекбокс "I have read and agree to the website terms and conditions*"'):
            driver.find_element(By.XPATH, "//input[@id='terms']").click()
            driver.find_element(By.XPATH, '//button[@id="place_order"]').click()

        with allure.step('Заказ успешно создан и на экране присутствует подробная информация о заказе'):
            logger.info('Запуск процесса валидации об успешном создании и получения заказа....')
            validation_current_text = driver.find_element(By.XPATH, "//h2[text()='Заказ получен']").text
            assert 'заказ получен' == validation_current_text.lower()
            logger.info('Процесс валидации завершен, браузер закрыт.')


