import configparser
import logging
import os
from selenium import webdriver


def get_config():
    config = configparser.ConfigParser()
    config.read('C:/Users/Adithya G/formyself/BoostUI/configuration/config.ini')
    return config


def setup_logger():
    logging.basicConfig(filename='logs/test_logs.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger()


def take_screenshot(driver, filename):
    screenshot_path = os.path.join('screenshots', filename)
    driver.save_screenshot(screenshot_path)
    return screenshot_path


def get_browser(browser_name):
    if browser_name.lower() == "chrome":
        return webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        return webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")



def read_config(section, key):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'C:/Users/Adithya G/formyself/BoostUI/configuration/config.ini'))
    return config.get(section, key)
