import time
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import logging
logger = logging.getLogger('file')

@allure.feature('Работа с функционалом сайтов GitHub и Skillbox')
class TestPracticalWork_4_6:
    @allure.story('Поиск и фильтрация задач (Issues)')
    @allure.title('Поиск задач по ключевому слову "bug" в заголовке')
    def test_github_search_by_issue_title(self, driver): #PASSED
        with allure.step('Переход на страницу со списком задач'):
            driver.get('https://github.com/microsoft/vscode/issues')
            el = driver.find_element(By.ID, 'repository-input')
        with allure.step('Очистка поля поиска и ввод запроса "in:title bug"'):
            el.send_keys(Keys.CONTROL, 'a')
            el.send_keys(Keys.BACKSPACE)
            el.send_keys('in:title bug', Keys.ENTER)

    @allure.story('Поиск и фильтрация задач (Issues)')
    @allure.title('Фильтрация списка задач по пользователю "bpasero"')
    def test_github_author_filter_bpasero(self, driver): #PASSED
        with allure.step('Переход на страницу со списком задач'):
            driver.get('https://github.com/microsoft/vscode/issues')
            el = driver.find_element(By.ID, 'repository-input')
        with allure.step('Сброс текущих значений в поле поиска'):
            el.send_keys(Keys.CONTROL, 'a')
            el.send_keys(Keys.BACKSPACE)
        with allure.step('Фильтрация по автору через выпадающий список'):
            driver.find_element(By.CSS_SELECTOR, "[data-testid='authors-anchor-button']").click()
            driver.find_element(By.CSS_SELECTOR, "[placeholder='Filter authors']").send_keys('bpasero')
            driver.find_element(By.CSS_SELECTOR, "[placeholder='Filter authors']").send_keys(Keys.ENTER)

    @allure.story('Расширенный поиск репозиториев')
    @allure.title('Расширенный поиск репозиториев по языку, звездам и файлу')
    def test_advanched_search_python_repository(self, driver): #PASSED
        with allure.step('Открытие страницы расширенного поиска'):
            driver.get('https://github.com/search/advanced')
            actions = ActionChains(driver)
        with allure.step('Фильтрация по языку "Python" и звездам ">20000"'):
            Select(driver.find_element(By.ID, 'search_language')).select_by_visible_text('Python')
            search_stars = driver.find_element(By.ID, 'search_stars')
            search_stars.click()
            search_stars.send_keys('>20000')
        with allure.step('Прокрутка страницы для доступа к фильтру по файлам'):
            for _ in range(0, 500, 20):
                actions.scroll_by_amount(0, 20).perform()
                time.sleep(0.001)
        with allure.step('Поиск по имени файла "environment.yml"'):
            search_filename = driver.find_element(By.ID, 'search_filename')
            search_filename.send_keys('environment.yml')
            search_filename.send_keys(Keys.ENTER)

    @allure.story('Фильтрация курсор через выпадающие списки')
    @allure.title('Проверка выпадающих списков и фильтрации курсов (Airflow, 6-12 мес)')
    def test_tab_zwei_DropdownList(self, driver): #PASSED
        with allure.step('Открытие страницы курсов Skillbox'):
            driver.maximize_window(); driver.get('https://skillbox.ru/code/')
        with allure.step('Выбор фильтров: Программы, Длительность и Тематика'):
            driver.find_element(By.XPATH, "//button[contains(@class, 'programs-filter-desktop__tab')]").click()
            driver.find_element(By.XPATH, "//button[contains(@class, 'ui-round-select__field') and contains(., 'Длительность')]").click()
            driver.find_element(By.XPATH, "//li[contains(@class, 'ui-round-select__item') and contains(text(), 'От 6 до 12 мес.')]").click()
            driver.find_element(By.XPATH, "//button[contains(., 'Тематика')]").click()
            driver.find_element(By.XPATH, "//li[contains(@class, 'ui-round-select__item') and contains(., 'Airflow')]").click()
            driver.find_element(By.XPATH, "//button[normalize-space()='Применить']").click()

    @allure.story('Просмотр детальной информации на графиках (Tooltip)')
    @allure.title('Проверка всплывающей подсказки tooltip на графике коммитов')
    def test_hover_on_commit_chart_shows_tooltip(self, driver): #PASSED
        with allure.step('Открытие страницы графиков репозиториея'):
            driver.maximize_window()
            driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
            actions = ActionChains(driver)
        with allure.step('Наведение курсора на точку графика (hover)'):
            el = driver.find_element(By.CSS_SELECTOR, "path.highcharts-point")
            actions.move_to_element(el).perform()
