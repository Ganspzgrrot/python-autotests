from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def wait_until(driver, locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator)))