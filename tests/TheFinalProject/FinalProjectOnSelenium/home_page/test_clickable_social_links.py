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

class TestSocialLInks:
    def test_click_social_links(self, driver):
        with allure.step('Отрыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            driver.get("https://pizzeria.skillbox.cc")
            wait = WebDriverWait(driver, 10)
        time.sleep(3)
        links = [
            ("Facebook", "//a[normalize-space()='Facebook']", "facebook.com"),
            ("VK", "//a[contains(text(),'ВКонтакте')]", "vk.com"),
            ("Instagram", "//a[normalize-space()='Instagram']", "instagram.com")
        ]
        for name, locator, expected_domain in links:
            element = driver.find_element(By.XPATH, locator)
            href = element.get_attribute('href')
            assert expected_domain in href, f"Ошибка в ссылке {name}: {href}"

