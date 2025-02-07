import time
import unittest
from selenium import webdriver
from pageObject.login import LoginPage
from utilities.utils import get_config, setup_logger, take_screenshot, get_browser
from pageObject.dashboard import DashboardPage
from pageObject.internal import InternalPage

#
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
        dashboard_page = DashboardPage(self.browser)
        dashboard_page.click_dropdown()
        dashboard_page.select_dropdown_option()
        self.assertTrue(dashboard_page.is_internal_displayed(),
                        "Internal text not display")
        self.logger.info("internal text is display")
        time.sleep(10)
        internal_page = InternalPage(self.browser)
        internal_page.click_internal_batch()
        time.sleep(10)
        self.assertTrue(internal_page.is_adding_batch_displayed(), "Adding New Entries text not display")
        self.logger.info("Adding New Entries is display")