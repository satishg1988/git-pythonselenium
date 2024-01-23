from abhibus.pom.pages.loginpage import LoginPage


# class Test_Login:

def test_verifyValidLogin(setUp, mobilenumber="90334703", expected_loginbutton_status=False):
    # self.driver = setUp
    lp = LoginPage(setUp)
    lp.clickLoginLink()
    lp.enterMobileNumber(mobilenumber)
    assert lp.checkLoginButtonStatus() == expected_loginbutton_status, "Actual login button status not expected status"
    # lp.clickLoginOrSignupButton()
    # assert lp.getOtpRequestMessageText().casefold() == expected_otp_request_message.casefold()


def test_verifyLoginButtonStatus(setUp, expected_loginbutton_status=False):
    # driver = self.driver
    lp = LoginPage(setUp)
    lp.clickLoginLink()
    assert lp.checkLoginButtonStatus() == expected_loginbutton_status

    # def test_inValidLoginWhenMobileNumberEmpty(self, expected_status=False, empty_mobile_number=""):
    #     driver = self.driver
    #     lp = LoginPage(driver)
    #
    #     lp.clickLoginLink()
    #     lp.enterMobileNumber(empty_mobile_number)
    #     assert lp.checkLoginButtonStatus() == expected_status, "Test Verification Failed When Mobile Number Empty"
    #
    # def inValidLoginWhenMobileNumberInvalid(self, invalid_mobile_number, expected_status):
    #     driver = self.driver
    #     lp = LoginPage(driver)
    #
    #     lp.clickLoginLink()
    #     lp.enterMobileNumber(invalid_mobile_number)
    #     assert lp.checkLoginButtonStatus() == expected_status, "Test Verification Failed When InValid Mobile"
    #
    # def verifyFirstRideFreeCheckBox(self, checkbox_default_status):
    #     driver = self.driver
    #     lp = LoginPage(driver)
    #     lp.clickLoginLink()
    #     # lp.getDefaultStatusOfFirstRideFreeCheckbox(checkbox_default_status)
    #     assert lp.getDefaultStatusOfFirstRideFreeCheckbox() == checkbox_default_status
    #
    # def verifyClickLoginWithGoogleLink(self, expected_result):
    #     driver = self.driver
    #     lp = LoginPage(driver)
    #     lp.clickLoginLink()
    #     # lp.clickLoginWithGoogleButton()
    #     assert lp.clickLoginWithGoogleButton() == expected_result
