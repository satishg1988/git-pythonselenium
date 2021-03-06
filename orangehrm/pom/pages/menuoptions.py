import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from orangehrm.pom.locators.allpagelocators import AllLocators
from orangehrm.pom.utilities.events import Events


class MenuOptions(Events):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # calling all the locators from allpageLocators>>AllLocators
        self.header_menu_options = AllLocators.header_menu_options
        self.sub_menu_options = AllLocators.sub_menu_options

    # Get all the header menu options and click the required option
    def moveToHeaderMenuOptions(self, req_head_menu):
        # header_menu = self.driver.find_elements(By.XPATH, self.header_menu_bar)
        header_menus = self.getElements(self.header_menu_options, locator_type="xpath")
        print("Total Header Menu Options: " + str(len(header_menus)))
        for header_menu in header_menus:
            print("Menu: " + header_menu.text)
            if req_head_menu.casefold() == header_menu.text.casefold():
                # menu.click()
                action = ActionChains(self.driver)
                action.move_to_element(header_menu).perform()
                print("Moved to required header menu options: " + req_head_menu)
                break

    # Gets all the primary sub menu options and moves to the required option
    def moveToSubMenuOptions(self, req_sub_menu):
        # self.clickelement(self.header_leave_link, locator_type)
        # self.clickelement(self.leave_list_link, locator_type="xpath")
        # print("Leave header link clicked")
        sub_menus = self.getElements(self.sub_menu_options, locator_type="xpath")
        for sub_menu in sub_menus:
            if req_sub_menu.casefold() == sub_menu.text.casefold():
                action = ActionChains(self.driver)
                action.move_to_element(sub_menu).perform()
                print("Moved to required sub menu options: " + req_sub_menu)
                break

    def clickSubMenuOptions(self, req_sub_menu):
        # self.clickelement(self.header_leave_link, locator_type)
        # self.clickelement(self.leave_list_link, locator_type="xpath")
        # print("Leave header link clicked")
        sub_menus = self.getElements(self.sub_menu_options, locator_type="xpath")
        for sub_menu in sub_menus:
            if req_sub_menu.casefold() == sub_menu.text.casefold():
                sub_menu.click()
                print("Required sub menu option clicked: " + req_sub_menu)
                break
