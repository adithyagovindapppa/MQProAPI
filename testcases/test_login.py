import unittest
import time
from selenium import webdriver
from pageObject.login import LoginPage
from utilities.utils import get_config, setup_logger, take_screenshot, get_browser
from pageObject.dashboard import DashboardPage


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = get_config()
        cls.logger = setup_logger()
        cls.browser = get_browser(cls.config['WEB']['browser'])
        cls.browser.get(cls.config['WEB']['base_url'])
        cls.browser.implicitly_wait(30)

    def test_login(self):
        login_page = LoginPage(self.browser)
        # print("username : " + self.config['CREDENTIALS']['username'])
        login_page.enter_email(self.config['CREDENTIALS']['username'])
        login_page.enter_password(self.config['CREDENTIALS']['password'])
        login_page.click_login()
        self.assertTrue(login_page.is_dynamic_boost_status_displayed(),
                        "Dynamic Boost Status text not found on the dashboard")
        self.logger.info("Dynamic Boost Status text is present on the dashboard")

    def test_invalid_email_login(self):
        login_page = LoginPage(self.browser)
        login_page.enter_email(self.config['CREDENTIALS']['invalidusername'])
        login_page.enter_password(self.config['CREDENTIALS']['password'])
        login_page.click_login()
        time.sleep(10)  # Consider using an explicit wait instead of sleep
        error_message = login_page.get_error_message()
        expected_error_message = "You’ve entered an invalid email / password combination, or your account is locked due to too many login attempts."
        self.assertIsNotNone(error_message, "Error message should be displayed")
        self.assertEqual(error_message, expected_error_message, f"Error message should be: {expected_error_message}")

    def test_empty_username_password(self):
        login_page = LoginPage(self.browser)
        login_page.enter_email(self.config['CREDENTIALS']['emptyusername'])
        login_page.enter_password(self.config['CREDENTIALS']['emptypassword'])
        self.assertFalse(login_page.is_sign_button_enabled(),
                         "Sign button should be disabled when email and password are empty")

    def test_invalid_password_login(self):
        login_page = LoginPage(self.browser)
        login_page.enter_email(self.config['CREDENTIALS']['username'])
        login_page.enter_password(self.config['CREDENTIALS']['invaidpassword'])
        login_page.click_login()
        time.sleep(10)  # Consider using an explicit wait instead of sleep
        error_message = login_page.get_error_message()
        expected_error_message = "You’ve entered an invalid email / password combination, or your account is locked due to too many login attempts."
        self.assertIsNotNone(error_message, "Error message should be displayed")
        self.assertEqual(error_message, expected_error_message, f"Error message should be: {expected_error_message}")

    def test_empty_password(self):
        login_page = LoginPage(self.browser)
        login_page.enter_email(self.config['CREDENTIALS']['username'])
        login_page.enter_password(self.config['CREDENTIALS']['emptypassword'])
        self.assertFalse(login_page.is_sign_button_enabled(),
                         "Sign button should be disabled when email and password are empty")

    def test_empty_email(self):
        login_page = LoginPage(self.browser)
        login_page.enter_email(self.config['CREDENTIALS']['emptyusername'])
        login_page.enter_password(self.config['CREDENTIALS']['password'])
        # self.assertFalse(login_page.is_sign_button_enabled(),
        #                  "Sign button should be disabled when email empty")

    def test_special_char_email(self):
        login_page = LoginPage(self.browser)
        login_page.enter_email(self.config['CREDENTIALS']['specialcharemail'])
        login_page.enter_password(self.config['CREDENTIALS']['password'])
        self.assertFalse(login_page.is_sign_button_enabled(),
                         "Sign button should be disabled when email and password are empty")

    def test_forgot_password(self):
        login_page = LoginPage(self.browser)
        time.sleep(5)
        login_page.click_forgot()
        time.sleep(5)
        self.assertTrue(login_page.is_forgot_password_displayed(),
                        "Forgot your password? text not found on the forgot password page")
        self.logger.info("Forgot your password?  text is present on the forgot password page")

    def test_back_button(self):
        login_page = LoginPage(self.browser)
        time.sleep(5)
        login_page.click_forgot()
        time.sleep(5)
        self.assertTrue(login_page.is_forgot_password_displayed(),
                        "Forgot your password? text not found on the forgot password page")
        self.logger.info("Forgot your password?  text is present on the forgot password page")
        login_page.click_backbutton()


if __name__ == "__main__":
    unittest.main()
