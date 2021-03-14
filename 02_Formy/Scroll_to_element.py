FULLNAME_FIELD_ID = 'name'
DATE_FIELD_ID = 'date'

class ScrollToElement:

    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

    def enter_fullname(self, full_name):
        name_field = self.driver.find_element_by_id(FULLNAME_FIELD_ID)
        self.move_to_element(name_field)
        name_field.send_keys(full_name)

    def enter_date(self, date):
        date_field = self.driver.find_element_by_id(DATE_FIELD_ID)
        self.move_to_element(date_field)
        date_field.send_keys(date)

    def move_to_element(self, element):
        self.action.move_to_element(element)
        self.action.perform()


