import time

from orangehrm.pom.locators.allpagelocators import AllLocators as AL
from orangehrm.pom.utilities.events import Events
import unittest
import logging


class LoginPage(Events):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.log = logging.getLogger()
        self.login_or_register_link = AL.login_or_register_link
        self.mobile_num_textbox = AL.mobile_num_textbox
        self.close_icon = AL.close_icon
        self.login_signup_otp_button = AL.login_signup_otp_button
        self.login_with_google_button = AL.login_with_google_button
        self.otp_request_message = AL.otp_request_message
        self.otp_sent_success_message = AL.otp_sent_success_message
        self.my_bookings_header_option = AL.my_bookings_header_option
        self.print_booking_header_option = AL.print_booking_header_option
        self.cancel_booking_header_option = AL.cancel_booking_header_option
        self.get_free_rides_header_option = AL.get_free_rides_header_option
        self.error_msg_mobile_empty = AL.error_msg_mobile_empty
        self.error_msg_mobile_invalid = AL.error_msg_mobile_invalid
        self.get_first_ride_free_checkbox = AL.get_first_ride_free_checkbox

    def clickLoginLink(self, locator_type="xpath"):
        self.clickelement(self.login_or_register_link, locator_type)

    def enterMobileNumber(self, mobilenumber, locator_type="xpath"):
        self.waitForPresenceOfElement(3, self.mobile_num_textbox, locator_type)
        self.sendkeyselement(mobilenumber, self.mobile_num_textbox, locator_type)
        time.sleep(3)

    def clickLoginOrSignupButton(self, locator_type="xpath"):
        # self.waitElementToBeClickable(10, self.login_signup_otp_button, locator_type)
        self.waitForPresenceOfElement(10, self.login_signup_otp_button, locator_type)
        self.clickelement(self.login_signup_otp_button, locator_type)
        time.sleep(5)

    def clickLoginWithGoogleButton(self, locator_type="xpath"):
        self.waitElementToBeClickable(5, self.login_with_google_button, locator_type)
        self.clickelement(self.login_with_google_button, locator_type)
        time.sleep(5)

    def getOtpRequestMessageText(self, otp_request_message, locator_type="xpath"):
        actual_text = self.getElementText(self.otp_request_message, locator_type)
        assert actual_text.casefold == otp_request_message.casefold, "FAIL: Actual Text not matched the Expected Text"

    def getOtpSentMessageText(self, otp_sent_message, locator_type="xpath"):
        actual_text = self.getElementText(self.otp_sent_success_message, locator_type)
        assert actual_text.casefold == otp_sent_message.casefold, "FAIL: Actual Text not matched the Expected Text"

    def getErrorMessageWhenMobileIsEmpty(self, expected_error_message, locator_type="xpath"):
        actual_error_message = self.getElementText(self.error_msg_mobile_empty, locator_type)
        assert actual_error_message == expected_error_message

    def getErrorMessageWhenMobileIsInvalid(self, expected_error_message, locator_type="xpath"):
        actual_error_message = self.getElementText(self.error_msg_mobile_invalid, locator_type)
        assert actual_error_message.casefold() == expected_error_message.casefold()

    def getDefaultStatusOfFirstRideFreeCheckbox(self, checkbox_default_status, locator_type="xpath"):
        self.waitForPresenceOfElement(5, self.get_first_ride_free_checkbox, locator_type)
        checkbox_actual_status = self.isElementSelected(self.get_first_ride_free_checkbox, locator_type)
        print(checkbox_actual_status)
        assert checkbox_actual_status == checkbox_default_status
