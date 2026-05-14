import pytest
from playwright.sync_api import sync_playwright
import allure

@pytest.fixture(scope='session')
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope='function')
def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    page=browser.new_page()
    yield page
    browser.close()