import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def test_github_search_by_issue_title(driver): #PASSED
    driver.get('https://github.com/microsoft/vscode/issues')
    el = driver.find_element(By.ID, 'repository-input')
    time.sleep(0.5)

    el.send_keys(Keys.CONTROL, 'a')
    el.send_keys(Keys.BACKSPACE)
    el.send_keys('in:title bug', Keys.ENTER)


def test_github_author_filter_bpasero(driver): #PASSED
    driver.get('https://github.com/microsoft/vscode/issues')

    el = driver.find_element(By.ID, 'repository-input')
    el.send_keys(Keys.CONTROL, 'a')
    el.send_keys(Keys.BACKSPACE)
    driver.find_element(By.CSS_SELECTOR, "[data-testid='authors-anchor-button']").click()
    driver.find_element(By.CSS_SELECTOR, "[placeholder='Filter authors']").send_keys('bpasero')
    driver.find_element(By.CSS_SELECTOR, "[placeholder='Filter authors']").send_keys(Keys.ENTER)


def test_advanched_search_python_repositore(driver): #PASSED
    driver.get('https://github.com/search/advanced')
    actions = ActionChains(driver)

    Select(driver.find_element(By.ID, 'search_language')).select_by_visible_text('Python')
    search_stars = driver.find_element(By.ID, 'search_stars'); search_stars.click(); search_stars.send_keys('>20000')
    for _ in range(0, 500, 20):
        actions.scroll_by_amount(0, 20).perform()
        time.sleep(0.001)
    search_filename = driver.find_element(By.ID, 'search_filename'); search_filename.send_keys('environment.yml'); search_filename.send_keys(Keys.ENTER)

def test_tab_zwei_DropdownList(driver): #PASSED
    driver.maximize_window(); driver.get('https://skillbox.ru/code/')
    actions = ActionChains(driver)

    driver.find_element(By.XPATH, "//button[contains(@class, 'programs-filter-desktop__tab')]").click()
    driver.find_element(By.XPATH, "//button[contains(@class, 'ui-round-select__field') and contains(., 'Длительность')]").click()
    driver.find_element(By.XPATH, "//li[contains(@class, 'ui-round-select__item') and contains(text(), 'От 6 до 12 мес.')]").click();
    driver.find_element(By.XPATH, "//button[contains(., 'Тематика')]").click()
    driver.find_element(By.XPATH, "//li[contains(@class, 'ui-round-select__item') and contains(., 'Airflow')]").click()
    driver.find_element(By.XPATH, "//button[normalize-space()='Применить']").click()
    for _ in range(0, 137, 10):
        actions.scroll_by_amount(0, 20).perform()
        time.sleep(0.001)

def test_hover_on_commit_chart_shows_tooltip(driver): #PASSED
    driver.maximize_window()
    driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
    actions = ActionChains(driver)

    el = driver.find_element(By.CSS_SELECTOR, "path.highcharts-point")
    actions.move_to_element(el).perform()
