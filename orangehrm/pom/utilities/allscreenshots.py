import os
import time
from traceback import print_stack


class ScreenShots:
    def captureScreenShots(self):
        filename_screenshot = str(round(time.time() * 1000)) + "--testscreenshot.png"
        directory_screenshot = "E:/PycharmProjects/git-pythonselenium/orangehrm/screenshots"
        destinationfile_screenshot = directory_screenshot + filename_screenshot
        # self.driver.save_screenshot(destinationfile_screenshot)
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, destinationfile_screenshot)
        destination_directory = os.path.join(current_directory, directory_screenshot)
        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destinationfile_screenshot)
            print("Screenshot saved successfully in:" + destination_file)
            # print("Screenshot saved successfully in:" + str(destinationfile_screenshot))
        except:
            print_stack()
