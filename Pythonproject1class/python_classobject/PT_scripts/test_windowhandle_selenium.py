from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import allure


@pytest.mark.usefixtures("browser_cbt")
class Test_Practice():

    def test_practice_application(self, readJson):

        self.driver.get(readJson['letskodeit'])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        parent_window = self.driver.current_window_handle

        self.driver.find_element(By.XPATH, '//button[contains(text(), "Open Window")]').click()
        time.sleep(3)

        for windows in self.driver.window_handles:
            if windows != parent_window:
                self.driver.switch_to.window(windows)
                print(self.driver.current_url)
                print(self.driver.title)
                self.driver.close()
                time.sleep(4)

        self.driver.switch_to.window(parent_window)
        print(self.driver.current_url)
        print(self.driver.title)

    #Handling multiple tabs in a single window
    def test_tab_handle(self, readJson):
        self.driver.get(readJson['letskodeit'])  
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        original_tab = self.driver.current_window_handle

        # Store the ID of the original window
        original_tab = self.driver.current_window_handle

        # Click the link which opens in a new window
        self.driver.find_element(By.XPATH, "//a[text()='Open Tab']").click()
        time.sleep(1)

        for tab_handle in self.driver.window_handles:
            if tab_handle != original_tab:
                self.driver.switch_to.window(tab_handle)
                print(self.driver.current_url)
                print(self.driver.title)
                self.driver.close()
                time.sleep(2)
        
        self.driver.switch_to.window(original_tab)
        print(self.driver.current_url)
        print(self.driver.title)    