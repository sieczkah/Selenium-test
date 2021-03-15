import unittest
from selenium import webdriver
from Radio_page import *
from time import sleep


class TestRadioButtonPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'D:\Selenium-GRID\chromedriver.exe')
        self.driver.get("https://formy-project.herokuapp.com/radiobutton")

    def test_radio_buttons(self):
        radio_button_page = RadioPage(self.driver)
        radio_button_page.select_button_1()
        sleep(1)
        radio_button_page.select_button_2()
        sleep(1)
        radio_button_page.select_button_3()
        sleep(1)
        radio_button_page.select_button_1()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
