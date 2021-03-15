FIRSTNAME_FIELD_ID = 'first-name'
LASTNAME_FIELD_ID = 'last-name'
JOBTITLE_FIELD_ID = 'job-title'
RADIO_BUTTON_ID = 'radio-button-2'
CHECKBOX_ID = 'checkbox-1'
YEARS_EXP_CSS = '#select-menu option[value="2"]'
DATEPICK_ID = 'datepicker'
SUBMIT_BUTTON_CSS = "a[role='button']"

class WebFormPage():

    def __init__(self, driver, keys):
        self.driver = driver
        self.keys = keys

    def submit_form(self, firstname, lastname, jobtitle, date):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_jobtitle(jobtitle)
        self.select_radiobutton()
        self.select_checkbox()
        self.entry_years_exp()
        self.entry_date(date)
        self.submit()

    def enter_firstname(self, fistname):
        fistname_field = self.driver.find_element_by_id(FIRSTNAME_FIELD_ID)
        fistname_field.send_keys(fistname)

    def enter_lastname(self, lastname):
        lastname_field = self.driver.find_element_by_id(LASTNAME_FIELD_ID)
        lastname_field.send_keys(lastname)

    def enter_jobtitle(self, jobtitle):
        jobtitle_field = self.driver.find_element_by_id(JOBTITLE_FIELD_ID)
        jobtitle_field.send_keys(jobtitle)

    def select_radiobutton(self):
        radio_button = self.driver.find_element_by_id(RADIO_BUTTON_ID)
        radio_button.click()

    def select_checkbox(self):
        checkbox = self.driver.find_element_by_id(CHECKBOX_ID)
        checkbox.click()

    def entry_years_exp(self):
        years_exp_fiel = self.driver.find_element_by_css_selector(YEARS_EXP_CSS).click()

    def entry_date(self, date):
        date_field = self.driver.find_element_by_id(DATEPICK_ID)
        date_field.send_keys(date)
        date_field.send_keys(self.keys.RETURN)

    def submit(self):
        submit_button = self.driver.find_element_by_css_selector(SUBMIT_BUTTON_CSS)
        submit_button.click()