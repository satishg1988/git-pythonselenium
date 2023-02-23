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


@then('Enter Mobile number "9010682626"')
def enterMobile(context):
    driver = context.driver
    lp = LoginPage(driver)
    lp.enterMobileNumber(Data.mobilenumber)


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