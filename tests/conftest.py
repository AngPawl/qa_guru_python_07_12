import pytest

from selene import browser, Config, Browser
from selene.support import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = "100.0"
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver))

    yield browser

@pytest.fixture(scope='function', autouse=True)
def open_new_browser(setup_browser):
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1400
    browser.config.window_height = 2800

    yield

    browser.quit()