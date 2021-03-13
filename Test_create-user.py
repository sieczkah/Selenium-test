import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from random import randint


class TestCreateUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:\Program Files (x86)\geckodriver.exe")

    def test_userCreate(self):
        """ Testing Creation of user"""
        driver = self.driver
        driver.get("https://selenium-blog.herokuapp.com/signup")
        username = 'Hubib' + str(randint(1,100))
        password = "password"
        email = f'{username}@com.com'
        username_field = driver.find_element_by_id("user_username")
        username_field.send_keys(username)

        email_field = driver.find_element_by_id("user_email")
        email_field.send_keys(email)

        password_field = driver.find_element_by_id("user_password")
        password_field.send_keys(password)

        submit_button = driver.find_element_by_id("submit")
        submit_button.click()

        banner = driver.find_element_by_id("flash_success")
        banner_text = banner.text
        self.assertEqual(banner_text, f"Welcome to the alpha blog {username}")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()