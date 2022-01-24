from orangehrm.pom.locators import allpagelocators
from orangehrm.pom.utilities.data import Data
from orangehrm.pom.utilities.events import Events


class LoginPage(Events):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_textbox = allpagelocators.AllLocators.username_textbox
        self.password_textbox = allpagelocators.AllLocators.password_textbox
        self.login_button = allpagelocators.AllLocators.login_button
        self.title = allpagelocators.AllLocators.title

    def enter_username(self, username, locator_type="xpath"):
        self.sendkeyselement(username, self.username_textbox, locator_type)

    def enter_password(self, password, locator_type="xpath"):
        self.sendkeyselement(password, self.password_textbox, locator_type)

    def click_login(self):
        self.clickelement(self.login_button, locator_type="id")

    def validLogin(self, uname="", pwd=""):
        driver = self.driver
        lp = LoginPage(driver)

        lp.enter_username(uname)
        lp.enter_password(pwd)
        lp.click_login()

    def verifyLoginSuccess(self):
        assert self.getElementText(self.title, locator_type="xpath").is_displayed(), "---Login Failed---"

    # def verifyLoginTitle(self):
    #  test for testing purpose
    #     actual_title = self.getTitle()
    #     return self.verifyTextContains(actual_title, expected_text="test")
        # if "OrangeHRM" in self.getTitle():
        #     print("Login Successful")
        #     return True
        # else:
        #     return False
