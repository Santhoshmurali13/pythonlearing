from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep


class Heroko_Automation:

    def launch_the_application(self):

        global driver  # making driver as global variable
        driver = webdriver.Chrome()  # instanciating Chrome driver inside driver valriable
        driver.get("https://the-internet.herokuapp.com/")  # Using ".get" we can launch the URL.
        driver.maximize_window()

    def checkbox_verification(self):

        driver.find_element(By.XPATH, "//a[text()='Checkboxes']").click()
        driver.implicitly_wait(5)
        #boolean is the concept to validate radio button and check box
        checkbox_1 = driver.find_element(By.XPATH, "//input[@type='checkbox'][1]").is_selected()  # validating the checkbox1
        checkbox_2 = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]").is_selected()  # validating the checkbox2
        print(checkbox_1)
        print(checkbox_2)
        if checkbox_1 is False:
            print("checkbox1 is not checked by default as expected")
        if checkbox_2 is True:
            print("checkbox2 is checked by default as expected")

        #uncheck checkbox 2 and check the Checkbox1:
        driver.find_element(By.XPATH, "//input[@type='checkbox'][1]").click()
        sleep(2)
        driver.find_element(By.XPATH, "//input[@type='checkbox'][2]").click()
        sleep(2)

        checkbox_1 = driver.find_element(By.XPATH, "//input[@type='checkbox'][1]").is_selected()
        checkbox_2 = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]").is_selected()
        print(checkbox_1)
        print(checkbox_2)
        if checkbox_1 is True:
            print("checkbox1 is now checked after checking it")
        if checkbox_2 is False:
            print("checkbox2 is now not checked after unchecking it")

    def close_the_application(self):
        driver.quit()


obj = Heroko_Automation()
obj.launch_the_application()
obj.checkbox_verification()
obj.close_the_application()
