import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging.config
import logging
from os import path

lof_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(lof_file_path)

@pytest.fixture
def driver():
    options = Options()
    options.page_load_strategy = 'normal'
    browser = webdriver.Chrome(options=options); browser.implicitly_wait(30)
    logging.info(f'Browser chrome has been started.')
    yield browser
    browser.quit()