import unittest
from orangehrm.pom.pages.loginpage import LoginPage


class LoginTest:

    def __init__(self, driver):
        self.driver = driver

    def verifyValidLogin(self, mobilenumber, expected_otp_request_message):
        driver = self.driver
        lp = LoginPage(driver)
        lp.clickLoginLink()
        lp.enterMobileNumber(mobilenumber)
        lp.clickLoginOrSignupButton()
        assert lp.getOtpRequestMessageText().casefold() == expected_otp_request_message.casefold()
        # lp.getOtpSentMessageText(otp_sent_message)

    def inValidLoginWhenMobileNumberEmpty(self, expected_error_message, empty_mobile_number=""):
        driver = self.driver
        lp = LoginPage(driver)

        lp.clickLoginLink()
        lp.enterMobileNumber(empty_mobile_number)
        lp.clickLoginOrSignupButton()
        # lp.getErrorMessageWhenMobileIsEmpty(expected_error_message)
        assert lp.getErrorMessageWhenMobileIsEmpty().casefold() == expected_error_message.casefold()

    def inValidLoginWhenMobileNumberInvalid(self, invalid_mobile_number, expected_error_message):
        driver = self.driver
        lp = LoginPage(driver)

        lp.clickLoginLink()
        lp.enterMobileNumber(invalid_mobile_number)
        lp.clickLoginOrSignupButton()
        # lp.getErrorMessageWhenMobileIsInvalid(expected_error_message)
        assert lp.getErrorMessageWhenMobileIsInvalid().casefold() == expected_error_message.casefold()

    def verifyFirstRideFreeCheckBox(self, checkbox_default_status):
        driver = self.driver
        lp = LoginPage(driver)
        lp.clickLoginLink()
        # lp.getDefaultStatusOfFirstRideFreeCheckbox(checkbox_default_status)
        assert lp.getDefaultStatusOfFirstRideFreeCheckbox() == checkbox_default_status

    def verifyClickLoginWithGoogleLink(self, expected_result):
        driver = self.driver
        lp = LoginPage(driver)
        lp.clickLoginLink()
        # lp.clickLoginWithGoogleButton()
        assert lp.clickLoginWithGoogleButton() == expected_result

