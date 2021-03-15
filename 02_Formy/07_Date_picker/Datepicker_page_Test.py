import unittest
from selenium import webdriver
from Datepicker_page import *
from selenium.webdriver.common.keys import Keys
from time import sleep


class TestRadioButtonPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'D:\Selenium-GRID\chromedriver.exe')
        self.driver.get("https://formy-project.herokuapp.com/datepicker")
        self.keys = Keys

    def test_date_pick(self):
        datepicker_page = DatePickerPage(self.driver, self.keys)
        datepicker_page.pick_date()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
