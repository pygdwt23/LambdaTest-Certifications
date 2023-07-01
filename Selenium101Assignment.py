from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
from faker import Faker
import time
import unittest
import logging
import os


fake = Faker()
base_url = "https://www.lambdatest.com/selenium-playground"
username = "pygdwt"
accessKey = "YkgRYdljv0S3A2Ai7Q3crv1YvREzhvY07MMy1NrLZ1ivam6n2F"
gridUrl = "hub.lambdatest.com/wd/hub"


url = "https://"+(username)+":"+accessKey+"@"+gridUrl

class BaseTest(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome()
        # chrome_options = webdriver.ChromeOptions()
            capability = {
	            "browserName": "Chrome",
	            "browserVersion": "latest",
	            "LT:Options": {
		            "username": "pygdwt",
		            "accessKey": "YkgRYdljv0S3A2Ai7Q3crv1YvREzhvY07MMy1NrLZ1ivam6n2F",
		            "visual": True,
		            "video": True,
		            "platformName": "Windows 10",
		            "build": "Selenium101Assignment",
		            "project": "UntitledSelenium101Assignment",
		            "name": "Selenium101Assignment"
	            }
            }
            self.driver = webdriver.Remote(command_executor=url,desired_capabilities=capability)
            self.driver.maximize_window()
            self.driver.get(base_url)
            self.action = ActionChains(self.driver)
        
    def tearDown(self):
        self.driver.quit()


class Scenario001(BaseTest):
    def test_001(self):
        print("=============================================================================================================================")
        print("02. SCENARIO 001 IS RUNNING")
    # Step 1 - Click “Simple Form Demo” under Input Forms.
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//a[.='Simple Form Demo']"))).click()

    # Step 2 - Validate that the URL contains “simple-form-demo”.
        get_url = self.driver.current_url
        print("URL: %s" %get_url)
        url_contains = self.driver.find_element(By.XPATH, "//link[1]")
        url_expected_contain = "simple-form-demo"
        if url_contains.text in url_expected_contain:
            print("The url validation is PASS and contain %s" %url_expected_contain)
        else:
            print("The url validation is FAIL")

    # Step 3 -  Create a variable for a string value E.g: “Welcome to LambdaTest”.
        your_message = "Hello! " + fake.name() + ", Welcome to the LambdaTest Selenium Certification."

    # Step 4 - Use this variable to enter values in the “Enter Message” text box.
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-message']"))).send_keys(your_message)

    # Step 5 - Click “Get Checked Value”.
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='showInput']"))).click()

    # Step 6 - Validate whether the same text message is displayed in the right-hand panel under the “Your Message:” section.
        righHandPanel = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//p[@id='message']"))).text
        self.assertEqual(your_message, righHandPanel)
        print("EXPECTED: %s" %your_message, "ACTUAL: %s" %righHandPanel)
        self.driver.get_screenshot_as_file("scenario001.png")
        print("scenario001.png is captured succesfully")
        time.sleep(5)
        print("RESULT: SCENARIO_001 IS PASS")



class Scenario002(BaseTest):
    def test_002(self):
        print("=============================================================================================================================")
        print("02. SCENARIO 002 IS RUNNING")
    # Step 1 - Open the https://www.lambdatest.com/selenium-playground page and click “Drag & Drop Sliders” under “Progress Bars & Sliders”.
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//a[.='Drag & Drop Sliders']"))).click()

    # Step 2 - Select the slider “Default value 15” and drag the bar to make it 95 by validating whether the range value shows 95.
        source = self.driver.find_element(By.XPATH, "//input[@value='15']")
        self.action.drag_and_drop_by_offset(source, 215, 0).perform()
        time.sleep(5)

        rangeSuccess = self.driver.find_element(By.XPATH, "//output[@id='rangeSuccess']").text
        expectedRange = 95
        self.assertEqual(int(rangeSuccess), expectedRange)
        self.driver.get_screenshot_as_file("scenario002.png")
        print("scenario002.png is captured succesfully")
        print("EXPECTED: %s" %expectedRange, "ACTUAL: %s" %rangeSuccess)
        print("RESULT: SCENARIO_002 IS PASS")


if __name__ == '__main__':
    unittest.main()