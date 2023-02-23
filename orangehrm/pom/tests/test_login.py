import unittest
from orangehrm.pom.pages.loginpage import LoginPage


class LoginTest:
    
    def __init__(self, driver):
        self.driver = driver

    def validLogin(self, mobilenumber, otp_sent_message):
        driver = self.driver
        lp = LoginPage(driver)
        lp.clickLoginLink()
        lp.enterMobileNumber(mobilenumber)
        lp.clickLoginOrSignupButton()
        # lp.getOtpRequestMessageText(otp_request_message)
        lp.getOtpSentMessageText(otp_sent_message)

    def inValidLoginWhenMobileNumberEmpty(self, expected_error_message, empty_mobile_number=""):
        driver = self.driver
        lp = LoginPage(driver)

        lp.clickLoginLink()
        lp.enterMobileNumber(empty_mobile_number)
        lp.clickLoginOrSignupButton()
        lp.getErrorMessageWhenMobileIsEmpty(expected_error_message)

    def inValidLoginWhenMobileNumberInvalid(self, invalid_mobile_number, expected_error_message):
        driver = self.driver
        lp = LoginPage(driver)

        lp.clickLoginLink()
        lp.enterMobileNumber(invalid_mobile_number)
        lp.clickLoginOrSignupButton()
        lp.getErrorMessageWhenMobileIsInvalid(expected_error_message)

    def verifyFirstRideFreeCheckBox(self, checkbox_default_status):
        driver = self.driver
        lp = LoginPage(driver)
        lp.clickLoginLink()
        lp.getDefaultStatusOfFirstRideFreeCheckbox(checkbox_default_status)

    def verifyClickLoginWithGoogleLink(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.clickLoginLink()
        lp.clickLoginWithGoogleButton()
