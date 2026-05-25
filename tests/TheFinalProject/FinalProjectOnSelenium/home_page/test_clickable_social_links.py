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

@allure.feature('Кликабельность и работоспособность всех ссылок на сайта Pizzeria')
class TestSocialLInks:
    @allure.title('Подвал сайта: Кликабельность и работоспособность ссылок под блоком "Контактная информация"')
    def test_click_social_links(self, driver):
        with allure.step('Отрыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            driver.get("https://pizzeria.skillbox.cc")
            wait = WebDriverWait(driver, 10)
            driver.maximize_window()

        links = [
            ("Facebook", "//a[normalize-space()='Facebook']", "facebook.com"),
            ("VK", "//a[contains(text(),'ВКонтакте')]", "vk.com"),
            ("Instagram", "//a[normalize-space()='Instagram']", "instagram.com")
        ]
        for name, locator, expected_domain in links:
            element = driver.find_element(By.XPATH, locator)
            href = element.get_attribute('href')
            assert expected_domain in href, f"Ошибка в ссылке {name}: {href}"
    @allure.title('Подвал сайта: Кликабельность и работоспособность ссылок под блоком "Страницы сайта"')
    def test_click_all_links_in_basement(self, driver):
        with allure.step('Отрыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            driver.get("https://pizzeria.skillbox.cc")
            wait = WebDriverWait(driver, 10)

        with allure.step('Нажать ссылку "Акции"'):
            previous_url = driver.current_url
            driver.find_element(By.XPATH, "//li[@class='page_item page-item-394']//a[contains(text(),'Акции')]").click()
            cur_url = driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url
            driver.get('https://pizzeria.skillbox.cc/')
        with allure.step('Нажать кнопку "Бонусная программа"'):
            previous_url = driver.current_url
            driver.find_element(By.XPATH, "//li[@class='page_item page-item-359']//a[contains(text(),'Бонусная программа')]").click()
            cur_url = driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url
            driver.get('https://pizzeria.skillbox.cc/')
        with allure.step('Нажать кнопку "Все товары"'):
            previous_url = driver.current_url
            driver.find_element(By.XPATH, "//a[contains(text(),'Все товары')]").click()
            cur_url = driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url
            driver.get('https://pizzeria.skillbox.cc/')
        with allure.step('Нажать кнопку "Главная"'):
            previous_url = driver.current_url
            driver.find_element(By.XPATH, "//li[@class='page_item page-item-39 current_page_item']//a[contains(text(),'Главная')]").click()
            cur_url = driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url == cur_url
            driver.get('https://pizzeria.skillbox.cc/')
        with allure.step('Нажать кнопку "Доставка и оплата"'):
            previous_url = driver.current_url
            driver.find_element(By.XPATH, "//li[@class='page_item page-item-376']//a[contains(text(),'Доставка и оплата')]").click()
            cur_url = driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url
            driver.get('https://pizzeria.skillbox.cc/')
        with allure.step('Нажать кнопку "Корзина"'):
            previous_url = driver.current_url
            driver.find_element(By.XPATH, "//li[@class='page_item page-item-20']//a[contains(text(),'Корзина')]").click()
            cur_url = driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url
            driver.get('https://pizzeria.skillbox.cc/')
        with allure.step('Нажать кнопку "Мой аккаунт"'):
            previous_url = driver.current_url
            driver.find_element(By.XPATH, "//li[@class='page_item page-item-22']//a[contains(text(),'Мой аккаунт')]").click()
            cur_url = driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url
            driver.get('https://pizzeria.skillbox.cc/')
        with allure.step('Нажать кнопку "О нас"'):
            previous_url = driver.current_url
            driver.find_element(By.XPATH, "//li[@class='page_item page-item-378']//a[contains(text(),'О нас')]").click()
            cur_url = driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url
            driver.get('https://pizzeria.skillbox.cc/')
        with allure.step('Нажать кнопку "Оформление заказа"'):
            previous_url = driver.current_url
            driver.find_element(By.CSS_SELECTOR, "li[class='page_item page-item-24'] a").click()
            cur_url = driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url
            driver.get('https://pizzeria.skillbox.cc/')
        with allure.step('Нажать кнопку "Регистрация"'):
            previous_url = driver.current_url
            driver.find_element(By.XPATH, "//a[contains(text(),'Регистрация')]").click()
            cur_url = driver.current_url
            logger.info(f'All URL -> ({previous_url} | {cur_url})')
            assert previous_url != cur_url
            driver.get('https://pizzeria.skillbox.cc/')