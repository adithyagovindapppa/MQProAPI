import os
import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

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
def test_validate_internal_page(driver):
    internal_page = login_and_navigate_to_internal(driver)
    assert internal_page.is_internal_displayed(), "Internal text not displayed"


# 2.Validate all key elements are displayed on the "Sources -> Internal" screen
def test_elements_displayed(driver):
    internal_page = login_and_navigate_to_internal(driver)
    assert internal_page.is_internal_displayed(), "Internal text not displayed"
    assert internal_page.are_key_elements_visible(), "One or more key elements are missing on the Internal page."


#
# 3.Validate redirection to "Adding New Entries" page when clicking "New Internal Batch"
def test_download_upload_file(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    time.sleep(10)
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
    internal_page.click_download_template2()

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
    internal_page.click_download_template3()

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
    internal_page.click_download_template4()

    assert internal_page.is_file_downloaded(download_dir, expected_file), "File not downloaded"

    # Optional: Verify file content
    file_path = os.path.join(download_dir, expected_file)
    assert os.path.getsize(file_path) > 0, "Downloaded file is empty"

    # Optional Cleanup
    os.remove(file_path)


#8.Validate the "Select Template Type" dropdown functionality
def test_select_template_dropdown(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    internal_page.click_template_dropdown()
    internal_page.click_template_domestic_file()
    time.sleep(5)
    internal_page.click_template_dropdown()
    internal_page.click_template_domestic_sourcelink_file()
    time.sleep(5)
    internal_page.click_template_dropdown()
    internal_page.click_template_international_file()
    time.sleep(5)
    internal_page.click_template_dropdown()
    internal_page.click_template_commerce_file()


#9.Validate the functionality of the "Back Arrow" button
def test_back_arrow(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    internal_page.click_back_arrow()
    assert internal_page.is_internal_displayed(), "Internal text not displayed"


#10.Validate file upload for "Template Domestic Payments"
def test_file_upload_domestic_payments(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    internal_page.click_template_dropdown()
    internal_page.click_template_domestic_file()
    # Resolve relative path dynamically
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/DOMESTIC.xlsx")
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    time.sleep(5)
    internal_page.click_validate_button()


#11.Validate file upload for "Template Domestic Payments with Source Link(s)
def test_file_upload_domestic_payments_sourcelink(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    internal_page.click_template_dropdown()
    internal_page.click_template_domestic_sourcelink_file()
    # Resolve relative path dynamically
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/DOMESTIC_SOURCE_LINK.xlsx")
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    time.sleep(5)
    internal_page.click_validate_button()


#12.Validate file upload for "Template International Payments
def test_file_upload_international_payments(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    internal_page.click_template_dropdown()
    internal_page.click_template_international_file()
    # Resolve relative path dynamically
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/INTERNATIONAL.xlsx")
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    time.sleep(5)
    internal_page.click_validate_button()


#13.Validate upload with invalid file format (e.g., PDF)
def test_invalid_file_upload(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    # Resolve relative path dynamically
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/Test.pdf")
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    time.sleep(5)
    error_message = internal_page.get_file_error_message()
    assert error_message is not None, "Error message should be displayed for invalid file."


#14.Validate upload with file exceeding size limit
def test_exceeding_sizelimit_file_upload(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    # Resolve relative path dynamically
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/Exceedsize(12MB).pdf")
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    time.sleep(5)
    error_message = internal_page.get_file_error_message()
    assert error_message is not None, "Error message should be displayed for invalid file."


#15.Validate the "Validate" button is disabled when no file is uploaded
def test_validate_button_disabled(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    internal_page.click_template_dropdown()
    internal_page.click_template_domestic_file()
    assert internal_page.is_validate_button_disabled(), "The 'Validate' button should be disabled when no file is uploaded."


#16.Validate file selection functionality and display of selected file
def test_validate_file_upload_name(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    internal_page.click_template_dropdown()
    internal_page.click_template_domestic_sourcelink_file()
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "../testdata/DOMESTIC_SOURCE_LINK.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    uploaded_file_name = internal_page.get_uploaded_file_name()
    assert uploaded_file_name == "DOMESTIC_SOURCE_LINK.xlsx", f"Expected file name 'DOMESTIC_SOURCE_LINK.xlsx', but got {uploaded_file_name}."


#17.Validate file upload completion and status update in the internal page
def test_validate_file_upload_completion(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    # assert internal_page.is_popup_message_displayed(), "Popup message 'We’re validating your file! This could take a few minutes.' was not displayed."
    internal_page.click_check_button()
    file_status = internal_page.get_file_status()
    assert file_status in ["Submitted",
                           "Validation"], f"Expected file status to be 'Submitted' or 'Validation', but got '{file_status}'."


#18.Validate the presence of details in the internal page after file validation
def test_file_details_after_validation(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    file_status = internal_page.get_file_status()
    assert file_status in ["Submitted",
                           "Validation"], f"Expected file status to be 'Submitted' or 'Validation', but got '{file_status}'."
    time.sleep(5)
    internal_page.click_status_button()
    time.sleep(5)
    assert "Total Payments" in internal_page.get_total_payments(), "Heading 'Total Payments' not found"
    # assert "Total Invoices" in internal_page.get_total_payments(), "Heading 'Total Invoices' not found"
    # assert "Errors" in internal_page.get_total_payments(), "Heading 'Errors' not found"

#19.Validate navigation to file status page from 'Submitted' status and check file details
def test_file_status(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    file_status = internal_page.get_file_status()
    assert file_status in ["Submitted",
                           "Validation"], f"Expected file status to be 'Submitted' or 'Validation', but got '{file_status}'."
    time.sleep(5)
    internal_page.click_status_button()
    time.sleep(5)
    assert "Total Payments" in internal_page.get_total_payments(), "Heading 'Total Payments' not found"
    # assert "Total Invoices" in internal_page.get_total_payments(), "Heading 'Total Invoices' not found"
    # assert "Errors" in internal_page.get_total_payments(), "Heading 'Errors' not found"

#20.Validate the functionality of 'Manual Batches Actions' for a submitted batch
def test_file_manual_batches_action(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    file_status = internal_page.get_file_status()
    assert file_status in ["Submitted",
                           "Validation"], f"Expected file status to be 'Submitted' or 'Validation', but got '{file_status}'."
    time.sleep(5)
    internal_page.click_status_button()
    time.sleep(5)
    internal_page.click_finalize_button()
    internal_page.click_continue_button()
    assert internal_page.is_manual_batches_actions_displayed(), "Manual Batches Actions' section is not displayed"
    assert internal_page.is_go_to_payments_button_displayed(), "Go to payments' button is not displayed"
    assert internal_page.is_download_pci_safe_original_button_displayed(), "Download PCI-safe Original' button is not displayed"
    assert internal_page.is_download_pci_safe_final_button_displayed(), "Download PCI-safe Final' button is not displayed"

#21.Validate the 'Go to payments' action in 'Manual Batches Actions'
def test_Goto_payment(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    file_status = internal_page.get_file_status()
    assert file_status in ["Submitted", "Validation"], f"Expected file status to be 'Submitted' or 'Validation', but got '{file_status}'."
    time.sleep(5)
    internal_page.click_status_button()
    time.sleep(5)
    internal_page.click_finalize_button()
    time.sleep(5)
    internal_page.click_continue_button()
    time.sleep(5)
    internal_page.click_check_back_later()
    time.sleep(5)
    internal_page.click_go_to_payment()
    assert internal_page.is_payment_page_displayed(), "payment page is not displayed"

#22.Validate the 'Download PCI-safe Original' action for a submitted batch
def test_download_picsafe_original(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    file_status = internal_page.get_file_status()
    assert file_status in ["Submitted", "Validation"], f"Expected file status to be 'Submitted' or 'Validation', but got '{file_status}'."
    time.sleep(5)
    internal_page.click_status_button()
    time.sleep(5)
    internal_page.click_finalize_button()
    time.sleep(5)
    internal_page.click_continue_button()
    time.sleep(5)
    internal_page.click_check_back_later()
    time.sleep(5)
    internal_page.click_download_pci()
    time.sleep(5)
    # download_dir = "C:/Users/Adithya G/Downloads"  # Update with your downloads folder
    # expected_file = "20250114-PNC_PCI-safeOriginal"  # Update with correct file name
    # internal_page.click_download_pci()
    #
    # assert internal_page.is_file_downloaded(download_dir, expected_file), "File not downloaded"
    #
    # # Optional: Verify file content
    # file_path = os.path.join(download_dir, expected_file)
    # assert os.path.getsize(file_path) > 0, "Downloaded file is empty"
    #
    # # Optional Cleanup
    # os.remove(file_path)

#23.Validate the 'Download PCI-safe Final' action for a submitted batch
def test_download_picsafe_final(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    file_status = internal_page.get_file_status()
    assert file_status in ["Submitted", "Validation"], f"Expected file status to be 'Submitted' or 'Validation', but got '{file_status}'."
    time.sleep(5)
    internal_page.click_status_button()
    time.sleep(5)
    internal_page.click_finalize_button()
    time.sleep(5)
    internal_page.click_continue_button()
    time.sleep(5)
    internal_page.click_check_back_later()
    time.sleep(5)
    internal_page.click_download_final_pci()
    time.sleep(5)

#24.Validate the 'Download Original' action for a submitted batch
def test_download_original(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    file_status = internal_page.get_file_status()
    assert file_status in ["Submitted", "Validation"], f"Expected file status to be 'Submitted' or 'Validation', but got '{file_status}'."
    time.sleep(5)
    internal_page.click_status_button()
    time.sleep(5)
    internal_page.click_finalize_button()
    time.sleep(5)
    internal_page.click_continue_button()
    time.sleep(5)
    internal_page.click_check_back_later()
    time.sleep(5)
    internal_page.click_download_original()
    time.sleep(5)
#25.Validate the 'Download Final' action for a submitted batch
def test_download_final(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    file_status = internal_page.get_file_status()
    assert file_status in ["Submitted", "Validation"], f"Expected file status to be 'Submitted' or 'Validation', but got '{file_status}'."
    time.sleep(5)
    internal_page.click_status_button()
    time.sleep(5)
    internal_page.click_finalize_button()
    time.sleep(5)
    internal_page.click_continue_button()
    time.sleep(5)
    internal_page.click_check_back_later()
    time.sleep(5)
    internal_page.click_download_final()
    time.sleep(5)

#26.Validate navigation to file status page from 'Validated' status and check for errors or warnings
def test_navigation_to_file_status_page(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    file_status = internal_page.get_file_status()
    expected_statuses = ["Submitted", "Validation"]
    assert file_status in expected_statuses, (
        f"Expected file status to be one of {expected_statuses}, but got '{file_status}'."
    )
    time.sleep(5)
    internal_page.click_status_button()
    time.sleep(5)
    assert internal_page.is_file_status_page_displayed(), "Failed to navigate to the file status page."
    error_warning_counts = internal_page.get_error_and_warning_counts()
    print(f"Error Count: {error_warning_counts['errors']}")
    print(f"Warning Count: {error_warning_counts['warnings']}")
    assert isinstance(error_warning_counts['errors'], int), "Error count is not a valid integer."
    assert isinstance(error_warning_counts['warnings'], int), "Warning count is not a valid integer."
    print("✅ Navigation and validation test passed successfully!")

#27.Validate the 'Download Latest File' action for a validated batch
def test_download_latest_file(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    file_status = internal_page.get_file_status()
    assert file_status in ["Submitted", "Validation"], f"Expected file status to be 'Submitted' or 'Validation', but got '{file_status}'."
    time.sleep(5)
    internal_page.click_status_button()
    time.sleep(5)
    internal_page.click_download_latest_file()
    time.sleep(5)

#28.Validate the 'Finalize Submission' functionality for a validated batch with warnings
def test_finalize_submission_with_warnings(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    file_status = internal_page.get_file_status()
    assert file_status in ["Submitted", "Validation"], f"Expected file status to be 'Submitted' or 'Validation', but got '{file_status}'."
    time.sleep(5)
    internal_page.click_status_button()
    time.sleep(5)
    assert internal_page.is_warning_message_displayed(), "Please check. This batch may be duplicated."
    internal_page.click_finalize_button()
    time.sleep(5)
    internal_page.click_continue_button()
    time.sleep(5)
    internal_page.click_check_back_later()
    time.sleep(5)

#29.Validate the 'Upload Again' functionality for a validated batch with warnings
def test_upload_again(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    file_status = internal_page.get_file_status()
    assert file_status in ["Submitted", "Validation"], f"Expected file status to be 'Submitted' or 'Validation', but got '{file_status}'."
    time.sleep(5)
    internal_page.click_status_button()
    time.sleep(5)
    internal_page.click_upload_again()
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/20250114-PNC_Latest.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_again_file(file_path)
    internal_page.click_again_validate_button()
    internal_page.click_again_check_back_button()
    assert internal_page.is_internal_validate_button_displayed(), "VALIDATED"

#30.Validate the 'Discard Batch' functionality for a validated batch
def test_discard_batch(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "../testdata/20250114-PNC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    time.sleep(5)
    file_status = internal_page.get_file_status()
    assert file_status in ["Submitted",
                           "Validation"], f"Expected file status to be 'Submitted' or 'Validation', but got '{file_status}'."
    time.sleep(5)
    internal_page.click_status_button()
    time.sleep(5)
    internal_page.click_discard_batch()
    time.sleep(3)
    internal_page.click_discard_batch_button()

# 31.Validate navigation to file status from 'Failed' header and error/warning count
def test_file_failed_status(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "../testdata/DOMESTIC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    time.sleep(5)
    # Wait for status to update
    file_status = internal_page.get_file_status()
    assert file_status == "Failed", f"Expected file status to be 'Failed', but got '{file_status}'."
    internal_page.click_failed_status_button()
    assert internal_page.is_file_status_page_displayed(), "Failed to navigate to the file status page."
    error_warning_counts = internal_page.get_error_and_warning_counts()
    print(f"Error Count: {error_warning_counts['errors']}")
    print(f"Warning Count: {error_warning_counts['warnings']}")
    assert isinstance(error_warning_counts['errors'], int), "Error count is not a valid integer."
    assert isinstance(error_warning_counts['warnings'], int), "Warning count is not a valid integer."
    print("✅ Navigation and validation test passed successfully!")
#     # file_status = internal_page.get_file_status()
#     # assert file_status in ["Submitted","Validation","Failed"], f"Expected file status to be 'Submitted' or 'Validation' or 'Failed', but got '{file_status}'."
#     file_status = internal_page.get_file_status()
#     if file_status in ["Submitted", "Validation", "Failed"]:
#         print(f"File status is: {file_status}")
#     else:
#         print("File status not found or unexpected.")
#     internal_page.click_failed_status_button()
#     time.sleep(5)
#     assert internal_page.is_file_status_page_displayed(), "Failed to navigate to the file status page."
#     error_warning_counts = internal_page.get_error_and_warning_counts()
#     print(f"Error Count: {error_warning_counts['errors']}")
#     print(f"Warning Count: {error_warning_counts['warnings']}")
#     assert isinstance(error_warning_counts['errors'], int), "Error count is not a valid integer."
#     assert isinstance(error_warning_counts['warnings'], int), "Warning count is not a valid integer."
#     print("✅ Navigation and validation test passed successfully!")

#32.Validate functionality of 'Download Original' button on a failed batch
def test_failed_batch_download_original(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "../testdata/DOMESTIC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    time.sleep(5)
    # file_status = internal_page.get_file_status()
    # assert file_status in ["Submitted","Validation","Failed"], f"Expected file status to be 'Submitted' or 'Validation' or 'Failed', but got '{file_status}'."
    file_status = internal_page.get_file_status()
    assert file_status == "Failed", f"Expected file status to be 'Failed', but got '{file_status}'."
    internal_page.click_failed_status_button()
    internal_page.click_download_original()

#33.Validate functionality of 'Download Latest File' button on a failed batch
def test_failed_batch_download_latest_file(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "../testdata/DOMESTIC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    time.sleep(5)
    # file_status = internal_page.get_file_status()
    # assert file_status in ["Submitted","Validation","Failed"], f"Expected file status to be 'Submitted' or 'Validation' or 'Failed', but got '{file_status}'."
    file_status = internal_page.get_file_status()
    assert file_status == "Failed", f"Expected file status to be 'Failed', but got '{file_status}'."
    internal_page.click_failed_status_button()
    internal_page.click_download_latest_file()
    time.sleep(5)


#34.Validate functionality of 'Upload Again' button on a failed batch
def test_failed_upload_again(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "../testdata/DOMESTIC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    time.sleep(5)
    # file_status = internal_page.get_file_status()
    # assert file_status in ["Submitted","Validation","Failed"], f"Expected file status to be 'Submitted' or 'Validation' or 'Failed', but got '{file_status}'."
    file_status = internal_page.get_file_status()
    assert file_status == "Failed", f"Expected file status to be 'Failed', but got '{file_status}'."
    internal_page.click_failed_status_button()
    time.sleep(5)
    internal_page.click_upload_again()
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    file_path = os.path.join(base_path, "../testdata/20250114-PNC_Latest.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_again_file(file_path)
    internal_page.click_again_validate_button()
    internal_page.click_again_check_back_button()
    assert internal_page.is_internal_validate_button_displayed(), "VALIDATED"

#35.Validate functionality of 'Discard Batch' button on a failed batch
def test_failed_batch_discard_batch(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "../testdata/DOMESTIC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    time.sleep(5)
    # file_status = internal_page.get_file_status()
    # assert file_status in ["Submitted","Validation","Failed"], f"Expected file status to be 'Submitted' or 'Validation' or 'Failed', but got '{file_status}'."
    file_status = internal_page.get_file_status()
    assert file_status == "Failed", f"Expected file status to be 'Failed', but got '{file_status}'."
    internal_page.click_failed_status_button()
    time.sleep(5)
    internal_page.click_discard_batch()
    time.sleep(3)
    internal_page.click_discard_batch_button()

#36.Validate functionality of 'Contact Production Support' button on a failed batch
def test_failed_batch_discard_batch(driver):
    internal_page = login_and_navigate_to_internal(driver)
    internal_page.click_internal_batch()
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "../testdata/DOMESTIC.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    print("Current working directory:", os.getcwd())
    print("Resolved file path:", file_path)
    internal_page.add_file(file_path)
    internal_page.click_validate_button()
    internal_page.click_check_button()
    time.sleep(5)
    # file_status = internal_page.get_file_status()
    # assert file_status in ["Submitted","Validation","Failed"], f"Expected file status to be 'Submitted' or 'Validation' or 'Failed', but got '{file_status}'."
    file_status = internal_page.get_file_status()
    assert file_status == "Failed", f"Expected file status to be 'Failed', but got '{file_status}'."
    internal_page.click_failed_status_button()
    time.sleep(5)
    internal_page.click_contact_production()



