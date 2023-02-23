from orangehrm.pom.pages.offers import Offers


class OffersTest:
    def __init__(self, driver):
        self.driver = driver

    def verifyTextOfBusBookingsOfferHeading(self, expected_heading_text):
        driver = self.driver
        of = Offers(driver)
        of.clickOffersHeaderOption()
        of.getTextOfBusBookingsOfferHeading(expected_heading_text)
