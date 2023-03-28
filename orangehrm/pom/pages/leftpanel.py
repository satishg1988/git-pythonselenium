import time

from selenium.webdriver import ActionChains

from orangehrm.pom.utilities.events import Events
from orangehrm.pom.locators.allpagelocators import AllLocators as AL


class LeftPanel(Events):
    def __init__(self, driver):
        super().__init__(driver)
        self.price_drop_checkbox = AL.price_drop_checkbox
        self.bus_type_filters = AL.bus_type_filters
        self.clearall_bustype = AL.clearall_bustype
        self.expand_collapse_bus_partner = AL.expand_collapse_bus_partner
        self.bus_partner_searchbox = AL.bus_partner_searchbox
        self.bus_partners_list = AL.bus_partners_list
        self.boarding_point_expand_collapse = AL.boarding_point_expand_collapse
        self.boarding_point_searchbox = AL.boarding_point_searchbox
        self.boarding_points_list = AL.boarding_points_list
        self.dropping_point_expand_collapse = AL.dropping_point_expand_collapse
        self.dropping_point_searchbox = AL.dropping_point_searchbox
        self.dropping_points_list = AL.dropping_points_list
        self.depature_time_filters = AL.depature_time_filters

        self.action = ActionChains(driver)

    def selectPriceDropCheckbox(self, locator_type="xpath"):
        self.waitForPresenceOfElement(5, self.price_drop_checkbox, locator_type)
        pricedrop_checkbox_status = self.isElementSelected(self.price_drop_checkbox, locator_type)
        print("price drop checkbox is: " + str(pricedrop_checkbox_status))
        if not pricedrop_checkbox_status:
            self.clickelement(self.price_drop_checkbox, locator_type)
            # time.sleep(5)

    def selectBusTypeFilter(self, req_bustype_list, locator_type="xpath"):
        for bus_type in self.getElements(self.bus_type_filters, locator_type):
            print("Bus Types: " + bus_type.text)
            # bustype_list = ["AC", "SEATER", "SLEEPER"]
            for req_bustype in req_bustype_list:
                print("Bus Types List: " + req_bustype)
                if bus_type.text.casefold() == req_bustype.casefold():
                    self.waitElementToBeClickable(5, self.bus_type_filters, locator_type)
                    bus_type.click()
                    break

    def getClearAllText(self, locator_type="xpath"):
        self.getElementText(self.clearall_bustype, locator_type)

    def expandOrCollapseBusPartner(self, locator_type="xpath"):
        self.waitElementToBeClickable(5, self.expand_collapse_bus_partner, locator_type)
        self.clickelement(self.expand_collapse_bus_partner, locator_type)

    def enterBusPartnerName(self, req_buspartner_name, locator_type="xpath"):
        self.sendkeyselement(req_buspartner_name, self.bus_partner_searchbox, locator_type)
        # time.sleep(5)

    def getBusPartnersList(self, req_buspartner_list, locator_type="xpath"):
        for bus_partner in self.getElements(self.bus_partners_list, locator_type):
            print("Bus Partner is: " + bus_partner.text)
            # req_buspartner_list = ["Orange Tours and Travels", "APSRTC", "Ajay Bus"]
            for req_buspartner in req_buspartner_list:
                if bus_partner.text.casefold() == req_buspartner.casefold():
                    self.waitElementToBeClickable(5, self.bus_partners_list, locator_type)
                    bus_partner.click()
                    # time.sleep(2)
                    break

    def expandOrCollapseBoardingPoint(self, locator_type="xpath"):
        self.waitElementToBeClickable(5, self.boarding_point_expand_collapse, locator_type)
        self.clickelement(self.boarding_point_expand_collapse, locator_type)

    def enterBoardingPointName(self, partial_boardingpoint_name, locator_type="xpath"):
        self.sendkeyselement(partial_boardingpoint_name, self.boarding_point_searchbox, locator_type)

    def getBoardingPointsList(self, req_boardingpoints_list, locator_type="xpath"):
        for boarding_point in self.getElements(self.boarding_points_list, locator_type):
            print("Boarding points are: " + boarding_point.text)
            for req_boardingpoint in req_boardingpoints_list:
                if req_boardingpoint.casefold() == boarding_point.text.casefold():
                    # self.action.move_to_element(boarding_point).click().perform()
                    self.waitElementToBeClickable(5, self.boarding_points_list, locator_type)
                    boarding_point.click()
                    print(req_boardingpoint + " : is selected")
                    # boarding_point.click()
                    # time.sleep(2)
                    break
                else:
                    print(req_boardingpoint + ": is not selected")

    def expandOrCollapseDroppingPoint(self, locator_type="xpath"):
        self.waitElementToBeClickable(5, self.dropping_point_expand_collapse, locator_type)
        self.clickelement(self.dropping_point_expand_collapse, locator_type)

    def enterDroppingPointName(self, partial_droppingpoint_name, locator_type="xpath"):
        self.sendkeyselement(partial_droppingpoint_name, self.dropping_point_searchbox, locator_type)

    def getDroppingPointsList(self, req_droppingpoints_list, locator_type="xpath"):
        for dropping_point in self.getElements(self.dropping_points_list, locator_type):
            print("Boarding points are: " + dropping_point.text)
            for req_droppingpoint in req_droppingpoints_list:
                if req_droppingpoint.casefold() == dropping_point.text.casefold():
                    # self.action.move_to_element(dropping_point).click().perform()
                    self.waitElementToBeClickable(5, self.dropping_points_list, locator_type)
                    dropping_point.click()
                    print(req_droppingpoint + " : is selected")
                    # boarding_point.click()
                    time.sleep(3)
                    break
                else:
                    print(req_droppingpoint + ": is not selected")
