
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver


        self.dropdown =  '//*[@id="root"]/header/nav/div/ul/li[2]/button'
        self.dropdown_option = '//*[@id="Sources-tables"]/div[3]/ul/li[3]'
        self.internal_text = '//*[@id="root"]/div[2]/section/h3'

    def click_dropdown(self):
        self.driver.find_element(By.XPATH,self.dropdown).click()

    def select_dropdown_option(self):
        self.driver.find_element(By.XPATH,self.dropdown_option).click()

    def is_internal_displayed(self):
        """Check if 'Dynamic Boost Status' text is displayed on the dashboard."""
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.internal_text))
            ).is_displayed()
        except:
            return False