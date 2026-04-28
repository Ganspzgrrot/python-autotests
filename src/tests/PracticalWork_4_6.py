import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def test_github_search_by_issue_title(driver): #PASSED
    driver.get('https://github.com/microsoft/vscode/issues')
    el = driver.find_element(By.ID, 'repository-input')
    time.sleep(2)

    el.send_keys(Keys.CONTROL, 'a'); time.sleep(0.6)
    el.send_keys(Keys.BACKSPACE); time.sleep(0.6)
    el.send_keys('in:title bug', Keys.ENTER)

    time.sleep(5)

def test_github_author_filter_bpasero(driver): #PASSED
    driver.get('https://github.com/microsoft/vscode/issues')
    time.sleep(1.4)

    el = driver.find_element(By.ID, 'repository-input'); time.sleep(0.8)
    el.send_keys(Keys.CONTROL, 'a'); time.sleep(0.8)
    el.send_keys(Keys.BACKSPACE); time.sleep(0.8)
    driver.find_element(By.CSS_SELECTOR, "[data-testid='authors-anchor-button']").click(); time.sleep(0.8)
    driver.find_element(By.CSS_SELECTOR, "[placeholder='Filter authors']").send_keys('bpasero'); time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[placeholder='Filter authors']").send_keys(Keys.ENTER)

    time.sleep(5)

def test_advanched_search_python_repositore(driver): #PASSED
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

def test_tab_zwei_DropdownList(driver): #PASSED
    driver.maximize_window(); driver.get('https://skillbox.ru/code/')
    actions = ActionChains(driver)

    time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(@class, 'programs-filter-desktop__tab')]").click(); time.sleep(0.7)
    driver.find_element(By.XPATH, "//button[contains(@class, 'ui-round-select__field') and contains(., 'Длительность')]").click(); time.sleep(0.7)
    driver.find_element(By.XPATH, "//li[contains(@class, 'ui-round-select__item') and contains(text(), 'От 6 до 12 мес.')]").click(); time.sleep(0.7)
    driver.find_element(By.XPATH, "//button[contains(., 'Тематика')]").click(); time.sleep(0.7)
    driver.find_element(By.XPATH, "//li[contains(@class, 'ui-round-select__item') and contains(., 'Airflow')]").click(); time.sleep(0.7)
    driver.find_element(By.XPATH, "//button[normalize-space()='Применить']").click(); time.sleep(0.4)
    for _ in range(0, 137, 10):
        actions.scroll_by_amount(0, 20).perform()
        time.sleep(0.01)

    time.sleep(8)

def test_hover_on_commit_chart_shows_tooltip(driver): #PASSED
    driver.maximize_window()
    driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
    actions = ActionChains(driver)
    time.sleep(2)

    el = driver.find_element(By.CSS_SELECTOR, "path.highcharts-point"); time.sleep(0.7)
    actions.move_to_element(el).perform()

    time.sleep(3.5)
