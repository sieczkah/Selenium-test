import unittest
from selenium import webdriver
from NewTab_page import *


class TestNewTabPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'D:\Selenium-GRID\chromedriver.exe')
        self.driver.get("https://formy-project.herokuapp.com/switch-window")

    def test_switch_tab(self):
        newtab_page = NewTabPage(self.driver)
        newtab_page.click_newtab()
        newtab_page.switch_tab()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

