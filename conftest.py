import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import logging.config
import logging

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('file')


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--incognito')
    options.page_load_strategy = 'normal'

    service = ChromeService(ChromeDriverManager().install())

    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(30)

    logger.info('Browser chrome has been started.')
    yield browser
    logger.info('Browser chrome has been closed.')
    browser.quit()