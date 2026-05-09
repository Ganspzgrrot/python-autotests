import time
from selenium.webdriver.support import expected_conditions as EC
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
    def test_issue_search_by_title(self, driver):  #Кейс №1 PASSED
        with allure.step('Открытие страницы GitHub Issues и поиск поля ввода'):
            driver.get('https://github.com/microsoft/vscode/issues')
            el = driver.find_element(By.ID, 'repository-input')
        with allure.step('Очистка поля поиска и ввод запроса "in:title bug"'):
            el.send_keys(Keys.CONTROL, 'a')
            el.send_keys(Keys.BACKSPACE)
            el.send_keys('in:title bug', Keys.ENTER)
        with allure.step('Проверка того, что все найденные Issues содержат слово "bug"'):
            issues = driver.find_elements(By.CLASS_NAME, 'issue')
            for issue in issues:
                title_text = issue.text.lower()
                assert "bug" in title_text

    @allure.title("Проверка фильтрации Issues по конткретному автору ('bpasero')")
    def test_github_author_filter_bpasero(self, driver):  #Кейс №2 PASSED
        with allure.step('Открытие страницы и поиск инпута'):
            driver.get('https://github.com/microsoft/vscode/issues')
            el = driver.find_element(By.ID, 'repository-input')
        with allure.step('применение фильтра "author:bpasero"'):
            el.send_keys('author:bpasero' + Keys.ENTER)
        with allure.step('Проверка: все найденные авторы должны быть "bpasero"'):
            authors = driver.find_elements(By.CSS_SELECTOR, ".js-issue-row a[data-hovercard-type='user']")
            for author in authors:
                assert author.text.lower() == 'bpasero'

    @allure.title("Расширенный поиск репозиториев: Python, >20к звёзд, файл environment.yml")
    def test_advanched_search_python_repositore(self, driver):  #Кейс №3 PASSED
        with allure.step('Подготовка: открытие страницы расширенного поиска'):
            driver.maximize_window()
            driver.get('https://github.com/search/advanced')
            actions = ActionChains(driver)
            wait = WebDriverWait(driver, 10)
        with allure.step('Выбор языка программирования "Python" и фильтра по звездам (>20000)'):
            Select(driver.find_element(By.ID, 'search_language')).select_by_visible_text('Python')
            search_stars = driver.find_element(By.ID, 'search_stars')
            search_stars.click()
            search_stars.send_keys('>20000')
        with allure.step('Прокрутка страницы для доступа к дополнительным фильтрам'):
            for _ in range(0, 500, 20):
                actions.scroll_by_amount(0, 20).perform(); time.sleep(0.01)
        with allure.step('Поиск по имени файла "environment.yml" и переход к результам'):
            search_filename = driver.find_element(By.ID, 'search_filename')
            search_filename.send_keys('environment.yml')
            search_filename.send_keys(Keys.ENTER)
            wait.until(EC.staleness_of(search_filename))
            star_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[aria-label*="stars"]')))
        with allure.step('Валидация: проверка количества звезд (>20000) у найденных репозиториев '):
            for link in star_links:
                label_text = link.get_attribute('aria-label')
                count_str = label_text.split()[0]
                count = int(count_str)
                assert count > 20000

    @allure.title("Фильтрация курсов на Skillbox: проверка выдачи по тегам 'Профессия' и 'Месяц'")
    def test_tab_zwei_DropdownList(self, driver):  #Кейс №4 PASSED
        with allure.step('Открытие страницы и подготовка браузера'):
            driver.maximize_window()
            driver.get('https://skillbox.ru/code/')
        with allure.step('Настройка фильтров: Программы, Длительность (6-12 мес) и Тематика (Airflow)'):
            driver.find_element(By.XPATH, "//button[contains(@class, 'programs-filter-desktop__tab')]").click()
            driver.find_element(By.XPATH, "//button[contains(@class, 'ui-round-select__field') and contains(., 'Длительность')]").click()
            driver.find_element(By.XPATH, "//li[contains(@class, 'ui-round-select__item') and contains(text(), 'От 6 до 12 мес.')]").click()
            driver.find_element(By.XPATH, "//button[contains(., 'Тематика')]").click()
            driver.find_element(By.XPATH, "//li[contains(@class, 'ui-round-select__item') and contains(., 'Airflow')]").click()
            driver.find_element(By.XPATH, "//button[normalize-space()='Применить']").click()
        with allure.step('Поиск и сбор карточек курсов'):
            courses = driver.find_elements(By.XPATH, "//article[contains(@class, 'product-card-new')]")
            assert len(courses) > 0, "Ошибка: Карточки не найдены!"
        with allure.step('Валидация: проверка каждой карточки на наличие текста "Профессия" и "Месяц"'):
            for course in courses:
                direction = course.find_element(By.XPATH, ".//span[contains(@class, 'product-card-new__direction')]").text.lower()
                duration = course.find_element(By.XPATH, ".//li[contains(@class, 'product-card-new__feature')]").text.lower()
                assert 'профессия' in direction
                assert 'месяц' in duration

    @allure.title("Проверка всплывающей подсказки (tooltip) на графике активности коммитов")
    def test_github_commit_activity_tooltip(self, driver):  #Кейс №5 PASSED
        with allure.step('Подготовка: переход на страницу графиков репозитория VS Code'):
            driver.maximize_window()
            driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
            actions = ActionChains(driver)
        with allure.step('Взаимодействие: наведение курсора на точку графика'):
            el = driver.find_element(By.CSS_SELECTOR, "path.highcharts-point")
            actions.move_to_element(el).perform()
        with allure.step('Валидация: проверка содержимого тултипа'):
            tooltip = driver.find_element(By.XPATH, "//*[contains(text(), 'commits')]")
            tooltip_text = tooltip.text.lower()
            assert 'commits' in tooltip_text
            assert 'week' in tooltip_text
