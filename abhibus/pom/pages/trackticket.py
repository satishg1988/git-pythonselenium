from abhibus.pom.locators.allpagelocators import AllLocators as AL
from abhibus.pom.utilities.events import Events


class TrackTicket():
    def __init__(self, driver):
        self.driver = driver
        self.events = Events(driver)
        self.track_ticket_option = AL.track_ticket_option
        self.track_ticket_heading = AL.track_ticket_heading
        self.ticket_details_button = AL.ticket_details_button
        self.errormessage_bookingid_empty = AL.errormsg_bookingid_empty
        self.errormsg_mobilenumber_empty = AL.errormsg_mobilenumber_empty
    def clickTrackTicketOption(self):
        self.events.waitElementToBeClickable(10, self.track_ticket_option, "xpath")
        Events(driver=self.driver).clickElement(self.track_ticket_option, "xpath")

    def getTextOfTrackTicketHeading(self):
        return self.events.getElementText(self.track_ticket_heading, "xpath")

    def clickTicketDetailsButton(self):
        self.events.clickElement(self.ticket_details_button, "xpath")

    def getErrorMsgBookingIdEmpty(self):
        return self.events.getElementText(self.errormessage_bookingid_empty, "xpath")

    def getErrorMsgMobileEmpty(self):
        return self.events.getElementText(self.errormsg_mobilenumber_empty, "xpath")
