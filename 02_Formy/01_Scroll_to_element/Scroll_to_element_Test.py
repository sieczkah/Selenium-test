import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Scroll_to_element import *

fullname = "Kubi Bubi"
date = "10/27/2020"


class TestScrollToElement(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'D:\Selenium-GRID\chromedriver.exe')
        self.driver.get("https://formy-project.herokuapp.com/scroll")
        self.action = ActionChains(self.driver)

    def test_Scroll_to_Element(self):
        scroll_to_element_page = ScrollToElement(self.driver, self.action)
        scroll_to_element_page.enter_fullname(fullname)
        scroll_to_element_page.enter_date(date)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
