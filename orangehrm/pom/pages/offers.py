import logging
from orangehrm.pom.utilities.events import Events
from orangehrm.pom.locators.allpagelocators import AllLocators as AL


class Offers(Events):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.offers_header_option = AL.offers_header_option
        self.bus_bookings_offer_heading = AL.bus_bookings_offer_heading

    def clickOffersHeaderOption(self, locator_type="xpath"):
        self.clickelement(self.offers_header_option, locator_type)

    def getTextOfBusBookingsOfferHeading(self, expected_heading_text, locator_type="xpath"):
        actual_heading_text = self.getElementText(self.bus_bookings_offer_heading, locator_type)
        print(actual_heading_text)
        assert actual_heading_text == expected_heading_text
