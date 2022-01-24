from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from orangehrm.pom.locators import allpagelocators
from orangehrm.pom.utilities.events import Events


class HomePage(Events):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # calling all the locators from allpageLocators>>AllLocators
        self.welcome_user_link = allpagelocators.AllLocators.welcome_user_link
        self.header_leave_link = allpagelocators.AllLocators.header_leave_link
        self.logout_link = allpagelocators.AllLocators.logout_link
        self.header_menu_bar = allpagelocators.AllLocators.header_menu_bar

    # click the welcome username link on home page
    def click_welcome_admin_link(self, locator_type="xpath"):
        self.clickelement(self.welcome_user_link, locator_type)
        print("Welcome Successful")

    # Get all the header menu options and click the required option
    def click_header_menu_options(self, req_menu):
        header_menu = self.driver.find_elements(By.XPATH, self.header_menu_bar)
        print("Total Header Menu Options: " + str(len(header_menu)))
        for menu in header_menu:
            print("Menu: " + menu.text)
            if req_menu.casefold() == menu.text.casefold():
                action = ActionChains(self.driver)
                action.move_to_element(menu).click(menu).perform()
                print(req_menu + " - header menu option clicked")
                break

    def click_header_leave_link(self, locator_type="xpath"):
        self.clickelement(self.header_leave_link, locator_type)
        print("Leave header link clicked")

    def click_logout_link(self, locator_type="xpath"):
        self.clickelement(self.welcome_user_link, locator_type)
        self.clickelement(self.logout_link, locator_type)
        print("Logout Successful")
