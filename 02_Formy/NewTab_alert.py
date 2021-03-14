ALERT_BUTTON_ID = "alert-button"

class NewTabAlert():

    def __init__(self, driver):
        self.driver = driver

    def click_alert(self):
        alert_button = self.driver.find_element_by_id(ALERT_BUTTON_ID)
        alert_button.click()

    def close_alert(self):
        alert = self.driver.switch_to_alert()
        alert.accept()
        