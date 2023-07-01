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
		            "project": "Selenium101Assignment",
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
        print("01. SCENARIO 001 IS RUNNING")
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
        if self.driver.find_element(By.XPATH, "//p[@id='message']").is_displayed:
            self.driver.execute_script("lambda-status=passed")
            print("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")
            print("lambda-status=failed")

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
        if self.driver.find_element(By.XPATH,"//output[@id='rangeSuccess']").is_displayed:
            self.driver.execute_script("lambda-status=passed")
            print("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")
            print("lambda-status=failed")

class Scenario003(BaseTest):
    def test_003(self):
        print("=============================================================================================================================")
        print("03. SCENARIO 003 IS RUNNING")
    # Step 1 - Open the https://www.lambdatest.com/selenium-playground page and click “Input Form Submit” under “Input Forms”.
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//a[.='Input Form Submit']"))).click()

    # Step 2 - Click “Submit” without filling in any information in the form.
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))).click()

    # Step 3 - Assert “Please fill in the fields” error message.
        errorMsg = self.driver.find_element(By.XPATH, "//input[@id='name']").get_attribute(name="validationMessage")
        expectedErrorMsg = "Please fill out this field."
        self.assertEqual(errorMsg, expectedErrorMsg)
        print(errorMsg)
        self.driver.get_screenshot_as_file("scenario003_a.png")
        time.sleep(5)

    # Step 4 - Fill in Name, Email, and other fields.
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).send_keys(fake.name())
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Email']"))).send_keys(fake.ascii_safe_email())
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys("LambdaTest@2023")
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='company']"))).send_keys(fake.company())
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='websitename']"))).send_keys(fake.url())

    # Step 5 - From the Country drop-down, select “United States” using the text property.
        countrySelect = Select(self.driver.find_element(By.XPATH, "//select[@name='country']"))
        countrySelect.select_by_value("US")
        self.driver.get_screenshot_as_file("scenario003_b.png")

        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inputCity']"))).send_keys(fake.city())
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Address 1']"))).send_keys(fake.address())
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Address 2']"))).send_keys(fake.address())
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inputZip']"))).send_keys(fake.postcode())
        self.driver.get_screenshot_as_file("scenario003_c.png")
        time.sleep(5)
    # Step 6 - Fill all fields and click “Submit”.
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))).click()

    # Step 7 - Once submitted, validate the success message “Thanks for contacting us, we will get back to you shortly.” on the screen.
        time.sleep(5)
        self.driver.get_screenshot_as_file("scenario003_d.png")
        if WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='success-msg hidden']"))).is_displayed():
            successMsg = self.driver.find_element(By.XPATH, "//p[@class='success-msg hidden']").text
            print(successMsg)
            expectedSuccessMsg = "Thanks for contacting us, we will get back to you shortly."
            self.assertEqual(expectedSuccessMsg, successMsg)
            self.driver.execute_script("lambda-status=passed")
            print("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")
            print("lambda-status=failed")


if __name__ == '__main__':
    unittest.main()