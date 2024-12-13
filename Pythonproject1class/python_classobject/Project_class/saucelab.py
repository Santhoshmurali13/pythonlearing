from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class sauce:

    def launch_the_application(self):

        global driver  #making driver as global variable
        driver = webdriver.Chrome()  #instanciating Chrome driver inside driver valriable
        driver.get("https://www.saucedemo.com/") # Using ".get" we can launch the URL.
        driver.maximize_window()

    def validate_login(self):

        driver.find_element(By.XPATH,   "//div[text()='Swag Labs']").is_displayed()
        print("logo is present")

    def login():
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        time.sleep(1)

obj = sauce()
obj.launch_the_application()
obj.validate_login()
