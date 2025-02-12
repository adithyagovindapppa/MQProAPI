# File: utilities/utils.py

import configparser
import logging
import os
from selenium import webdriver

def get_config():
    config = configparser.ConfigParser()
    # Build a relative path to your config.ini file
    config_path = os.path.join(os.path.dirname(__file__), '..', 'C:/Users/Adithya G/formyself/postboost/configuration/config.ini')
    config.read(config_path)
    return config

def setup_logger():
    # Create logs directory if it doesn't exist
    log_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'test_logs.log')
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    logging.basicConfig(filename=log_path, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger()

def take_screenshot(driver, filename):
    screenshot_path = os.path.join(os.path.dirname(__file__), '..', 'screenshots', filename)
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
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
    config_path = os.path.join(os.path.dirname(__file__), '..', 'C:/Users/Adithya G/formyself/postboost/configuration/config.ini')
    config.read(config_path)
    return config.get(section, key)
