from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def wait_css(driver, locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))

def wait_css_all_elements(driver, locator, timeout = 10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)))