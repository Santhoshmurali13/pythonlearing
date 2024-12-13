from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from time import sleep


class Swaglabs:

    def launch_swaglabs_application(self):
        global driver
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # Prevents browser from closing

        # Instantiate the WebDriver with options
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

    def validate_swaglabs_logo(self):
        Logo = driver.find_element(By.CLASS_NAME, "login_logo").is_displayed()
        if Logo:
            print("Login Logo Is displayed")
        else:
            print("Login Logo is not displayed")

    def login_into_application(self):
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        sleep(2)
        driver.find_element(By.NAME, "login-button").click()
        driver.implicitly_wait(5)
        Logged_in = driver.find_element(By.XPATH, "//span[text()='Products']").is_displayed()
        if Logged_in:
            print("User Logged In Successfully")
        else:
            assert False, "Login Failed! Check the Credentials"

    def click_on_menu(self):
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        driver.implicitly_wait(5)

    def logout_of_application(self):
        driver.find_element(By.ID, "logout_sidebar_link").click()
        driver.implicitly_wait(5)
        Logo = driver.find_element(By.CLASS_NAME, "login_logo").is_displayed()
        if Logo:
            print("User Logged Out Successfully")
        else:
            print("Failed To Log Out Successfully")
        sleep(3)

    def close_the_application(self):
        driver.quit()


Swag = Swaglabs()
Swag.launch_swaglabs_application()
Swag.validate_swaglabs_logo()
Swag.login_into_application()
Swag.click_on_menu()
Swag.logout_of_application()
Swag.close_the_application()