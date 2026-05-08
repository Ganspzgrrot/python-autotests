import time
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait

@allure.feature('Функциональность поиска и фильтрации')
@allure.story('Валидация выдачи результатов по фильтрам')
class TestPracticalWork56:
    @allure.title("Поиск Issues по ключевому слову в заголовке ('bug')")
    def test_issue_search_by_title(self, driver): #Кейс №1 PASSED
        """
        Шаги:
        1.Открыть страницу со списком Issues репозитория Microsoft VS Code на GitHub;
        2.Очистить строку поиска и ввести фильтр 'in:title bug' для поиска по заголовкам;
        3.Проверить, что в каждом найденном тикете в названии присутствует слово 'bug'.

        Ожидаемый результат: Все найденные тикеты содержат слово 'bug' в своем заголовке(регистр не важен)
        """
        driver.get('https://github.com/microsoft/vscode/issues')
        el = driver.find_element(By.ID, 'repository-input')

        el.send_keys(Keys.CONTROL, 'a'); el.send_keys(Keys.BACKSPACE)
        el.send_keys('in:title bug', Keys.ENTER)

        issues = driver.find_elements(By.CLASS_NAME, 'issue')
        for issue in issues:
            title_text = issue.text.lower()
            assert "bug" in title_text

    @allure.title("Проверка фильтрации Issues по конткретному автору ('bpasero')")
    def test_github_author_filter_bpasero(self, driver):  #Кейс №2 PASSED
        """
        Шаги:
        1.Открыть страницу GitHub Issues для репозитория VS Code;
        2.В поле поиска ввести фильтр 'author:bpasero' и нажать Enter;
        3.Собрать список авторов изо всех найденных тикетов на странице.

        Ожидаемыйй результат: Для каждого найденного тикета автором является именно 'bpasero'
        """
        driver.get('https://github.com/microsoft/vscode/issues')

        el = driver.find_element(By.ID, 'repository-input'); el.send_keys('author:bpasero' + Keys.ENTER)
        authors = driver.find_elements(By.CSS_SELECTOR, ".js-issue-row a[data-hovercard-type='user']")
        for author in authors:
            assert author.text.lower() == 'bpasero'

    @allure.title("Расширенный поиск репозиториев: Python, >20к звёзд, файл environment.yml")
    def test_advanched_search_python_repositore(self, driver):  #Кейс №3 PASSED
        """
        Шаги:
        1.Перейти на страницу расширенного поиска GitHub;
        2.Выбрать в выпадающем списке язык программирования Python;
        3.Указать в поле количества звезд значение '>20000';
        4.Ввести название файла 'environment.yml' и нажать Enter для запуска поиска;
        5.Собрать данные о количестве звезд из результатов поиска.

        Ожидаемый результат: Каждый найденный репозиторий в результатах поиске имеет более 20000 звезд
        """
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

    @allure.title("Фильтрация курсов на Skillbox: проверка выдачи по тегам 'Профессия' и 'Месяц'")
    def test_tab_zwei_DropdownList(self, driver):  #Кейс №4 PASSED
        """
        Шаги:
        1.Открыть страницу каталога курсов Skillbox;
        2.Выбрать вкладку программ обучения;
        3.Настроить фильтры: выбрать длительность 'от 6 до 12 мес.' и тематику 'Airflow';
        4.Нажать кнопку 'Применить' и дождаться обновления списка;
        5.Проверить каждую найденную карточку курса на соответствие выбранным фильтрам.

        Ожидаемый результат: Список курсов не пуст, и каждая карточка содержит информацию о направлении ('профессия') и корректную длительность ('месяц')
        """
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

    @allure.title("Проверка всплывающей подсказки (tooltip) на графике активности коммитов")
    def test_github_commit_activity_tooltip(self, driver): #Кейс №5 PASSED
        """
        Шаги:
        1.Открыть страницу статистики активности коммитов (Commit Activity) репозитория VS Code;
        2.Найти на графике элемент точки(столбец активности);
        3.Выполнить наведение курсора мыши на выбранный элемент графика;
        4.Дождаться появления всплывающей подсказки (tooltip) и считать ее текст.

        Ожидаемый результат: Появившийся тултип содержит информацию о количестве коммитов ('commits') и временном интервале ('week')
        """
        driver.maximize_window()
        driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        actions = ActionChains(driver)

        el = driver.find_element(By.CSS_SELECTOR, "path.highcharts-point")
        actions.move_to_element(el).perform()

        tooltip = driver.find_element(By.XPATH, "//*[contains(text(), 'commits')]")
        tooltip_text = tooltip.text.lower()
        assert 'commits' in tooltip_text
        assert 'week' in tooltip_text
