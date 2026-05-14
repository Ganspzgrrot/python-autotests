from pytest_playwright.pytest_playwright import browser, new_context
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
import allure
import logging

logger = logging.getLogger('file')

@allure.feature('Функциональность поиска и фильтрации')
@allure.story('Валидация выдачи результатов по фильтрам')
class TestPracticalWork56:
    @allure.title("Поиск Issues по ключевому слову в заголовке ('bug')")
    def test_issue_search_by_title(self, page):  #Кейс №1 PASSED
        with allure.step('Открытие страницы GitHub Issues и поиск поля ввода'):
            page.goto('https://github.com/microsoft/vscode/issues')

            el = page.locator('#repository-input')
        with allure.step('Очистка поля поиска и ввод запроса "in:title bug"'):
            el.fill('is:issue state:open in:title bug')
            el.press('Enter')
        with allure.step('Проверка того, что все найденные Issues содержат слово "bug"'):
            issues = page.locator('#issue').all()
            for issue in issues:
                title_text = issue.text.lower()
                assert "bug" in title_text

    @allure.title("Проверка фильтрации Issues по конткретному автору ('bpasero')")
    def test_github_author_filter_bpasero(self, page):  #Кейс №2 PASSED
        with allure.step('Открытие страницы и поиск инпута'):
            page.goto('https://github.com/microsoft/vscode/issues')
            el = page.locator('#repository-input')
        with allure.step('применение фильтра "author:bpasero"'):
            el.fill('author:bpasero')
        with allure.step('Проверка: все найденные авторы должны быть "bpasero"'):
            authors = page.locator(".js-issue-row a[data-hovercard-type='user']").all()
            for author in authors:
                expect(author).to_have_text('bpasero', ignoreCase=True)

    @allure.title("Расширенный поиск репозиториев: Python, >20к звёзд, файл environment.yml")
    def test_advanched_search_python_repositore(self, page):  #Кейс №3 PASSED
        with allure.step('Подготовка: открытие страницы расширенного поиска'):
            page.goto('https://github.com/search/advanced')
        with allure.step('Выбор языка программирования "Python" и фильтра по звездам (>20000)'):
            page.locator('#search_language').select_option(label='Python')
            search_stars = page.locator('#search_stars')
            search_stars.click()
            search_stars.fill('>20000')
        with allure.step('Поиск по имени файла "environment.yml" и переход к результам'):
            search_filename = page.locator('#search_filename')
            search_filename.fill('environment.yml')
            search_filename.press('Enter')
            star_links = page.locator('a[aria-label*="stars"]').all()
        with allure.step('Валидация: проверка количества звезд (>20000) у найденных репозиториев '):
            for link in star_links:
                label_text = link.get_attribute('aria-label')
                count_str = label_text.split()[0]
                count = int(count_str)
                assert count > 20000

    @allure.title("Фильтрация курсов на Skillbox: проверка выдачи по тегам 'Профессия' и 'Месяц'")
    def test_tab_zwei_DropdownList(self, browser, page):  #Кейс №4 PASSED
        with allure.step('Открытие страницы и подготовка браузера'):
            page.goto('https://skillbox.ru/code/')
        with allure.step('Настройка фильтров: Программы, Длительность (6-12 мес) и Тематика (Airflow)'):
            page.locator("//button[contains(text(),'Фильтры')]").click()
            page.locator(".programs-filter-group:nth-child(1) .programs-filter-group__tab:nth-child(1)").click()
            page.locator(".programs-filter-group:nth-child(4) .programs-filter-group__tab:nth-child(2)").click()
            page.locator(".ui-tab--stroke-additional").click()
            page.fill(".ui-search-shared__input--small", "Python")
            page.locator("//label[normalize-space()='Python']").click()
            page.locator('//button[normalize-space(text())="Выбрать"]').click()
            page.locator('//button[normalize-space(text())="Применить"]').click()
        with allure.step('Поиск и сбор карточек курсов'):
            page.wait_for_selector(".product-card-new")
            page.mouse.wheel(0, 500)
            courses = page.locator(".product-card-new").all()
            assert len(courses) > 0, "Ошибка: Карточки не найдены!"
        with allure.step('Валидация: проверка каждой карточки на наличие текста "Профессия" и "Месяц"'):
            page.mouse.wheel(0, 500)
            for course in courses:
                direction_text = course.locator(".product-card-new__direction").inner_text().lower()
                duration_text = course.locator(".product-card-new__feature").first.inner_text().lower()
                assert 'профессия' in direction_text
                assert 'месяц' in duration_text

    @allure.title("Проверка всплывающей подсказки (tooltip) на графике активности коммитов")
    def test_github_commit_activity_tooltip(self, page):  #Кейс №5 PASSED
        with allure.step('Подготовка: переход на страницу графиков репозитория VS Code'):
            page.goto('https://github.com/microsoft/vscode/graphs/commit-activity')
            page.set_viewport_size({'width': 1920, 'height': 1080})
        with allure.step('Взаимодействие: наведение курсора на точку графика'):
            page.hover("path.highcharts-point")
        with allure.step('Валидация: проверка содержимого тултипа'):
            tooltip = page.locator("//*[contains(text(), 'commits')]")
            tooltip_text = tooltip.inner_text().lower()
            assert 'commits' in tooltip_text
            assert 'week' in tooltip_text