import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from DragDrop_page import *
from time import sleep


class TestDragDropPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'D:\Selenium-GRID\chromedriver.exe')
        self.driver.get("https://formy-project.herokuapp.com/dragdrop")
        self.action = ActionChains(self.driver)

    def test_drag_drop_image(self):
        drag_page = DragDropPage(self.driver, self.action)
        sleep(1)
        drag_page.drag_drop_image()
        sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
