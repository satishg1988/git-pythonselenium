import logging
import time

from selenium.webdriver import ActionChains

from abhibus.pom.utilities.events import Events
from abhibus.pom.locators.allpagelocators import AllLocators as AL


class Offers(Events):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.events = Events(self.driver)
        self.offers_header_option = AL.offers_header_option
        self.bus_bookings_offer_heading = AL.bus_bookings_offer_heading
        self.offercards_title = AL.offercards_title
        self.offercards_viewdetails_btn_one = AL.offercards_viewdetails_btn_one
        self.offercards_viewdetails_btn_two = AL.offercards_viewdetails_btn_two
        self.copy_code_btn = AL.copy_code_btn
        self.code_copied_msg = AL.code_copied_msg

    def clickOffersHeaderOption(self):
        self.events.waitElementToBeClickable(10, self.offers_header_option, "xpath")
        self.events.clickElement(self.offers_header_option, locator_type="xpath")

    def getTextOfBusBookingsOfferHeading(self, locator_type="xpath"):
        return self.getElementText(self.bus_bookings_offer_heading, locator_type)

    def getOfferCards(self, req_title):
        global title
        offer_cards_locator = self.offercards_viewdetails_btn_one + req_title + self.offercards_viewdetails_btn_two
        print("Offer Cards - View Details: ", offer_cards_locator)
        offer_card_titles = self.events.getElements(self.offercards_title, "xpath")
        for title in offer_card_titles:
            print("Offer Card Titles: " + title.text)
            if title.text.casefold() == req_title.casefold():
                self.events.clickElement(offer_cards_locator, "xpath")
                time.sleep(2)
                break
        return title

    def clickCopyCodeBtn(self):
        try:
            copy_code_btn = self.events.getelement(self.copy_code_btn, "xpath")
            print("Copy Code Btn: ", copy_code_btn)
            if self.events.isElementDisplayed(self.copy_code_btn, "xpath"):
                action = ActionChains(self.driver)
                action.move_to_element(copy_code_btn).click().perform()
                # self.events.clickElement(self.copy_code_btn, "xpath")
        except:
            print("No Such Element Found")

    def getTextOfCopiedCode(self):
        return self.events.getElementText(self.code_copied_msg, "xpath")

