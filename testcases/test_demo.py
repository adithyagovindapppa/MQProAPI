import os
import time
import pytest
from pageObject.login import LoginPage
from utilities.utils import get_browser, get_config, setup_logger, take_screenshot
from pageObject.dashboard import DashboardPage
from pageObject.internal import InternalPage

# Initialize the logger and configuration
logger = setup_logger()
config = get_config()


@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize the browser driver."""
    browser_name = config.get('WEB', 'browser')
    driver = get_browser(browser_name)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# Helper function for login and navigating to Internal Page
def login_and_navigate_to_internal(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    # Open the base URL and log in
    driver.get(base_url)
    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()

    # Wait for login to complete
    time.sleep(5)  # Consider replacing with WebDriverWait for better synchronization

    # Navigate to the Internal page
    internal_page = InternalPage(driver)
    internal_page.click_dropdown()
    internal_page.select_dropdown_option()

    return internal_page


# 1. Validate that the "Sources -> Internal" screen is displayed
def test_validate_internal_page(driver):
    internal_page = login_and_navigate_to_internal(driver)
    assert internal_page.is_internal_displayed(), "Internal text not displayed"


# 2. Validate all key elements are displayed on the "Sources -> Internal" screen
def test_elements_displayed(driver):
    internal_page = login_and_navigate_to_internal(driver)
    assert internal_page.is_internal_displayed(), "Internal text not displayed"
    assert internal_page.are_key_elements_visible(), "One or more key elements are missing on the Internal page."


# 3. Validate redirection to "Adding New Entries" page when clicking "New Internal Batch"
def test_download_upload_file(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    assert internal_page.is_adding_batch_displayed(), "Adding New Entries text not displayed"
    assert internal_page.are_download_upload_sections_visible(), "Download/Upload sections are missing"


# 4. Validate the download functionality for 'Template Domestic Payments'
def test_download_template(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()

    download_dir = "C:/Users/Adithya G/Downloads"  # Update with your downloads folder
    expected_file = "DOMESTIC.xlsx"  # Update with correct file name
    internal_page.click_download_template1()

    assert internal_page.is_file_downloaded(download_dir, expected_file), "File not downloaded"

    # Optional: Verify file content
    file_path = os.path.join(download_dir, expected_file)
    assert os.path.getsize(file_path) > 0, "Downloaded file is empty"

    # Optional Cleanup
    os.remove(file_path)


# 5. Validate the download functionality for 'Template Domestic Payments with Source Link(s)'
def test_download_source_template(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()

    download_dir = "C:/Users/Adithya G/Downloads"  # Update with your downloads folder
    expected_file = "DOMESTIC_SOURCE_LINK.xlsx"  # Update with correct file name
    internal_page.click_download_template()

    assert internal_page.is_file_downloaded(download_dir, expected_file), "File not downloaded"

    # Optional: Verify file content
    file_path = os.path.join(download_dir, expected_file)
    assert os.path.getsize(file_path) > 0, "Downloaded file is empty"

    # Optional Cleanup
    os.remove(file_path)


# 6. Validate the download functionality for 'Template International Payments'
def test_download_international_payments(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()

    download_dir = "C:/Users/Adithya G/Downloads"  # Update with your downloads folder
    expected_file = "INTERNATIONAL.xlsx"  # Update with correct file name
    internal_page.click_download_template()

    assert internal_page.is_file_downloaded(download_dir, expected_file), "File not downloaded"

    # Optional: Verify file content
    file_path = os.path.join(download_dir, expected_file)
    assert os.path.getsize(file_path) > 0, "Downloaded file is empty"

    # Optional Cleanup
    os.remove(file_path)


# 7. Validate the download functionality for 'Template Commerce Payments'
def test_download_commerce_payments(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()

    download_dir = "C:/Users/Adithya G/Downloads"  # Update with your downloads folder
    expected_file = "COMMERCE.xlsx"  # Update with correct file name
    internal_page.click_download_template()

    assert internal_page.is_file_downloaded(download_dir, expected_file), "File not downloaded"

    # Optional: Verify file content
    file_path = os.path.join(download_dir, expected_file)
    assert os.path.getsize(file_path) > 0, "Downloaded file is empty"

    # Optional Cleanup
    os.remove(file_path)


# 8. Validate the "Select Template Type" dropdown functionality
def test_select_template_dropdown(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()

    internal_page.open_dropdown()
    time.sleep(5)  # Reduced sleep, you could use WebDriverWait for more reliable waits
    assert internal_page.verify_all_options_present(), "Not all expected options are displayed in the dropdown."
    for option in [
        "Template Domestic Payments",
        "Template Domestic Payments with Source Link(s)",
        "Template International Payments",
        "Template Commerce Payments"
    ]:
        selected_option = internal_page.select_option(option)
        assert selected_option == option, f"Failed to select {option}, selected {selected_option} instead"

import os
import time

import pytest
from pageObject.login import LoginPage
from utilities.utils import get_browser, get_config, setup_logger, take_screenshot
from pageObject.dashboard import DashboardPage
from pageObject.internal import InternalPage

# Initialize the logger and configuration
logger = setup_logger()
config = get_config()


####
@pytest.fixture(scope="function")
def driver():
    # Read the browser name from the [WEB] section of config.ini
    browser_name = config.get('WEB', 'browser')
    driver = get_browser(browser_name)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def login_and_navigate_to_internal(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')

    # Open the base URL and log in
    driver.get(base_url)
    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()

    # Wait for login to complete
    time.sleep(5)  # Consider replacing with WebDriverWait for better synchronization

    # Navigate to the Internal page
    internal_page = InternalPage(driver)
    internal_page.click_dropdown()
    internal_page.select_dropdown_option()

    return internal_page


#1.Validate that the "Sources -> Internal" screen is displayed
# def test_validate_internal_page(driver):
#     base_url = config.get('WEB', 'base_url')
#     valid_user = config.get('CREDENTIALS', 'username')
#     valid_password = config.get('CREDENTIALS', 'password')
#     driver.get(base_url)
#     login_page = LoginPage(driver)
#     login_page.enter_email(valid_user)
#     login_page.enter_password(valid_password)
#     login_page.click_login()
#     time.sleep(10)
#     internal_page = InternalPage(driver)
#     internal_page.click_dropdown()
#     internal_page.select_dropdown_option()
#     assert internal_page.is_internal_displayed(), "Internal text not display"
def test_validate_internal_page(driver):
    internal_page = login_and_navigate_to_internal(driver)
    assert internal_page.is_internal_displayed(), "Internal text not displayed"


#2.Validate all key elements are displayed on the "Sources -> Internal" screen
def test_elements_displayed(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')
    driver.get(base_url)
    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    time.sleep(10)
    internal_page = InternalPage(driver)
    internal_page.click_dropdown()
    internal_page.select_dropdown_option()
    assert internal_page.is_internal_displayed(), "Internal text not display"
    time.sleep(5)
    assert internal_page.are_key_elements_visible(), "One or more key elements are missing on the Internal page."


#3.Validate redirection to "Adding New Entries" page when clicking "New Internal Batch"
def test_download_upload_file(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')
    driver.get(base_url)
    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    time.sleep(10)
    internal_page = InternalPage(driver)
    internal_page.click_dropdown()
    internal_page.select_dropdown_option()
    assert internal_page.is_internal_displayed(), "Internal text not display"
    time.sleep(10)
    internal_page.click_internal_batch()
    assert internal_page.is_adding_batch_displayed(), "Adding New Entries text not display"
    assert internal_page.are_download_upload_sections_visible(), "Download/Upload sections are missing"


#4.Validate redirection to "Adding New Entries" page when clicking "New Internal Batch"
def test_download_template(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')
    driver.get(base_url)
    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    time.sleep(10)
    internal_page = InternalPage(driver)
    internal_page.click_dropdown()
    internal_page.select_dropdown_option()
    time.sleep(10)
    internal_page.click_internal_batch()
    assert internal_page.is_adding_batch_displayed(), "Adding New Entries text not display"
    download_dir = "C:/Users/Adithya G/Downloads"  # Update with your downloads folder
    expected_file = "DOMESTIC.xlsx"  # Update with correct file name
    internal_page.click_download_template1()

    assert internal_page.is_file_downloaded(download_dir, expected_file), "File not downloaded"

    file_path = os.path.join(download_dir, expected_file)

    # ✅ Optional: Verify file content
    assert os.path.getsize(file_path) > 0, "Downloaded file is empty"

    # ✅ Cleanup (if needed)
    os.remove(file_path)  # Delete after validation (optional)


#5.Validate the download functionality for 'Template Domestic Payments with Source Link(s)'
def test_download_source_template(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')
    driver.get(base_url)
    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    time.sleep(10)
    internal_page = InternalPage(driver)
    internal_page.click_dropdown()
    internal_page.select_dropdown_option()
    time.sleep(10)
    internal_page.click_internal_batch()
    assert internal_page.is_adding_batch_displayed(), "Adding New Entries text not display"
    download_dir = "C:/Users/Adithya G/Downloads"  # Update with your downloads folder
    expected_file = "DOMESTIC_SOURCE_LINK.xlsx"  # Update with correct file name
    internal_page.click_download_template2()

    assert internal_page.is_file_downloaded(download_dir, expected_file), "File not downloaded"

    file_path = os.path.join(download_dir, expected_file)

    # ✅ Optional: Verify file content
    assert os.path.getsize(file_path) > 0, "Downloaded file is empty"

    # ✅ Cleanup (if needed)
    os.remove(file_path)  # Delete after validation (optional)


#6.Validate the download functionality for 'Template International Payments
def test_download_international_payments(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')
    driver.get(base_url)
    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    time.sleep(10)
    internal_page = InternalPage(driver)
    internal_page.click_dropdown()
    internal_page.select_dropdown_option()
    time.sleep(10)
    internal_page.click_internal_batch()
    assert internal_page.is_adding_batch_displayed(), "Adding New Entries text not display"
    download_dir = "C:/Users/Adithya G/Downloads"  # Update with your downloads folder
    expected_file = "INTERNATIONAL.xlsx"  # Update with correct file name
    internal_page.click_download_template3()

    assert internal_page.is_file_downloaded(download_dir, expected_file), "File not downloaded"

    file_path = os.path.join(download_dir, expected_file)

    # ✅ Optional: Verify file content
    assert os.path.getsize(file_path) > 0, "Downloaded file is empty"

    # ✅ Cleanup (if needed)
    os.remove(file_path)  # Delete after validation (optional)


#7.Validate the download functionality for 'Template Commerce Payments
def test_download_commerce_payments(driver):
    base_url = config.get('WEB', 'base_url')
    valid_user = config.get('CREDENTIALS', 'username')
    valid_password = config.get('CREDENTIALS', 'password')
    driver.get(base_url)
    login_page = LoginPage(driver)
    login_page.enter_email(valid_user)
    login_page.enter_password(valid_password)
    login_page.click_login()
    time.sleep(10)
    internal_page = InternalPage(driver)
    internal_page.click_dropdown()
    internal_page.select_dropdown_option()
    time.sleep(10)
    internal_page.click_internal_batch()
    assert internal_page.is_adding_batch_displayed(), "Adding New Entries text not display"
    download_dir = "C:/Users/Adithya G/Downloads"  # Update with your downloads folder
    expected_file = "COMMERCE.xlsx"  # Update with correct file name
    internal_page.click_download_template4()

    assert internal_page.is_file_downloaded(download_dir, expected_file), "File not downloaded"

    file_path = os.path.join(download_dir, expected_file)

    # ✅ Optional: Verify file content
    assert os.path.getsize(file_path) > 0, "Downloaded file is empty"

    # ✅ Cleanup (if needed)
    os.remove(file_path)  # Delete after validation (optional)

#9.Validate the functionality of the "Back Arrow" button
#16.Validate file selection functionality and display of selected file
def test_validate_file_upload_name(driver):
    # Step 1: Login and navigate to internal page
    internal_page = login_and_navigate_to_internal(driver)

    # Step 2: Click on the necessary elements to reach the file upload section
    internal_page.click_internal_batch()
    internal_page.click_template_dropdown()
    internal_page.click_template_domestic_sourcelink_file()

    # Step 3: Resolve the file path dynamically
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "../testdata/DOMESTIC_SOURCE_LINK.xlsx")

    # Step 4: Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Output current working directory and resolved file path for debugging
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)

    # Step 5: Add the file to the upload section
    internal_page.add_file(file_path)

    # You can assert whether the uploaded file name appears in the UI or whether the button's state changes.
    uploaded_file_name = internal_page.get_uploaded_file_name()  # Assuming this method exists
    assert uploaded_file_name == "DOMESTIC_SOURCE_LINK.xlsx", f"Expected file name 'DOMESTIC_SOURCE_LINK.xlsx', but got {uploaded_file_name}."
#26.Validate navigation to file status page from 'Validated' status and check for errors or warnings
def test_navigation_to_file_status_page(driver):
    """
    Test the navigation to the file status page, including file upload, validation,
    and error/warning count retrieval.
    """
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()

    # Prepare file path
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)

    # Upload & Validate File
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()

    # Verify File Status
    file_status = internal_page.get_file_status()
    expected_statuses = ["Submitted", "Validation"]

    assert file_status in expected_statuses, (
        f"Expected file status to be one of {expected_statuses}, but got '{file_status}'."
    )

    # Click Status Button and Verify Navigation
    time.sleep(5)
    internal_page.click_status_button()
    time.sleep(5)

    assert internal_page.is_file_status_page_displayed(), "Failed to navigate to the file status page."

    # Retrieve and Validate Error/Warning Counts
    error_warning_counts = internal_page.get_error_and_warning_counts()

    print(f"Error Count: {error_warning_counts['errors']}")
    print(f"Warning Count: {error_warning_counts['warnings']}")

    assert isinstance(error_warning_counts['errors'], int), "Error count is not a valid integer."
    assert isinstance(error_warning_counts['warnings'], int), "Warning count is not a valid integer."

    print("✅ Navigation and validation test passed successfully!")



