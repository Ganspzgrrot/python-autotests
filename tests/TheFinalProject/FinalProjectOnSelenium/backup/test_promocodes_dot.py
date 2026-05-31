import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.feature("Промокоды")
@allure.story("Сценарий №3: Ошибка при сбое сети")
@allure.severity(allure.severity_level.CRITICAL)
def test_coupons_network_failure(driver):
    with allure.step("Открытие страницы корзины"):
        driver.get("https://pizzeria.skillbox.cc/cart/")  # Замени на свой URL

    with allure.step("Включение перехвата сетевых запросов через CDP"):
        driver.execute_cdp_cmd("Network.enable", {})
        driver.execute_cdp_cmd("Network.setRequestInterception", {
            "patterns": [
                {
                    "urlPattern": "*promocode*",
                    "interceptionStage": "HeadersReceived"
                }
            ]
        })

        def block_promocode_request(event):
            interception_id = event.get("interceptionId")
            driver.execute_cdp_cmd("Network.continueInterceptedRequest", {
                "interceptionId": interception_id,
                "errorReason": "Failed"
            })

        driver.execute_cdp_cmd("Network.requestIntercepted", block_promocode_request)

    with allure.step("Ввод промокода и отправка"):
        promo_input = driver.find_element(By.XPATH, "//input[@id='coupon_code']")
        promo_input.send_keys("GIVEMEHALYAVA")

        apply_button = driver.find_element(By.CSS_SELECTOR, "//button[contains(text(),'Применить купон')]")
        apply_button.click()

    with allure.step("Проверка отображения ошибки 'Проблема с сетью'"):
        error_message_locator = (By.CSS_SELECTOR, ".promo-error-message")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(error_message_locator)
        )

        error_text = driver.find_element(*error_message_locator).text

        assert "Ошибка соединения" in error_text, f"Ожидался текст ошибки сети, но пришло: {error_text}"