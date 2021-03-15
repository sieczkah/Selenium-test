IMAGE_ID = "image"
BOX_ID = "box"


class DragDropPage():

    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

    def drag_drop_image(self):
        image_element = self.driver.find_element_by_id(IMAGE_ID)
        box_element = self.driver.find_element_by_id(BOX_ID)
        self.action.drag_and_drop(image_element, box_element).perform()

