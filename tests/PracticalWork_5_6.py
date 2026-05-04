import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class TestPracticalWork56:
    def test_issue_search_by_title(self, driver): #Кейс №1 PASSED
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

    def test_github_author_filter_bpasero(self, driver):  #Кейс №2 PASSED
        driver.get('https://github.com/microsoft/vscode/issues')
        time.sleep(1.4)

        el = driver.find_element(By.ID, 'repository-input'); time.sleep(0.8); el.send_keys('author:bpasero' + Keys.ENTER); time.sleep(0.5)
        authors = driver.find_elements(By.CSS_SELECTOR, ".js-issue-row a[data-hovercard-type='user']")
        for author in authors:
            assert author.text.lower() == 'bpasero'

        time.sleep(5)

    def test_advanched_search_python_repositore(self, driver):  #Кейс №3 PASSED
        driver.maximize_window()
        driver.get('https://github.com/search/advanced')
        actions = ActionChains(driver)
        time.sleep(4)

        Select(driver.find_element(By.ID, 'search_language')).select_by_visible_text('Python'); time.sleep(2)
        search_stars = driver.find_element(By.ID, 'search_stars'); search_stars.click(); search_stars.send_keys('>20000'); time.sleep(0.6)
        for _ in range(0, 500, 20):
            actions.scroll_by_amount(0, 20).perform(); time.sleep(0.01)
        search_filename = driver.find_element(By.ID, 'search_filename'); search_filename.send_keys('environment.yml'); time.sleep(0.5); search_filename.send_keys(Keys.ENTER); time.sleep(5)
        star_links = driver.find_elements(By.CSS_SELECTOR, 'a[aria-label*="stars"]')
        for link in star_links:
            label_text = link.get_attribute('aria-label')
            count_str = label_text.split()[0]; count = int(count_str)
            assert count > 20000

        time.sleep(6)

    def test_tab_zwei_DropdownList(self, driver):  #Кейс №4 PASSED
        driver.maximize_window()
        driver.get('https://skillbox.ru/code/')
        actions = ActionChains(driver)
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[contains(@class, 'programs-filter-desktop__tab')]").click(); time.sleep(0.7)
        driver.find_element(By.XPATH, "//button[contains(@class, 'ui-round-select__field') and contains(., 'Длительность')]").click(); time.sleep(0.7)
        driver.find_element(By.XPATH, "//li[contains(@class, 'ui-round-select__item') and contains(text(), 'От 6 до 12 мес.')]").click(); time.sleep(0.7)
        driver.find_element(By.XPATH, "//button[contains(., 'Тематика')]").click(); time.sleep(0.7)
        driver.find_element(By.XPATH, "//li[contains(@class, 'ui-round-select__item') and contains(., 'Airflow')]").click(); time.sleep(0.7)
        driver.find_element(By.XPATH, "//button[normalize-space()='Применить']").click()
        time.sleep(10)

        courses = driver.find_elements(By.XPATH, "//article[contains(@class, 'product-card-new')]")
        assert len(courses) > 0, "Ошибка: Карточки не найдены!"

        for course in courses:
            direction = course.find_element(By.XPATH, ".//span[contains(@class, 'product-card-new__direction')]").text.lower()
            duration = course.find_element(By.XPATH, ".//li[contains(@class, 'product-card-new__feature')]").text.lower()
            assert 'профессия' in direction
            assert 'месяц' in duration

        time.sleep(8)

    def test_github_commit_activity_tooltip(self, driver):
        driver.maximize_window()
        driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        actions = ActionChains(driver)
        time.sleep(2)

        el = driver.find_element(By.CSS_SELECTOR, "path.highcharts-point"); time.sleep(0.7)
        actions.move_to_element(el).perform(); time.sleep(5)

        tooltip = driver.find_element(By.XPATH, "//*[contains(text(), 'commits')]")
        tooltip_text = tooltip.text.lower()
        assert 'commits' in tooltip_text
        assert 'week' in tooltip_text

        time.sleep(3.5)
