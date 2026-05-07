import time
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait


class TestPracticalWork56:
    def test_issue_search_by_title(self, driver): #Кейс №1 PASSED
        driver.get('https://github.com/microsoft/vscode/issues')
        el = driver.find_element(By.ID, 'repository-input')

        el.send_keys(Keys.CONTROL, 'a'); el.send_keys(Keys.BACKSPACE)
        el.send_keys('in:title bug', Keys.ENTER)

        issues = driver.find_elements(By.CLASS_NAME, 'issue')
        for issue in issues:
            title_text = issue.text.lower()
            assert "bug" in title_text

    def test_github_author_filter_bpasero(self, driver):  #Кейс №2 PASSED
        driver.get('https://github.com/microsoft/vscode/issues')

        el = driver.find_element(By.ID, 'repository-input'); el.send_keys('author:bpasero' + Keys.ENTER)
        authors = driver.find_elements(By.CSS_SELECTOR, ".js-issue-row a[data-hovercard-type='user']")
        for author in authors:
            assert author.text.lower() == 'bpasero'

    def test_advanched_search_python_repositore(self, driver):  #Кейс №3 PASSED
        driver.maximize_window()
        driver.get('https://github.com/search/advanced')
        actions = ActionChains(driver)
        wait = WebDriverWait(driver, 10)

        Select(driver.find_element(By.ID, 'search_language')).select_by_visible_text('Python')
        search_stars = driver.find_element(By.ID, 'search_stars'); search_stars.click(); search_stars.send_keys('>20000')
        for _ in range(0, 500, 20):
            actions.scroll_by_amount(0, 20).perform(); time.sleep(0.01)

        search_filename = driver.find_element(By.ID, 'search_filename'); search_filename.send_keys('environment.yml')
        search_filename.send_keys(Keys.ENTER); wait.until(EC.staleness_of(search_filename))
        star_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[aria-label*="stars"]')))
        for link in star_links:
            label_text = link.get_attribute('aria-label')
            count_str = label_text.split()[0]; count = int(count_str)
            assert count > 20000

    def test_tab_zwei_DropdownList(self, driver):  #Кейс №4 PASSED
        driver.maximize_window()
        driver.get('https://skillbox.ru/code/')
        actions = ActionChains(driver)

        driver.find_element(By.XPATH, "//button[contains(@class, 'programs-filter-desktop__tab')]").click()
        driver.find_element(By.XPATH, "//button[contains(@class, 'ui-round-select__field') and contains(., 'Длительность')]").click()
        driver.find_element(By.XPATH, "//li[contains(@class, 'ui-round-select__item') and contains(text(), 'От 6 до 12 мес.')]").click()
        driver.find_element(By.XPATH, "//button[contains(., 'Тематика')]").click()
        driver.find_element(By.XPATH, "//li[contains(@class, 'ui-round-select__item') and contains(., 'Airflow')]").click()
        driver.find_element(By.XPATH, "//button[normalize-space()='Применить']").click()

        courses = driver.find_elements(By.XPATH, "//article[contains(@class, 'product-card-new')]")
        assert len(courses) > 0, "Ошибка: Карточки не найдены!"

        for course in courses:
            direction = course.find_element(By.XPATH, ".//span[contains(@class, 'product-card-new__direction')]").text.lower()
            duration = course.find_element(By.XPATH, ".//li[contains(@class, 'product-card-new__feature')]").text.lower()
            assert 'профессия' in direction
            assert 'месяц' in duration

    def test_github_commit_activity_tooltip(self, driver):
        driver.maximize_window()
        driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        actions = ActionChains(driver)

        el = driver.find_element(By.CSS_SELECTOR, "path.highcharts-point")
        actions.move_to_element(el).perform()

        tooltip = driver.find_element(By.XPATH, "//*[contains(text(), 'commits')]")
        tooltip_text = tooltip.text.lower()
        assert 'commits' in tooltip_text
        assert 'week' in tooltip_text
