from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from faker import Faker
import time
import unittest
import logging


fake = Faker(["id_ID"])
base_url = "https://www.lambdatest.com/selenium-playground"

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(base_url)
        self.action = ActionChains(self.driver)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class Scenario001(BaseTest):
    def test_001(self):

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
        time.sleep(5)



