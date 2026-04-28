import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class TestPracticalWork56:
    def test_issue_search_by_title(self, driver):
        driver.get('https://github.com/microsoft/vscode/issues')
        el = driver.find_element(By.ID, 'repository-input')
        time.sleep(2)

        el.send_keys(Keys.CONTROL, 'a'); time.sleep(0.6); el.send_keys(Keys.BACKSPACE); time.sleep(0.6)
        el.send_keys('in:title bug', Keys.ENTER); time.sleep(0.5)

        issues = driver.find_elements(By.CLASS_NAME, 'issue')
        for issue in issues:
            title_text = issue.text.lower()
            assert "bug" in title_text

        time.sleep(5)

    def test_github_author_filter_bpasero(self, driver):  # PASSED
        driver.get('https://github.com/microsoft/vscode/issues')
        time.sleep(1.4)

        el = driver.find_element(By.ID, 'repository-input'); time.sleep(0.8); el.send_keys('author:bpasero' + Keys.ENTER); time.sleep(0.5)
        authors = driver.find_elements(By.CSS_SELECTOR, ".js-issue-row a[data-hovercard-type='user']")
        for author in authors:
            assert author.text.lower() == 'bpasero'

        time.sleep(5)

    def test_advanched_search_python_repositore(self, driver):  # PASSED
        driver.get('https://github.com/search/advanced')
        actions = ActionChains(driver)
        time.sleep(4)

        Select(driver.find_element(By.ID, 'search_language')).select_by_visible_text('Python'); time.sleep(2)
        search_stars = driver.find_element(By.ID, 'search_stars'); search_stars.click(); search_stars.send_keys('>20000'); time.sleep(0.6)
        for _ in range(0, 500, 20):
            actions.scroll_by_amount(0, 20).perform(); time.sleep(0.01)
        search_filename = driver.find_element(By.ID, 'search_filename'); search_filename.send_keys('environment.yml'); time.sleep(0.5); search_filename.send_keys(Keys.ENTER); time.sleep(5)
        results_header = driver.find_element(By.XPATH, "//*[contains(text(), 'results')]"); time.sleep(5)
        header = results_header.text.lower(); time.sleep(3); count = header.split()[0].replace(',', '').replace('.', ''); count = int(count)
        assert count > 0

        time.sleep(6)

