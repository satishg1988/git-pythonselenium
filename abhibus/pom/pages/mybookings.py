from abhibus.pom.locators.allpagelocators import AllLocators as AL
from abhibus.pom.utilities.events import Events


class MyBookings(Events):

    def __init__(self, driver):
        super().__init__(driver)
        self.my_bookings_header_option = AL.my_bookings_header_option
        self.print_booking_header_option = AL.print_booking_header_option
        self.cancel_booking_header_option = AL.cancel_booking_header_option

    def clickPrintBookingsHeaderOption(self, locator_type="xpath"):
        self.clickelement(self.my_bookings_header_option, locator_type)
        self.clickelement(self.print_booking_header_option, locator_type)

    def clickCancelBookingHeaderOption(self, locator_type="xpath"):
        self.clickelement(self.my_bookings_header_option, locator_type)
        self.clickelement(self.cancel_booking_header_option, locator_type)
