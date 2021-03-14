import unittest
from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from random import randint
import SignUp_page
import UserPage

username = 'Hubib' + str(randint(1, 100))
password = "password"
email = f'{username}@com.com'
expected_banner_text = f"Welcome to the alpha blog {username}"


class TestCreateUser(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Remote(
        #     # command_executor='http://192.168.0.14:4444/wd/hub',
        #     # desired_capabilities=DesiredCapabilities.FIREFOX)
        # self.driver = webdriver.Firefox(executable_path=r"C:\Program Files (x86)\geckodriver.exe")
        self.driver = webdriver.Chrome(executable_path=r'D:\Selenium-GRID\chromedriver.exe')

    def test_userCreate(self):
        """ Testing Creation of user"""
        driver = self.driver
        driver.get("https://selenium-blog.herokuapp.com/signup")
        signup = SignUp_page.SignupPage(driver)

        signup.enter_username(username)
        signup.enter_email(email)
        signup.enter_password(password)
        signup.submit_form()

        users_page = UserPage.UserPage(driver)
        banner_text = users_page.get_banner_text()
        self.assertEqual(banner_text, expected_banner_text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
