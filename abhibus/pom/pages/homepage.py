import time

from selenium.webdriver.support.ui import WebDriverWait
from abhibus.pom.locators.allpagelocators import AllLocators as AL
from abhibus.pom.utilities.events import Events
from selenium.webdriver import ActionChains


class HomePage(Events):
    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(self.driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.events = Events(self.driver)

        # calling all the locators from allpageLocators>>AllLocators
        self.bus_link = AL.buses_link
        self.trains_link = AL.trains_link
        self.hotels_link = AL.hotels_link
        self.rentals_link = AL.rentals_link
        self.from_station_textbox = AL.from_station_textbox
        self.source_cities_list = AL.source_cities_list
        self.to_station_textbox = AL.to_station_textbox
        self.destination_cities_list = AL.destination_cities_list
        self.journey_date = AL.journey_date
        self.month_name = AL.month_name
        self.year_name = AL.year_name
        self.dates_list = AL.dates_list
        self.month_group_pre_xpath = AL.month_group_pre_xpath
        self.month_group_post_xpath = AL.month_group_post_xpath
        self.year_group_pre_xpath = AL.year_group_pre_xpath
        self.year_group_post_xpath = AL.year_group_post_xpath
        self.days_group_pre_xpath = AL.days_group_pre_xpath
        self.days_group_post_xpath = AL.days_group_post_xpath
        self.next_icon = AL.next_icon
        self.search_button = AL.search_button
        self.selectseat_button_xpath_part_one = AL.selectseat_button_xpath_part_one
        self.selectseat_button_xpath_part_two = AL.selectseat_button_xpath_part_two
        self.selectseat_button_xpath_part_three = AL.selectseat_button_xpath_part_three
        self.selectseat_button_xpath_part_four = AL.selectseat_button_xpath_part_four
        self.bus_partners_list = AL.bus_partners_list
        # self.bus_partners_type_list = AL.bus_partners_type_list
        # self.select_seat_button = AL.select_seat_button
        self.seat_button_xpath_part_one = AL.seat_button_xpath_part_one
        self.seat_button_xpath_part_two = AL.seat_button_xpath_part_two
        self.boardingpoint_dropdown_xpath_part_one = AL.boardingpoint_dropdown_xpath_part_one
        self.boardingpoint_dropdown_xpath_part_two = AL.boardingpoint_dropdown_xpath_part_two
        self.boardingpoint_dropdown_xpath_part_three = AL.boardingpoint_dropdown_xpath_part_three
        self.boardingpoint_dropdown_xpath_part_four = AL.boardingpoint_dropdown_xpath_part_four

        self.droppingpoint_dropdown_xpath_part_one = AL.droppingpoint_dropdown_xpath_part_one
        self.droppingpoint_dropdown_xpath_part_two = AL.droppingpoint_dropdown_xpath_part_two
        self.droppingpoint_dropdown_xpath_part_three = AL.droppingpoint_dropdown_xpath_part_three
        self.droppingpoint_dropdown_xpath_part_four = AL.droppingpoint_dropdown_xpath_part_four
        # self.boardingpoint_dropdown = AL.boardingpoint_dropdown
        self.boardingpoint_dropdown_list = AL.boardingpoint_dropdown_list
        # self.droppingpoint_dropdown = AL.droppingpoint_dropdown
        self.droppingpoint_dropdown_list = AL.droppingpoint_dropdown_list
        self.continuetopayment_button_xpath_part_one = AL.continuetopayment_button_xpath_part_one
        self.continuetopayment_button_xpath_part_two = AL.continuetopayment_button_xpath_part_two
        self.continuetopayment_button_xpath_part_three = AL.continuetopayment_button_xpath_part_three
        self.continuetopayment_button_xpath_part_four = AL.continuetopayment_button_xpath_part_four
        # self.continue_to_payment_button = AL.continue_to_payment_button
        self.show_icon = AL.show_icon
        self.hide_icon = AL.hide_icon

    # click the welcome username link on home page
    def clickBusLink(self):
        self.events.clickElement(self.bus_link, "id")

    def clickFromStation(self):
        self.events.waitForPresenceOfElement(10, self.from_station_textbox, "xpath")
        self.events.clickElement(self.from_station_textbox, "xpath")

    def enterSourceCityName(self, partial_src_city_name):
        self.events.waitForPresenceOfElement(10, self.from_station_textbox, "xpath")
        self.events.sendkeyselement(partial_src_city_name, self.from_station_textbox, "xpath")

    def selectSourceCityName(self, expected_src_city_name):
        received_src_cityname = None
        self.events.waitForPresenceOfElement(10, self.source_cities_list, "xpath")
        cities_names = self.events.getElements(self.source_cities_list, "xpath")
        for city_name in cities_names:
            received_src_cityname = city_name.text
            print(received_src_cityname)
            if received_src_cityname.casefold() == expected_src_city_name.casefold():
                city_name.click()
                break
        return received_src_cityname

    def clickToStation(self):
        self.events.waitForPresenceOfElement(10, self.to_station_textbox, "xpath")
        self.events.clickElement(self.to_station_textbox, "xpath")

    def enterToStationName(self, partial_city_name):
        self.events.waitForPresenceOfElement(10, self.to_station_textbox, "xpath")
        self.events.sendkeyselement(partial_city_name, self.to_station_textbox, "xpath")

    def selectDestinationCityName(self, expected_dst_city_name):
        received_dst_cityname = None
        self.events.waitForPresenceOfElement(5, self.destination_cities_list, "xpath")
        destination_cities = self.events.getElements(self.destination_cities_list, "xpath")
        for city_name in destination_cities:
            received_dst_cityname = city_name.text
            print(received_dst_cityname)
            if received_dst_cityname.casefold() == expected_dst_city_name.casefold():
                # self.action.move_to_element(city_name).click().perform()
                city_name.click()
                break
        return received_dst_cityname

    def getDefaultDate(self):
        self.events.waitElementToBeClickable(10, self.journey_date, "xpath")
        default_date = self.events.getelement(self.journey_date, "xpath").get_attribute("value")
        # print(default_date)
        return default_date

    def clickDate(self, expected_month, expected_year, req_day):
        self.events.waitForPresenceOfElement(10, self.journey_date, "xpath")
        journey_date_element = self.events.getelement(self.journey_date, "xpath")
        self.action.move_to_element(journey_date_element).click().perform()
        # self.events.clickElement(self.journey_date, "xpath")
        actual_month = self.events.getElementText(self.month_name, "xpath")
        actual_year = self.events.getElementText(self.year_name, "xpath")
        print("Actual Month and Year: ", actual_month, actual_year)
        if (actual_month.casefold() == expected_month.casefold()) and (actual_year == expected_year):
            all_days_list = self.getElements(self.dates_list, "xpath")
            for day in all_days_list:
                print("Day is: " + day.text)
                print("Day Status is: " + str(day.is_enabled()))
                try:
                    if day.text.casefold() == req_day.casefold():
                        # self.action.move_to_element(day).click().perform()
                        day.click()
                        # date_of_journey = self.getelement(self.date_of_journey_field, locator_type)
                        # print("Selected Date Is: " + date_of_journey.get_attribute("name"))
                        break
                except:
                    print(req_day + ": is not available")

                    # return True
        return False

    def clickNextIconOnDatePicker(self):
        self.clickelement(self.next_icon, locator_type="xpath")

    def selectDate(self, req_group_name1, req_group_name2, expected_month, expected_year, req_day):
        driver = self.driver
        hp = HomePage(driver)
        # result = False
        result = hp.clickDate(req_group_name1, expected_month, expected_year, req_day)
        print(result)
        if not result:
            result = hp.clickDate(req_group_name2, expected_month, expected_year, req_day)
            print(result)
        if not result:
            hp.clickNextIconOnDatePicker()
            hp.clickDate(req_group_name2, expected_month, expected_year, req_day)

    def clickSearchButton(self, locator_type="linktext"):
        self.waitElementToBeClickable(5, self.search_button, locator_type)
        self.clickelement(self.search_button, locator_type)
        time.sleep(2)

    # def getBusPartnersList(self, req_bus_partner, req_bus_partner_type, locator_type="xpath"):
    #     self.waitForPresenceOfElement(5, self.bus_partners_list, locator_type)
    #     bus_partners = self.getElements(self.bus_partners_list, locator_type)
    #     bus_partners_type = self.getElements(self.bus_partners_type_list, locator_type)
    #
    #     for bus_partner in bus_partners:
    #         print("Bus Partner  : " + bus_partner.text)
    #         if bus_partner.text.casefold() == req_bus_partner.casefold():
    #             for bus_partner_type in bus_partners_type:
    #                 print("Bus Partner Type : " + bus_partner_type.text)
    #                 if bus_partner_type.text.casefold() == req_bus_partner_type.casefold():
    #                     print("Actual " + bus_partner_type.text + " and req bus partner type " + req_bus_partner_type + "are equal")
    #                     self.clickelement(self.select_seat_button, locator_type)
    #                     break
    #
    # def getBusPartnersTypeList(self, locator_type="xpath"):
    #     self.getElements(self.bus_partners_type_list, locator_type)

    def clickSelectSeatButton(self, req_bus_partner, req_bus_partner_type, req_departure_time, locator_type="xpath"):
        selectseat_button_final_xpath = self.selectseat_button_xpath_part_one + req_bus_partner + self.selectseat_button_xpath_part_two \
                                  + req_bus_partner_type + self.selectseat_button_xpath_part_three + req_departure_time + self.selectseat_button_xpath_part_four
        # self.driver.execute_script("window.scrollTo(0,500)")
        element = self.getelement(selectseat_button_final_xpath, locator_type)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        # element.click()
        # self.waitElementToBeClickable(20, selectseat_button_final_xpath, locator_type)
        # self.action.move_to_element(self.getelement(selectseat_button_final_xpath, locator_type)).click().perform()
        # self.clickelement(selectseat_button_final_xpath, locator_type)
        time.sleep(2)

    def selectRequiredSeat(self, req_seat_nums, locator_type="xpath"):
        # req_seats_list = ["OU7", "OU8", "OU9"]
        status = None
        for req_seat_num in req_seat_nums:
            try:
                seat_button_xpath_final = self.seat_button_xpath_part_one + req_seat_num + self.seat_button_xpath_part_two
                element = self.getelement(seat_button_xpath_final, locator_type)
                if element.is_enabled():
                    print("Element Status Is: " + str(element.is_enabled()))
                    # self.waitForPresenceOfElement(5, seat_button_xpath_final, locator_type)
                    self.waitElementToBeClickable(15, seat_button_xpath_final, locator_type)
                    self.action.move_to_element(element).click().perform()
                    # self.clickelement(seat_button_xpath_final, locator_type)
                    # time.sleep(5)
                status = True
            except AttributeError:
                print("Error Occurred - AttributeError: 'NoneType' object has no attribute 'is_enabled")
                status = False
        return status

    def selectBoardingPoint(self, req_bus_partner, req_bus_partner_type, req_departure_time, locator_type="xpath"):
        boardingpoint_dropdown_xpath_final = self.boardingpoint_dropdown_xpath_part_one + req_bus_partner + \
                                             self.boardingpoint_dropdown_xpath_part_two + req_bus_partner_type + \
                                             self.boardingpoint_dropdown_xpath_part_three + req_departure_time + \
                                             self.boardingpoint_dropdown_xpath_part_four
        # self.clickelement(boardingpoint_dropdown_xpath_final, locator_type)
        self.selectElementByVisibleText("Eluru Bypass-23:05", boardingpoint_dropdown_xpath_final, locator_type)
        time.sleep(5)

    def selectDroppingPoint(self, req_bus_partner, req_bus_partner_type, req_departure_time, locator_type="xpath"):
        droppingpoint_dropdown_xpath_final = self.droppingpoint_dropdown_xpath_part_one + req_bus_partner + \
                                             self.droppingpoint_dropdown_xpath_part_two + req_bus_partner_type + \
                                             self.droppingpoint_dropdown_xpath_part_three + req_departure_time + \
                                             self.droppingpoint_dropdown_xpath_part_four
        # self.clickelement(droppingpoint_dropdown_xpath_final, locator_type)
        self.selectElementByVisibleText("Alwyn X road-07:10", droppingpoint_dropdown_xpath_final, locator_type)

    def clickContinueToPaymentButton(self, req_bus_partner, req_bus_partner_type, req_departure_time, locator_type="xpath"):
        continuetopayment_button_xpath_final = self.continuetopayment_button_xpath_part_one + req_bus_partner + \
                                             self.continuetopayment_button_xpath_part_two + req_bus_partner_type + \
                                             self.continuetopayment_button_xpath_part_three + req_departure_time + \
                                             self.continuetopayment_button_xpath_part_four
        if self.isElementEnabled(continuetopayment_button_xpath_final, locator_type):
            self.clickelement(continuetopayment_button_xpath_final, locator_type)
            # time.sleep(5)

    def clickShowIcon(self, locator_type="css"):
        if self.isElementDisplayed(self.show_icon, locator_type):
            self.waitElementToBeClickable(5, self.show_icon, locator_type)
            self.clickelement(self.show_icon, locator_type)
            time.sleep(5)
