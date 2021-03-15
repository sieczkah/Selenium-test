MODAL_BUTTON_ID = "modal-button"
CLOSE_BUTTON_ID = "close-button"


class ModalPage():

    def __init__(self, driver):
        self.driver = driver

    def click_modal(self):
        modal_button = self.driver.find_element_by_id(MODAL_BUTTON_ID)
        modal_button.click()

    def close_modal(self):
        close_button = self.driver.find_element_by_id(CLOSE_BUTTON_ID)
        self.driver.execute_script("arguments[0].click()", close_button)
