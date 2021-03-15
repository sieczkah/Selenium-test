DROPDOWN_BUT_ID = 'dropdownMenuButton'
AUTOCOMPLETE_FIELD = 'autocomplete'

class DropdownPage():

    def __init__(self, driver):
        self.driver = driver

    def dropdown_select(self):
        dropdown_button = self.driver.find_element_by_id(DROPDOWN_BUT_ID)
        dropdown_button.click()
        autocomplete_field = self.driver.find_element_by_id(AUTOCOMPLETE_FIELD)
        autocomplete_field.click()

