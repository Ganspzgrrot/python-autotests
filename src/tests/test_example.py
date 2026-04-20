import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class PracticalWork:
    def test_github_search_by_issue_title(self, driver):
        driver.get('https://github.com/microsoft/vscode/issues')
        el = driver.find_element(By.ID, 'repository-input')
        time.sleep(2)
        el.send_keys(Keys.CONTROL, 'a')
        time.sleep(0.6)
        el.send_keys(Keys.BACKSPACE)
        time.sleep(0.6)

        el.send_keys('in:title bug', Keys.ENTER)
        time.sleep(2)
