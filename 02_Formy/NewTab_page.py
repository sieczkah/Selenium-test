from time import sleep
OPENTAB_BUTTON_ID = 'new-tab-button'

class NewTabPage:

    def __init__(self, driver):
        self.driver = driver

    def click_newtab(self):
        newtab_button = self.driver.find_element_by_id(OPENTAB_BUTTON_ID)
        newtab_button.click()

    def switch_tab(self):
        for tab in self.driver.window_handles:
            sleep(1)
            self.driver.switch_to_window(tab)
            sleep(1)
