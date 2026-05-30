import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from tests.TheFinalProject.FinalProjectOnSelenium.Pages.e2e_page.e2e_models import E2E
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
        e2e_page = E2E(driver)
        e2e_page.open()
        e2e_page.max_win()

        #e2e_page.user_registration() #Если понадобится регистрация - просьба раскомментировать эту строку

        e2e_page.login()
        e2e_page.add_product_in_cart()
        e2e_page.making_an_order()

        with allure.step('Заказ успешно создан и на экране присутствует подробная информация о заказе'):
            logger.info('Запуск процесса валидации об успешном создании и получения заказа....')
            validation_current_text = driver.find_element(By.XPATH, "//h2[text()='Заказ получен']").text
            assert 'заказ получен' == validation_current_text.lower()
            logger.info('Процесс валидации завершен, браузер закрыт.')


