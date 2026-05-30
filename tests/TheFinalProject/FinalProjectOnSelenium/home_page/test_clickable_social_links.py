import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from tests.TheFinalProject.FinalProjectOnSelenium.Pages.home_page_page.clickable_social_links_models import ClickableSocialLinks
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
        social_links = ClickableSocialLinks(driver)
        social_links.open()
        social_links.max_win()

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
        social_links = ClickableSocialLinks(driver)
        social_links.open()
        social_links.max_win()

        social_links.validation_shares_link()
        social_links.validation_bonus_program_link()
        social_links.validation_all_products_link()
        social_links.validation_main_link()
        social_links.validation_delivery_and_payment_link()
        social_links.validation_cart_link()
        social_links.validation_my_account_link()
        social_links.validation_about_us_link()
        social_links.validation_place_order()
        social_links.validation_registration_link()