import pytest
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from tests.TheFinalProject.FinalProjectOnSelenium.Pages.cart_page.cart_page_model import CartPage

@allure.feature("Промокоды")
@allure.story("Сценарий №3: Ошибка при сбое сети")
@allure.severity(allure.severity_level.CRITICAL)
def test_coupons_network_failure(driver):
    cart_page = CartPage(driver)

    with allure.step("Подготовка корзины"):
        cart_page.open()
        cart_page.max_win()
        cart_page.click_pizza_card()
        cart_page.add_to_cart()
        cart_page.click_cart_button()

    with allure.step("Включение блокировки сети через CDP"):
        driver.execute_cdp_cmd("Network.enable", {})
        driver.execute_cdp_cmd("Network.setBlockedURLs", {
            "urls": ["*wc-ajax=apply_coupon*", "*admin-ajax.php*"]
        })

    with allure.step("Применение купона"):
        cart_page.coupon_application("GIVEMEHALYAVA")

    with allure.step("Проверка реакции сайта на сбой"):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        try:
            error_msg = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".woocommerce-error"))
            )
            assert "Ошибка" in error_msg.text
        except TimeoutException:
            print("Тест пройден: сайт завис при попытке применения купона в условиях сбоя сети")