import time

from selenium.webdriver import ActionChains

from abhibus.pom.locators.allpagelocators import AllLocators as AL
from abhibus.pom.utilities.events import Events
from abhibus.pom.utilities.Base import Base


class LoginPage(Base):
    def __init__(self, driver):
        self.driver = driver
        self.events = Events(self.driver)
        # self.login_button = AL.login_button
        # self.login_or_register_link = AL.login_or_register_link
        # self.close_icon = AL.close_icon
        # self.login_signup_otp_button = AL.login_signup_otp_button
        # self.login_with_google_button = AL.login_with_google_button
        # self.otp_request_message = AL.otp_request_message
        # self.otp_sent_success_message = AL.otp_sent_success_message
        # self.my_bookings_header_option = AL.my_bookings_header_option
        # self.print_booking_header_option = AL.print_booking_header_option
        # self.cancel_booking_header_option = AL.cancel_booking_header_option
        # self.get_free_rides_header_option = AL.get_free_rides_header_option
        # self.error_msg_mobile_empty = AL.error_msg_mobile_empty
        # self.error_msg_mobile_invalid = AL.error_msg_mobile_invalid
        # self.get_first_ride_free_checkbox = AL.get_first_ride_free_checkbox
        self.login_or_register_link = AL.login_or_register_link

    login_button = AL.login_button
    mobile_num_textbox = AL.mobile_num_textbox
    login_with_google_button = AL.login_with_google_button
    login_signup_otp_button = AL.login_signup_otp_button
    otp_request_message = AL.otp_request_message

    def clickLoginLink(self):
        # events = Events(self.driver)
        login_link_element = self.events.getelement(self.login_or_register_link, "xpath")
        actions = ActionChains(self.driver)
        actions.move_to_element(login_link_element).click().perform()
        # self.events.waitElementToBeClickable(10, self.login_or_register_link, "xpath")
        # self.events.clickElement(self.login_or_register_link, locator_type="xpath")
        # self.clickElement(self.login_or_register_link, locator_type="id")
        # Events(self.driver).clickElement(self.login_or_register_link, locator_type="id")

    def checkLoginButtonStatus(self):
        actual_loginbutton_status = self.events.isElementEnabled(self.login_button, locator_type="xpath")
        return actual_loginbutton_status

    def enterMobileNumber(self, mobilenumber):
        self.events.waitForPresenceOfElement(3, self.mobile_num_textbox, locator_type="xpath")
        self.events.sendkeyselement(mobilenumber, self.mobile_num_textbox, locator_type="xpath")
        # time.sleep(3)

    def clickLoginOrSignupButton(self, locator_type="xpath"):
        # self.waitElementToBeClickable(10, self.login_signup_otp_button, locator_type)
        self.events.waitForPresenceOfElement(5, self.login_signup_otp_button, locator_type)
        self.events.clickElement(self.login_signup_otp_button, locator_type)
        time.sleep(2)

    def clickLoginWithGoogleButton(self, locator_type="xpath"):
        self.events.waitElementToBeClickable(5, self.login_with_google_button, locator_type)
        self.events.clickElement(self.login_with_google_button, locator_type)
        time.sleep(2)
        return True

    def getOtpRequestMessageText(self, locator_type="xpath"):
        self.events.waitForPresenceOfElement(5, self.otp_request_message, locator_type)
        actual_text = self.events.getElementText(self.otp_request_message, locator_type)
        print("Actual OTP Request Message Is: " + actual_text)
        # assert actual_text.casefold() == otp_request_message.casefold(), "FAIL: Actual Text not matched the Expected Text"
        return actual_text

    def getOtpSentMessageText(self, locator_type="xpath"):
        actual_text = self.getElementText(self.otp_sent_success_message, locator_type)
        # assert actual_text.casefold == otp_sent_message.casefold, "FAIL: Actual Text not matched the Expected Text"
        return actual_text

    def getErrorMessageWhenMobileIsEmpty(self, locator_type="xpath"):
        actual_error_message = self.getElementText(self.error_msg_mobile_empty, locator_type)
        print("Actual Error Message - Empty: " + actual_error_message)
        # assert actual_error_message.casefold() == expected_error_message.casefold()
        return actual_error_message

    def getErrorMessageWhenMobileIsInvalid(self, locator_type="xpath"):
        actual_error_message = self.getElementText(self.error_msg_mobile_invalid, locator_type)
        print("Actual Error Message - Invalid: " + actual_error_message)
        # assert actual_error_message.casefold() == expected_error_message.casefold()
        return actual_error_message

    def getDefaultStatusOfFirstRideFreeCheckbox(self, locator_type="xpath"):
        self.waitForPresenceOfElement(5, self.get_first_ride_free_checkbox, locator_type)
        checkbox_actual_status = self.isElementSelected(self.get_first_ride_free_checkbox, locator_type)
        print("The Actual Status is:" + str(checkbox_actual_status))
        # assert checkbox_actual_status == checkbox_default_status
        return checkbox_actual_status
