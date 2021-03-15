DATE_FIELD_ID = 'datepicker'


class DatePickerPage():

    def __init__(self, driver, keys):
        self.driver = driver
        self.keys = keys

    def pick_date(self):
        date_field = self.driver.find_element_by_id(DATE_FIELD_ID)
        date_field.send_keys('03/15/2021')
        date_field.send_keys(self.keys.RETURN)

