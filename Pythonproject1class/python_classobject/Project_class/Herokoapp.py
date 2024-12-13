from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Automation:

    def launch_the_application(self):

        global driver  #making driver as global variable
        driver = webdriver.Chrome()  #instanciating Chrome driver inside driver valriable
        driver.get("https://the-internet.herokuapp.com/") # Using ".get" we can launch the URL.
        driver.maximize_window()

    # def validate_how_to_select_dropdown(self):

    #     driver.find_element(By.XPATH, "//a[text()='Dropdown']").click()
    #     driver.implicitly_wait(5)
    #     select = Select(driver.find_element(By.XPATH, "//select[@id='dropdown']"))
  
    #     select.select_by_visible_text("Option 1")
    #     time.sleep(2)

    #     select.select_by_visible_text("Option 2")
    #     time.sleep(2)

    #     select.select_by_index(1)
    #     time.sleep(2)

    #     select.select_by_index(2)
    #     time.sleep(2)

    def handle_checkbox(self):
        #validate checkbox 1 is not checked and checkbox 2 is check by default.
        #select checkbox 1 and validate checkbox 1 is selected.
        #uncheck checkbox 2 and validate checkbox 2 is not selected.
        driver.find_element(By.XPATH, "//a[text()='Checkboxes']").click()
        driver.implicitly_wait(5)
        #boolean is the concept to validate radio button and check box
        checkbox_1 = driver.find_element(By.XPATH, "//input[@type='checkbox'][1]").is_selected()  #validating the checkbox1
        checkbox_2 = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]").is_selected() #validating the checkbox2
        print(checkbox_1)
        print(checkbox_2)
        if checkbox_1 == False:
            print("checkbox1 is not checked by default as expected")
        if checkbox_2 == True:
            print("checkbox2 is checked by default as expected")

#uncheck checkbox 2 and check the Checkbox1:
        driver.find_element(By.XPATH, "//input[@type='checkbox'][1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@type='checkbox'][2]").click()
        time.sleep(2)

        checkbox_1 = driver.find_element(By.XPATH, "//input[@type='checkbox'][1]").is_selected()
        checkbox_2 = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]").is_selected()
        print(checkbox_1)
        print(checkbox_2)
        if checkbox_1 == True:
            print("checkbox1 is now checked after checking it")
        if checkbox_2 == False:
            print("checkbox2 is now not checked after unchecking it")


obj = Automation()
obj.launch_the_application()
# obj.validate_how_to_select_dropdown()
obj.handle_checkbox()
#obj.close_the_application()