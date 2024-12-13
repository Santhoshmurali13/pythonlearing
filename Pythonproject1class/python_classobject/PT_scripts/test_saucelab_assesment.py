from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest
import time



@pytest.mark.usefixtures("browser_cbt") #using fixtures with defined scope
class TestDemo_assesment():

    def test_launch_the_application(self, readJson):

        self.driver.get(readJson['url_saucelab'])  
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # login into the app
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(readJson['username'])
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(readJson['password'])
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.implicitly_wait(5)

        if self.driver.find_element(By.XPATH, "(//button[@type='button'])[1]").is_displayed():
            print("Login successfull")
        else:
            print("Login is unsuccessfull")

        #validate url
        current_url = self.driver.current_url
        if readJson['url_saucelab'] in current_url:
            print("Current Url is as Expected")
        else:
            print("Current url is not as expected url")

        #validate title
        title = self.driver.title
        print(title)
        if title == readJson['sauce_title']:
            print("Title Is As Expected")
        else:
            print("Title text is not as expected")    
        self.driver.find_element(By.XPATH, "//span[@data-test='title' and text()='Products']").is_displayed()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bike-light']").click()
        self.driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge']").is_displayed()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge' and text()='2']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='remove-sauce-labs-backpack']").is_displayed()
        self.driver.find_element(By.XPATH, "//button[@data-test='remove-sauce-labs-bike-light']").is_displayed()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@data-test='remove-sauce-labs-backpack']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge' and text()='1']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='continue-shopping']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-fleece-jacket']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='checkout']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@data-test='firstName']").send_keys(readJson['username1'])
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@data-test='lastName']").send_keys(readJson['lastname'])
        self.driver.find_element(By.XPATH, "//input[@data-test='postalCode']").send_keys(readJson['postal'])
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@data-test='continue']").click()
        price_text = self.driver.find_element(By.XPATH, "//div[@data-test='subtotal-label']").text
        price = price_text.replace("Item total: $", "")
        tax_text = self.driver.find_element(By.XPATH, "//div[@data-test='tax-label']").text
        tax = tax_text.replace("Tax: $", "")
        total_text = self.driver.find_element(By.XPATH, "//div[@data-test='total-label']").text
        total = total_text.replace("Total: $", "")
        if float(total) == float(price) + float(tax):
            print("Total value is the sum of price and tax")
        else:
            print("Total value is not the sum of price and tax")
        self.driver.find_element(By.XPATH, "//button[@data-test='finish']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//h2[@data-test='complete-header']").is_displayed()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Back Home')]").click()
        time.sleep(5)




    