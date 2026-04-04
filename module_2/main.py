from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def run_script():
    driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://skillbox.ru")
    driver.quit()

if __name__ == '__main__':
    run_script()
    print(0)