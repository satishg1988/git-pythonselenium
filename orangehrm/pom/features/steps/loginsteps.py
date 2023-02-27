from behave import *
from orangehrm.pom.browsersetup.browseractions import Browser
from orangehrm.pom.utilities.data import Data
from orangehrm.pom.pages.loginpage import LoginPage


@given('Launch the browser')
def launchBrowser(context):
    b = Browser
    b.browserSetUp(context, "chrome")


@when('Open the URL https://www.abhibus.com/ website')
def openUrl(context):
    b = Browser
    b.launchUrl(context, Data.url)


@then('Click on the Login link')
def clickLogin(context):
    driver = context.driver
    lp = LoginPage(driver)
    lp.clickLoginLink()


@then('Enter a valid Mobile number')
def enterMobile(context):
    driver = context.driver
    lp = LoginPage(driver)
    lp.enterMobileNumber(Data.mobilenumber)


@then('Enter Mobile number is empty')
def enterEmptyMobileNumber(context):
    driver = context.driver
    lp = LoginPage(driver)
    # lp.clickLoginLink()
    lp.enterMobileNumber(mobilenumber="")
    # lp.getErrorMessageWhenMobileIsEmpty("Please enter valid mobile number")


@then('OTP request message to be displayed')
def otpRequestMessage(context):
    driver = context.driver
    lp = LoginPage(driver)
    lp.getOtpRequestMessageText("Your OTP request will be proccessed.")


@then('Error message is displayed when mobile number is empty')
def errorMessageWhenEmptyMobileNumber(context):
    driver = context.driver
    lp = LoginPage(driver)
    # lp.enterMobileNumber("9010")
    lp.getErrorMessageWhenMobileIsEmpty("Please enter valid mobile number")


@then('Enter an invalid mobile number "{mobilenumber}"')
def enterInvalidMobileNumber(context, mobilenumber):
    driver = context.driver
    lp = LoginPage(driver)
    lp.enterMobileNumber(mobilenumber)
    # lp.getErrorMessageWhenMobileIsInvalid("Please enter valid mobile number")


@then('Error message is displayed when mobile number is invalid')
def errorMessageWhenInvalidMobileNumber(context):
    driver = context.driver
    lp = LoginPage(driver)
    # lp.enterMobileNumber("9010")
    lp.getErrorMessageWhenMobileIsInvalid("Please enter valid mobile number")


@then('Click the Login or Signup button')
def clickLoginButton(context):
    driver = context.driver
    lp = LoginPage(driver)
    lp.clickLoginOrSignupButton()


@then('Close the browser')
def closeBrowser(context):
    driver = context.driver
    driver.close()
    driver.quit()
