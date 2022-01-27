import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from orangehrm.pom.locators.allpagelocators import AllLocators
from orangehrm.pom.utilities.events import Events


class HomePage(Events):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # calling all the locators from allpageLocators>>AllLocators
        self.welcome_user_link = AllLocators.welcome_user_link
        self.header_menu_options = AllLocators.header_menu_options
        self.sub_menu_options = AllLocators.sub_menu_options
        self.header_leave_link = AllLocators.header_leave_link
        self.leave_list_link = AllLocators.leave_list_link
        self.logout_link = AllLocators.logout_link

    # click the welcome username link on home page
    def clickWelcomeUserLink(self, locator_type="xpath"):
        self.clickelement(self.welcome_user_link, locator_type)
        print("Welcome Successful")

    # Get all the header menu options and click the required option
    # def clickHeaderMenuOptions(self, req_head_menu, locator_type="xpath"):
    #     # header_menu = self.driver.find_elements(By.XPATH, self.header_menu_bar)
    #     header_menus = self.getElements(self.header_menu_options, locator_type)
    #     print("Total Header Menu Options: " + str(len(header_menus)))
    #     for menu in header_menus:
    #         print("Menu: " + menu.text)
    #         if req_head_menu.casefold() == menu.text.casefold():
    #             menu.click()
    #             # action = ActionChains(self.driver)
    #             # action.move_to_element(menu).click(menu).perform()
    #             print("Required header menu option clicked: " + req_head_menu)
    #             break
    #
    # def clickSubMenuOptions(self, req_sub_menu):
    #     # self.clickelement(self.header_leave_link, locator_type)
    #     # self.clickelement(self.leave_list_link, locator_type="xpath")
    #     # print("Leave header link clicked")
    #     sub_menus = self.getElements(self.sub_menu_options, locator_type="xpath")
    #     for sub_menu in sub_menus:
    #         if req_sub_menu.casefold() == sub_menu.text.casefold():
    #             sub_menu.click()
    #             print("Required sub menu option clicked: " + req_sub_menu)
    #             break

    def clickLogoutLink(self, locator_type="xpath"):
        self.clickelement(self.welcome_user_link, locator_type)
        self.clickelement(self.logout_link, locator_type)
        print("Logout Successful")
