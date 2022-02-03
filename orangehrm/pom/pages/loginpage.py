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
        self.username_textbox_empty = allpagelocators.AllLocators.username_textbox_empty

    def enterUsername(self, username, locator_type="xpath"):
        self.sendkeyselement(username, self.username_textbox, locator_type)

    def enterPassword(self, password, locator_type="xpath"):
        self.sendkeyselement(password, self.password_textbox, locator_type)

    def clickLogin(self):
        self.clickelement(self.login_button, locator_type="id")

    def validLogin(self, uname="", pwd=""):
        driver = self.driver
        lp = LoginPage(driver)

        lp.enterUsername(uname)
        lp.enterPassword(pwd)
        lp.clickLogin()

    def inValidLogin(self, uname="", pwd=""):
        driver = self.driver
        lp = LoginPage(driver)

        lp.enterUsername(uname)
        lp.enterPassword(pwd)
        lp.clickLogin()

    def verifyLoginSuccess(self, expected_title):
        actual_title = self.getElementText(self.title, locator_type="xpath")
        assert actual_title.casefold() == expected_title.casefold()

    def verifyLoginFailure(self, expected_error_message):
        actual_error_message = self.getElementText(self.username_textbox_empty, locator_type="xpath")
        assert actual_error_message == expected_error_message


    # def verifyLoginTitle(self):
    #  test for testing purpose
    #     actual_title = self.getTitle()
    #     return self.verifyTextContains(actual_title, expected_text="test")
        # if "OrangeHRM" in self.getTitle():
        #     print("Login Successful")
        #     return True
        # else:
        #     return False
