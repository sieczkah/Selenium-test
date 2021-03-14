NAME_FIELD = 'name'
BUTTON_ID = 'button'


class KeyboardAndMouseInput:

    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, full_name):
        name_field = self.driver.find_element_by_id(NAME_FIELD)
        name_field.click()
        name_field.send_keys(full_name)

    def submit_button(self):
        button = self.driver.find_element_by_id(BUTTON_ID)
        button.click()
        self.driver.quit()
