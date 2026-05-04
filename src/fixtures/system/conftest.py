import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addini("load_page_normal", "Normal page load")

@pytest.fixture
def driver(pytestconfig):
    options = Options()
    options.page_load_strategy = pytestconfig.getini("load_page_normal")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(30)
    yield browser
    browser.quit()