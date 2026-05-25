import time
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_until
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

@allure.feature('Добавление товара в корзину')
class TestAddToCart:
    @allure.title('Проверка ненулевого количества товара в корзине')
    def test_add_pizza_to_cart(self, driver):
        with allure.step('Открыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            driver.get('https://pizzeria.skillbox.cc')
            logger.info('Запускаем браузер в полный экран....')
            driver.maximize_window()
            wait = WebDriverWait(driver, 10)

        with allure.step('Нажать на карточку товара'):
            logger.info('Ищем и нажимаем на карточку товара "Пицца «4 в 1»"....')
            driver.find_element(By.CSS_SELECTOR, "a[title='Пицца «4 в 1»']").click()
        with allure.step('Нажать на кнопку "Добавить в корзину"'):
            logger.info('Ищем и нажимаем на кнопку "Добавить в корзину"....')
            driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
        with allure.step('Нажать на кнопку "Корзина" в меню сайта пиццерии'):
            logger.info('Ищем и нажимаем на кнопку "Корзина", и осуществляем в нее переход....'); time.sleep(1.5)
            driver.find_element(By.XPATH, '//*[@id="menu-item-29"]//a').click()
            logger.info('Получаем список всех товаров из корзины....')
            product_list = driver.find_elements(By.CSS_SELECTOR, "td.product-name")

        with allure.step('Запуск процесса валидации ненулевого количества товаров в корзине'):
            logger.info('Запускаем процесс валидации ненулевого количества товаров в корзине')
            assert len(product_list) > 0
            logger.info('Процесс валидации завершен, браузер закрыт.')

    @allure.title('Вычисление общей суммы товаров')
    def test_add_pizza_and_verify_total_amount(self, driver):
        with allure.step('Открыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            driver.get('https://pizzeria.skillbox.cc')
            logger.info('Запускаем браузер в полный экран....')
            driver.maximize_window()
            wait = WebDriverWait(driver, 10)

        logger.info('Ищем нужные элементы, которые пригодятся для процесса валидации.....')
        with allure.step('Нажать на карточку товара "Пицца 4 в 1"'):
            driver.find_element(By.CSS_SELECTOR, "a[title='Пицца «4 в 1»']").click()
        with allure.step('Нажать на кнопку "Добавить в корзину"'):
            driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click(); time.sleep(1.3)
        with allure.step('Нажать на кнопку "Корзина" в меню сайта пиццерии'):
            wait_until(driver,'//*[@id="menu-item-29"]//a').click()
        input_field = driver.find_element(By.CSS_SELECTOR, "input.qty")
        summ = driver.find_element(By.CSS_SELECTOR, 'strong > span.woocommerce-Price-amount.amount > bdi')
        current_text = driver.find_element(By.CSS_SELECTOR, "td.product-price span.woocommerce-Price-amount")
        step_value = input_field.get_attribute("step")

        with allure.step('Проверка вычисления общей суммы всех товаров'):
            logger.info('Запускаем процесс валидации....')
            assert int(current_text.text[0:3]) * int(step_value) == int(summ.text[0:3])
            logger.info('Процесс валидации завершен, браузер закрыт.')

    @allure.title('Применение 10% скидки при вводе промокода GIVEMEHALYAVA')
    def test_cart_promo_code_discount(self, driver):
        with allure.step('Открыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            driver.get('https://pizzeria.skillbox.cc')
            logger.info('Запускаем браузер в полный экран....')
            driver.maximize_window()
            wait = WebDriverWait(driver, 10)

        logger.info('Добавляем товары в корзину для проверки работоспобности вычисления 10% скидки с применением промокода GIVMEHALYAVA....')
        with allure.step('Нажать на карточку товара "Пицца 4 в 1"'):
            driver.find_element(By.CSS_SELECTOR, "a[title='Пицца «4 в 1»']").click()
        with allure.step('Очистить поле и выставить количество товаров 3'):
            driver.find_element(By.XPATH, "//input[@name='quantity']").clear()
            driver.find_element(By.XPATH, "//input[@name='quantity']").send_keys('3')
        with allure.step('Нажать на кнопку "Добавить в корзину и перейти на страницу корзины, через кнопку "Корзина" в меню страницы'):
            driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click(); time.sleep(1.3)
            wait_until(driver,'//*[@id="menu-item-29"]//a').click()

        with allure.step('Применение купона: в поле для ввода купона ввести промокод GIVEMEHALYAVA и нажать кнопку "Применить купон"'):
            logger.info('Применяем купон....')
            driver.find_element(By.XPATH, "//input[@id='coupon_code']").send_keys('GIVEMEHALYAVA')
            driver.find_element(By.XPATH, "//button[@name='apply_coupon']").click()

        with allure.step("Подсчитываем корректное применение 10% скидки ко всем товарам по промокоду GIVEMEHALYAVA"):
            logger.info('Подсчитываем корректное применение 10% скидки ко всем товарам по промокоду GIVEMEHALYAVA....')
            total_cost = driver.find_element(By.CSS_SELECTOR, "tr.cart-subtotal > td > span.woocommerce-Price-amount.amount > bdi").text[0:4]
            total_discount_price = float(int(total_cost[0:4])) * 0.9

        logger.info('Запускаем процесс валидации применения 10% скидки по промокоду GIVEHALYAVA')
        assert int(float(int(total_cost)) * 0.9) == int(total_discount_price)
        logger.info('Процесс валидации завершен, браузер закрыт.')

    @allure.title('Применение несуществующего промокода DC120')
    def test_cart_promo_code_dont_discount(self, driver):
        with allure.step('Открытие главной страницы пиццерии https://pizzeria.skillbox.cc'):
            driver.get('https://pizzeria.skillbox.cc')
            logger.info('Запускаем браузер в полный экран....')
            driver.maximize_window()
            wait = WebDriverWait(driver, 10)

        logger.info('Добавляем товары в корзину для проверки работоспобности вычисления 10% скидки с применением промокода DC120....')
        with allure.step('Нажать на карточку товара "Пицца 4 в 1"'):
            driver.find_element(By.CSS_SELECTOR, "a[title='Пицца «4 в 1»']").click()
        with allure.step('Очистить поле и выставить количество товаров 3'):
            driver.find_element(By.XPATH, "//input[@name='quantity']").clear()
            driver.find_element(By.XPATH, "//input[@name='quantity']").send_keys('3')
        with allure.step('Нажать кнопку "Добавить в корзину" и перейти в корзину через кнопку "Корзина" в меню страницы'):
            driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click(); time.sleep(1.3)
            wait_until(driver, '//*[@id="menu-item-29"]//a').click()

        with allure.step('Применяем купон: в поле для ввода купона вписать значение "DC120" и нажать кнопку "применить купон'):
            logger.info('Применяем купон....')
            driver.find_element(By.XPATH, "//input[@id='coupon_code']").send_keys('DC120')
            driver.find_element(By.XPATH, "//button[@name='apply_coupon']").click(); time.sleep(1.3)

        with allure.step('Запускаем процесс валидации ошибки при применении 10% скидки по промокоду DC120'):
            logger.info('Запускаем процесс валидации ошибки при применении 10% скидки по промокоду DC120')
            error_validate = driver.find_element(By.XPATH, "//li[contains(text(), 'Неверный купон.')]")
            assert error_validate.text == 'Неверный купон.'
            logger.info('Процесс валидации завершен, браузер закрыт.')
