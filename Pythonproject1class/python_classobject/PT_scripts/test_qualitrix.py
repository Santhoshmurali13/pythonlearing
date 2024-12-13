from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class Test_Qualitrix:

    def test_launch_qualitrix_application(self):
        global driver
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # Prevents browser from closing

        # Instantiate the WebDriver with options
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://qualitrix.com/")
        driver.maximize_window()

    def test_print_links(self):
        total_links = driver.find_elements(By.XPATH, "//a")
        for i in range(1, len(total_links)+1):
            xpath_format = "(//a)[{}]".format(str(i))
            print(xpath_format)
            link = driver.find_element(By.XPATH, xpath_format).text
            print("When the value of i is : " + str(i) + " " + "the link is : " + str(link))

    def test_print_images(self):
        total_links = driver.find_elements(By.XPATH, "//img")
        for i in range(1, len(total_links)+1):
            xpath_format = '(//img)['+str(i)+']'
            print(xpath_format)
            image = driver.find_element(By.XPATH, xpath_format).get_attribute('src')
            print("When the value of i is : " + str(i) + " " + "the image is : " + str(image))

    def test_print_all_links(self):

        total_links_count = len(driver.find_elements(By.XPATH, "//a"))

        file = open("D:\pythonproject\python_classobject\link.txt", "w")  #open a file
        for i in range(1,  total_links_count+1):
            
            xpath = '(//a)['+str(i)+']'
            link_name = driver.find_element(By.XPATH, xpath).text
            #print("When the value of i is: " + str(i) + " " + "the value of text is: " + link_name)
            #write data in the txt file
            file.write("When the value of i is: " + str(i) + " " + "the value of text is: " + link_name) 
            file.write("\n") # to enter into next line
         
        file.close()  # close a file
        print("Data is written into the file.")
        driver.quit()

