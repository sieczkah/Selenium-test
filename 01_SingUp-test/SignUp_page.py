# SELECTORS
USERNAME_FIELD = "user_username"
EMAIL_FIELD = "user_email"
PASSWORD_FIELD = "user_password"
SUBMIT_BUTTON = "submit"


class SignupPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        username_field = self.driver.find_element_by_id(USERNAME_FIELD)
        username_field.send_keys(username)

    def enter_email(self, email):
        email_field = self.driver.find_element_by_id(EMAIL_FIELD)
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element_by_id(PASSWORD_FIELD)
        password_field.send_keys(password)

    def submit_form(self):
        sign_up_button = self.driver.find_element_by_id(SUBMIT_BUTTON)
        sign_up_button.click()
