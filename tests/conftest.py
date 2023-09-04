import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def open_new_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1400
    browser.config.window_height = 2800

    yield

    browser.quit()
