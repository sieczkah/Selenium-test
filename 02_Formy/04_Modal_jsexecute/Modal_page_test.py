import unittest
from selenium import webdriver
from Modal_page import *
from time import sleep


class TestModalPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'D:\Selenium-GRID\chromedriver.exe')
        self.driver.get("https://formy-project.herokuapp.com/modal")

    def test_modal_page(self):
        modal_page = ModalPage(self.driver)
        modal_page.click_modal()
        sleep(1)
        modal_page.close_modal()
        sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
