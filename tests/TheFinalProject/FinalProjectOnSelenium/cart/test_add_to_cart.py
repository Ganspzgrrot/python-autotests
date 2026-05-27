import time
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
from tests.TheFinalProject.FinalProjectOnSelenium.functions.wait_until_function_on_more_locators.wait_until_on_xpath import wait_xpath
from tests.TheFinalProject.FinalProjectOnSelenium.Pages.cart_page.cart_page_model import CartPage
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')

@allure.feature('Добавление товара в корзину')
class TestAddToCart:
    @allure.title('Проверка ненулевого количества товара в корзине')
    def test_add_pizza_to_cart(self, driver):
        cart_page = CartPage(driver)
        cart_page.open()
        cart_page.max_win()

        time.sleep(2)
        cart_page.click_pizza_card()
        cart_page.add_to_cart()

        cart_page.click_cart_button()
        product_list = cart_page.list_products()

        with allure.step('Запуск процесса валидации ненулевого количества товаров в корзине'):
            logger.info('Запускаем процесс валидации ненулевого количества товаров в корзине')
            assert len(product_list) > 0
            logger.info('Процесс валидации завершен, браузер закрыт.')

    @allure.title('Вычисление общей суммы товаров')
    def test_add_pizza_and_verify_total_amount(self, driver):
        cart_page = CartPage(driver)
        cart_page.open()
        cart_page.max_win()

        logger.info('Ищем нужные элементы, которые пригодятся для процесса валидации.....')
        cart_page.click_pizza_card()
        cart_page.add_to_cart()
        cart_page.click_cart_button()
        input_field = cart_page.product_quantity()
        summ = cart_page.total_amount()
        summ = int(summ.text[0:3])
        current_text = cart_page.product_price()

        step_value = input_field.get_attribute("step")
        current_arg = int(current_text.text[0:3])
        step_value = int(step_value)

        with allure.step('Проверка вычисления общей суммы всех товаров'):
            logger.info('Запускаем процесс валидации....')
            assert current_arg * step_value == summ
            logger.info('Процесс валидации завершен, браузер закрыт.')

    @allure.title('Применение 10% скидки при вводе промокода GIVEMEHALYAVA')
    def test_cart_promo_code_discount(self, driver):
        cart_page = CartPage(driver)
        cart_page.open()
        cart_page.max_win()

        logger.info('Добавляем товары в корзину для проверки работоспобности вычисления 10% скидки с применением промокода GIVMEHALYAVA....')
        cart_page.click_pizza_card()
        cart_page.clear_and_paste_value_in_field('3')
        cart_page.add_to_cart()
        cart_page.click_cart_button()

        cart_page.coupon_application('GIVEMEHALYAVA')

        with allure.step("Подсчитываем корректное применение 10% скидки ко всем товарам по промокоду GIVEMEHALYAVA"):
            logger.info('Подсчитываем корректное применение 10% скидки ко всем товарам по промокоду GIVEMEHALYAVA....')
            total_cost = driver.find_element(By.CSS_SELECTOR, "tr.cart-subtotal > td > span.woocommerce-Price-amount.amount > bdi").text[0:4]
            total_discount_price = float(int(total_cost[0:4])) * 0.9

        logger.info('Запускаем процесс валидации применения 10% скидки по промокоду GIVEHALYAVA')
        assert int(float(int(total_cost)) * 0.9) == int(total_discount_price)
        logger.info('Процесс валидации завершен, браузер закрыт.')

    @allure.title('Применение несуществующего промокода DC120')
    def test_cart_promo_code_dont_discount(self, driver):
        cart_page = CartPage(driver)
        with allure.step('Открытие главной страницы пиццерии https://pizzeria.skillbox.cc'):
            cart_page.open()
            cart_page.max_win()

        cart_page.click_pizza_card()
        cart_page.clear_and_paste_value_in_field('3')
        cart_page.add_to_cart()
        cart_page.click_cart_button()

        with allure.step('Применяем купон: в поле для ввода купона вписать значение "DC120" и нажать кнопку "применить купон'):
            logger.info('Применяем купон....')
            driver.find_element(By.XPATH, "//input[@id='coupon_code']").send_keys('DC120')
            driver.find_element(By.XPATH, "//button[@name='apply_coupon']").click(); time.sleep(1.3)

        with allure.step('Запускаем процесс валидации ошибки при применении 10% скидки по промокоду DC120'):
            logger.info('Запускаем процесс валидации ошибки при применении 10% скидки по промокоду DC120')
            error_validate = driver.find_element(By.XPATH, "//li[contains(text(), 'Неверный купон.')]")
            assert error_validate.text == 'Неверный купон.'
            logger.info('Процесс валидации завершен, браузер закрыт.')
