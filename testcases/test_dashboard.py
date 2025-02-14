import pytest
from pageObject.login import LoginPage
from utilities.utils import get_browser, get_config, setup_logger, take_screenshot
from pageObject.dashboard import DashboardPage

# Initialize the logger and configuration
logger = setup_logger()
config = get_config()
#

@pytest.fixture(scope="function")
def driver():
    # Read the browser name from the [WEB] section of config.ini
    browser_name = config.get('WEB', 'browser')
    driver = get_browser(browser_name)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_dynamic_boost_status_heading(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_dynamic_boost_status_heading_visible(), "Dynamic Boost Status heading is not visible"


def test_last_updated_timestamp(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_last_updated_timestamp_visible(), "Last Updated timestamp is not visible"


def test_dynamic_boost_icon(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_dynamic_boost_icon_visible(), "Dynamic Boost icon is not visible"


def test_profile_icon(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_profile_icon_visible(), "Profile icon is not visible"


def test_status_menu(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_status_menu_visible_and_clickable(), "Status menu is not visible or clickable"


def test_sources_menu(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_sources_menu_visible_and_clickable(), "Sources menu is not visible or clickable"


def test_payments_menu(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_payments_menu_visible_and_clickable(), "Payments menu is not visible or clickable"


def test_invoices_menu(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_invoices_menu_visible_and_clickable(), "Invoices menu is not visible or clickable"


def test_gateways_dropdown(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_gateways_dropdown_visible(), "Gateways dropdown is not visible"


def test_exceptions_badge(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_exceptions_badge_visible(), "Exceptions badge is not visible"


def test_source_documents_received_section(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_source_documents_received_section_visible(), "Source Documents Received section is not visible"


def test_emails_section(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_emails_section_visible(), "Emails section is not visible"


def test_payments_by_status_section(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_payments_by_status_section_visible(), "Payments by Status section is not visible"


def test_gateways_section(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_gateways_section_visible(), "Gateways section is not visible"


def test_payments_by_source_section(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_payments_by_source_section_visible(), "Payments by Source section is not visible"
