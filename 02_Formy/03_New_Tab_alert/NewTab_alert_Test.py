import unittest
from selenium import webdriver
from NewTab_alert import *
from time import sleep


class TestNewtabAlert(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'D:\Selenium-GRID\chromedriver.exe')
        self.driver.get("https://formy-project.herokuapp.com/switch-window")

    def test_close_alert(self):
        alert_page = NewTabAlert(self.driver)
        alert_page.click_alert()
        sleep(2)
        alert_page.close_alert()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
