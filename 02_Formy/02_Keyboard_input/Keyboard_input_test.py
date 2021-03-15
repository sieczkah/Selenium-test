import unittest
from selenium import webdriver
from Keyboard_input import *

fullname = "Kubi Bubi"


class TestKeyboardAndMouse(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\Selenium-GRID\chromedriver.exe')
        self.driver.get("https://formy-project.herokuapp.com/keypress")

    def test_KeyboardInput(self):
        keyboard_page = KeyboardAndMouseInput(self.driver)
        keyboard_page.enter_name(fullname)
        keyboard_page.submit_button()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()