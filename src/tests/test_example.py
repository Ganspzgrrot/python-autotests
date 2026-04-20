import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def test_github_search_by_issue_title(driver):
    driver.get('https://github.com/microsoft/vscode/issues')
    el = driver.find_element(By.ID, 'repository-input')
    time.sleep(2)

    el.send_keys(Keys.CONTROL, 'a'); time.sleep(0.6)
    el.send_keys(Keys.BACKSPACE); time.sleep(0.6)
    el.send_keys('in:title bug', Keys.ENTER)

    time.sleep(5)

def test_github_author_filter_bpasero(driver):
    driver.get('https://github.com/microsoft/vscode/issues')
    time.sleep(1.4)

    el = driver.find_element(By.ID, 'repository-input'); time.sleep(0.8)
    el.send_keys(Keys.CONTROL, 'a'); time.sleep(0.8)
    el.send_keys(Keys.BACKSPACE); time.sleep(0.8)
    driver.find_element(By.CSS_SELECTOR, "[data-testid='authors-anchor-button']").click(); time.sleep(0.8)
    driver.find_element(By.CSS_SELECTOR, "[placeholder='Filter authors']").send_keys('bpasero'); time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[placeholder='Filter authors']").send_keys(Keys.ENTER)

    time.sleep(5)

def test_advanched_search_python_repositore(driver):
    driver.get('https://github.com/search/advanced')
    actions = ActionChains(driver)
    time.sleep(2)

    Select(driver.find_element(By.ID, 'search_language')).select_by_visible_text('Python'); time.sleep(0.6)
    search_stars = driver.find_element(By.ID, 'search_stars'); search_stars.click(); search_stars.send_keys('>20000'); time.sleep(0.6)
    for _ in range(0, 500, 20):
        actions.scroll_by_amount(0, 20).perform()
        time.sleep(0.1)
    search_filename = driver.find_element(By.ID, 'search_filename'); search_filename.send_keys('environment.yml'); time.sleep(0.5); search_filename.send_keys(Keys.ENTER)

    time.sleep(6)
