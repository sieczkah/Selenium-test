import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Webform_page import *
from Confirmation_page import *

firstname = 'Hubert'
lastname = 'Sieczka'
jobtitle = 'Electric Designer'
date = '03/15/2021'
EXPECTED_ALERT = 'The form was successfully submitted!'


class TestRadioButtonPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'D:\Selenium-GRID\chromedriver.exe')
        self.driver.get("https://formy-project.herokuapp.com/form")

    def test_webform_page(self):
        webform_page = WebFormPage(self.driver, Keys)
        webform_page.submit_form(firstname, lastname, jobtitle, date)

        confirmation_page = ConfirmationPage(self.driver)
        confirmation_page.wait_for_alert(WebDriverWait, EC, By)

        self.assertEqual(EXPECTED_ALERT, confirmation_page.get_alert_text())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
