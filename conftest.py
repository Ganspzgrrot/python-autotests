import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.page_load_strategy = 'normal'
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(30)
    yield browser
    browser.quit()