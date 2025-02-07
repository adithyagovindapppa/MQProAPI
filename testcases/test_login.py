import unittest
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

    # @classmethod
    # def tearDownClass(cls):
    #     cls.browser.quit()


if __name__ == "__main__":
    unittest.main()
