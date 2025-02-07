
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class InternalPage:
    def __init__(self, driver):
        self.driver = driver

        self.internal_text = '//*[@id="root"]/div[2]/section/h3'
        self.internal_batch = '//*[@id="grid-actions"]/button[1]'
        self.adding_text ='//*[@id="root"]/h1'

    def is_internal_displayed(self):
        """Check if 'Dynamic Boost Status' text is displayed on the dashboard."""
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.internal_text))
            ).is_displayed()
        except:
            return False

    def click_internal_batch(self):
        self.driver.find_element(By.XPATH,self.internal_batch).click()



    def is_adding_batch_displayed(self):

        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.adding_text))
            ).is_displayed()
        except:
            return False

