ALERT_CLASS_NAME = 'alert'


class ConfirmationPage():

    def __init__(self, driver):
        self.driver = driver

    def wait_for_alert(self, WebDriverWait, EC, By):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'alert')))

    def get_alert_text(self):
        alert = self.driver.find_element_by_class_name(ALERT_CLASS_NAME)
        return alert.text
