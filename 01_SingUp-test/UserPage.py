SUCCESS_BANNER = "flash_success"


class UserPage:

    def __init__(self, driver):
        self.driver = driver

    def get_banner_text(self):
        banner = self.driver.find_element_by_id(SUCCESS_BANNER)
        return banner.text
