from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from Locators import Qualitrix_home
import pytest
import time


class Qualitrix_page_object:

    def __init__(self, driver):
        self.driver = driver

    def launch_the_app(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        print("Qualitrix Application is launched Successfully ... ..... PASS")

    def Validate_header_menu(self):
        assert len(self.driver.find_elements(By.XPATH, Qualitrix_home.Qualitrix_logo())) == 1
        assert self.driver.find_element(By.XPATH, Qualitrix_home.Qualitrix_logo()).is_displayed() == True
        print("Qualitrix logo is present")