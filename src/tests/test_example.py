import pytest
from selenium import webdriver

def test_site_title():
    driver = webdriver.Chrome()
    driver.get('https://skillbox.ru')
    assert "Skillbox" in driver.title
    driver.quit()
