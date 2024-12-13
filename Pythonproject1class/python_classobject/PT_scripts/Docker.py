from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
from time import sleep


class Testqualitrix:
    
    def test_001(self):
        global driver
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # Prevents browser from closing

        # Instantiate the WebDriver with options
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        driver.quit()