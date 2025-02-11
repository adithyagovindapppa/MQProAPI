from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.email_field = "email"
        self.password_field = "password"
        self.submit_button = '//*[@id="root"]/div/div/form/button[2]'
        self.dashboard_text = "//*[@id='root']/section/header/div[1]/h1"
        self.error_message = "//*[@id='root']/div/div[1]/div/div[1]"
        self.forgot_password = "//*[@id='root']/div/div/form/button[1]"
        self.forgot_text = "//*[@id='root']/div/div/form/h2"
        self.back_button = "//*[@id='root']/div/div/form/button[1]"

    def enter_email(self, username):
        self.driver.find_element(By.ID,self.email_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID,self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.submit_button).click()

    def is_dynamic_boost_status_displayed(self):
        """Check if 'Dynamic Boost Status' text is displayed on the dashboard."""
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.dashboard_text))
            ).is_displayed()
        except:
            return False

    def get_error_message(self):
        try:
            return self.driver.find_element(By.XPATH, self.error_message).text
        except NoSuchElementException:
            return None

    def is_sign_button_enabled(self):
        """Check if the sign in (submit) button is enabled."""
        try:
            return self.driver.find_element(By.XPATH, self.submit_button).is_enabled()
        except NoSuchElementException:
            return False
    def click_forgot(self):
        self.driver.find_element(By.XPATH,self.forgot_password).click()

    def is_forgot_password_displayed(self):
        """Check if 'Dynamic Boost Status' text is displayed on the dashboard."""
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.forgot_text))
            ).is_displayed()
        except:
            return False

    def click_backbutton(self):
        self.driver.find_element(By.XPATH,self.back_button).click()


