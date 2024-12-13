from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time
from time import sleep


class Testalert:
    
    def test_001(self):
        global driver
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # Prevents browser from closing

        # Instantiate the WebDriver with options
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Edge()
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//a[text()='JavaScript Alerts']").click()
        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        
        alert = Alert(driver)
        print(alert.text)

        alert.accept()
        time.sleep(2)
        Alert_Handled = driver.find_element(By.XPATH, '//p[text()="You successfully clicked an alert"]').is_displayed()
        if Alert_Handled:
            print("Alert Handled As Expected")
        else:
            print("Alert Handled Success Message Is Not Ddisplayed")

        #Click for JS Confirm
        driver.find_element(By.XPATH, '//button[text()="Click for JS Confirm"]').click()
        print(alert.text)
        alert.dismiss()
        time.sleep(3)
        Alert_Handled = driver.find_element(By.XPATH, '//p[text()="You clicked: Cancel"]').is_displayed()
        if Alert_Handled:
            print("Dismissed Alert Success Message Is Displayed")
        else:
            print("Dismissed Alert Success Message Is Not Ddisplayed")    

        driver.quit()





        