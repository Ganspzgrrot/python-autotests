import pytest
from selenium import webdriver
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()