from selenium.webdriver import Remote
import pytest

@pytest.fixture()
def set_up_browser():
    driver = Remote(desired_capabilities={
        "browserName": "chrome",
        "browserVersion": "latest"
    }, command_executor="http://127.0.0.1:4444/wb/hub")
    yield driver
    driver.quit()