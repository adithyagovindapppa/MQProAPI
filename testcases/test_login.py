# File: testcases/test_login.py

import pytest
from pageObject.login import LoginPage
from utilities.utils import get_browser, get_config, setup_logger, take_screenshot

# Initialize the logger and configuration
logger = setup_logger()
config = get_config()


@pytest.fixture(scope="function")
def driver():
    # Read the browser name from the [WEB] section of config.ini
    browser_name = config.get('WEB', 'browser')
    driver = get_browser(browser_name)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_valid_login(driver):
    # Use the base_url from the [WEB] section and valid credentials from [CREDENTIALS]
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()

    # Assert that the dashboard (or a unique element) is displayed after login
    assert login_page.is_dynamic_boost_status_displayed(), "Dashboard was not displayed after valid login."

    screenshot_file = take_screenshot(driver, 'valid_login.png')
    logger.info("Screenshot saved to %s", screenshot_file)


def test_invalid_login(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    invalid_password = config.get('CREDENTIALS', 'invaidpassword')  # note: key name as provided

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(invalid_password)
    login_page.click_login()

    error_message = login_page.get_error_message()
    assert error_message is not None, "Error message should be displayed for invalid login."

    screenshot_file = take_screenshot(driver, 'invalid_login.png')
    logger.info("Screenshot saved to %s", screenshot_file)


def test_empty_username(driver):
    base_url = config.get('WEB', 'base_url')
    empty_user = config.get('CREDENTIALS', 'emptyusername')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(empty_user)
    login_page.enter_password(valid_password)
    login_page.click_login()

    # Add your assertions for error handling here
    error_message = login_page.get_error_message()
    assert error_message is not None, "Error message should be displayed for empty username."


def test_special_character_email_button_enabled(driver):
    base_url = config.get('WEB', 'base_url')
    special_email = config.get('CREDENTIALS', 'specialcharemail')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(special_email)
    login_page.enter_password(valid_password)
    error_message = login_page.is_sign_button_enabled()
    assert error_message is not None, "Sign button should be disabled when email and password are empty"
