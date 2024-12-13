from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import allure


class Py_Cons:

    #def __init__(self):
        #print("This is called a default Constructor ......")

    def __init__(self, name, age):
        self.name = name
        self.age = age  


obj = Py_Cons("Santhosh", 35)
print(obj.name)
print(obj.age)