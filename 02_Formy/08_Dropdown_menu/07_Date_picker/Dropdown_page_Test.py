import unittest
from selenium import webdriver
from DropDown_page import *
from selenium.webdriver.common.keys import Keys
from time import sleep


class TestRadioButtonPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'D:\Selenium-GRID\chromedriver.exe')
        self.driver.get("https://formy-project.herokuapp.com/dropdown")

    def test_dropdown_menu(self):
        dropdown_page = DropdownPage(self.driver)
        dropdown_page.dropdown_select()
        sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
