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
        # self.wait = WebDriverWait(self.driver, 10)

        # calling all the locators from allpageLocators>>AllLocators
        self.left_panel = AllLocators.left_panel
        self.rightpanel_all_header_options = AllLocators.rightpanel_all_header_options

    # Get all the left panel options and click the required option
    def clickLeftPaneOptions(self, req_leftpanel_option):
        # header_menu = self.driver.find_elements(By.XPATH, self.header_menu_bar)
        leftpanel_options = self.getElements(self.left_panel, locator_type="xpath")
        print("Total left Panel Options: " + str(len(leftpanel_options)))
        for leftpanel_option in leftpanel_options:
            print("Left Panel Option: " + leftpanel_option.text)
            if req_leftpanel_option.casefold() == leftpanel_option.text.casefold():
                # menu.click()
                action = ActionChains(self.driver)
                action.move_to_element(leftpanel_option).click().perform()
                print("Moved and Clicked the required left panel option: " + req_leftpanel_option)
                break

    # Gets all the primary sub menu options and moves to the required option
    def clickRightPanelMenuOptions(self, req_rightpanel_menu):
        # self.clickelement(self.header_leave_link, locator_type)
        # self.clickelement(self.leave_list_link, locator_type="xpath")
        # print("Leave header link clicked")
        rightpanel_menus = self.getElements(self.rightpanel_all_header_options, locator_type="xpath")
        print("Total Right Panel Options: " + str(len(rightpanel_menus)))
        for rightpanel_menu in rightpanel_menus:
            print("Right Panel Option: " + rightpanel_menu.text)
            if req_rightpanel_menu.casefold() == rightpanel_menu.text.casefold():
                action = ActionChains(self.driver)
                action.move_to_element(rightpanel_menu).click().perform()
                print("Moved to required menu options in right panel and clicked: " + req_rightpanel_menu)
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
