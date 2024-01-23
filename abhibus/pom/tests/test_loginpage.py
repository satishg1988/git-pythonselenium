from abhibus.pom.pages.loginpage import LoginPage


def test_verifyValidLogin(setUp, mobilenumber="9010682626", expected_otp_request_message="Enter OTP to verify your number 9010682626"):
    lp = LoginPage(setUp)
    lp.clickLoginLink()
    lp.enterMobileNumber(mobilenumber)
    lp.clickLoginOrSignupButton()
    assert lp.getOtpRequestMessageText().casefold() == expected_otp_request_message.casefold()


def test_inValidLoginWhenMobileNumberEmpty(setUp, empty_mobile_number="", expected_status=False):
    lp = LoginPage(setUp)
    lp.clickLoginLink()
    lp.enterMobileNumber(empty_mobile_number)
    assert lp.checkLoginButtonStatus() == expected_status, "Test Verification Failed When Mobile Number Empty"


def test_inValidLoginWhenMobileNumberInvalid(setUp, invalid_mobile_number="12783", expected_status=False):
    lp = LoginPage(setUp)
    lp.clickLoginLink()
    lp.enterMobileNumber(invalid_mobile_number)
    assert lp.checkLoginButtonStatus() == expected_status, "Test Verification Failed When InValid Mobile"


def test_verifyFirstRideFreeCheckBox(setUp, checkbox_default_status):
    lp = LoginPage(setUp)
    lp.clickLoginLink()
    assert lp.getDefaultStatusOfFirstRideFreeCheckbox() == checkbox_default_status


def test_verifyClickLoginWithGoogleLink(setUp, expected_result=True):
    lp = LoginPage(setUp)
    lp.clickLoginLink()
    assert lp.clickLoginWithGoogleButton() == expected_result


def test_verifyLoginButtonStatus(setUp, expected_status=False):
    lp = LoginPage(setUp)
    lp.clickLoginLink()
    assert lp.checkLoginButtonStatus() == expected_status
