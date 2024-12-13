

#import sys
#rom pathlib import Path
#sys.path.append(str(Path(__file__).parent.parent))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest
import time

@pytest.fixture(scope="function")
def browser_fun(request):
    print("initiating chrome driver")
    #driver = webdriver.Chrome("/Users/mithunroy/Downloads/chromedriver")
    print("initiating chrome driver")
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome()  # instanciating Chrome driver inside driver variable
    driver.maximize_window()
    driver.get("https://www.docker.com")
    driver.implicitly_wait(20)
    request.instance.driver = driver
    driver.maximize_window()

    yield driver

    driver.close()


@pytest.fixture(scope="class")
def browser_cls(request):
    print("initiating chrome driver")
    #driver = webdriver.Chrome("/Users/mithunroy/Downloads/chromedriver")
    print("initiating chrome driver")
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome()  # instanciating Chrome driver inside driver variable
    driver.maximize_window()
    driver.get("https://www.docker.com")
    driver.implicitly_wait(20)
    request.cls.driver = driver
    driver.maximize_window()

    yield driver

    driver.close()


@pytest.mark.usefixtures("browser_fun")
class TestDemo_Selenium():

    def test_docker_HomePage_Scenarios(self):

        self.driver.get("https://www.docker.com")
        self.driver.implicitly_wait(20)

        if self.driver.find_element(By.XPATH, "//li[@class='logo']").is_displayed():
            print("Logo is present....")
        else:
            print("Logo is not present....")

    def test_docker_HomePage_Scenarios1(self):

        self.driver.get("https://www.docker.com")
        self.driver.implicitly_wait(20)
        if self.driver.find_element(By.XPATH, "//li[@class='logo']").is_displayed():
            print("Logo is present....")
        else:
            print("Logo is not present....")

    def test_docker_HomePage_Scenarios3(self):

        if self.driver.find_element(By.XPATH, "//li[@class='logo']").is_displayed():
            print("Logo is present....")
        else:
            print("Logo is not present....")

    def test_launch_the_application(self):

        self.driver.get("https://www.saucedemo.com/")  # Using ".get" we can launch the URL.
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # login into the app
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.implicitly_wait(5)

        if self.driver.find_element(By.XPATH, "(//button[@type='button'])[1]").is_displayed():
            print("Login successfull")
        else:
            print("Login is unsuccessfull")

        self.driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()
        time.sleep(2)
        if self.driver.find_element(By.XPATH, "//input[@id='user-name']").is_displayed():
            print("logout is successfull")
