RADIO_BUTTON_1_ID = "radio-button-1"
RADIO_BUTTON_2_CSS = "input[value='option2']"
RADIO_BUTTON_3_XPATH = '/html/body/div/div[3]/input'

class RadioPage():

    def __init__(self, driver):
        self.driver = driver

    def select_button_1(self):
        radio_button_1 = self.driver.find_element_by_id(RADIO_BUTTON_1_ID)
        radio_button_1.click()

    def select_button_2(self):
        radio_button_2 = self.driver.find_element_by_css_selector(RADIO_BUTTON_2_CSS)
        radio_button_2.click()

    def select_button_3(self):
        radio_button_3 = self.driver.find_element_by_xpath(RADIO_BUTTON_3_XPATH)
        radio_button_3.click()
