from abhibus.pom.utilities.events import Events
from abhibus.pom.locators.allpagelocators import AllLocators as AL


class GetFreeRides(Events):
    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver
        self.get_free_rides_header_option = AL.get_free_rides_header_option

    def clickGetFreeRidesHeaderOption(self, locator_type="xpath"):
        self.clickelement(self.get_free_rides_header_option, locator_type)
