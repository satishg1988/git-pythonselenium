from selenium.webdriver.support.ui import WebDriverWait
from orangehrm.pom.locators.allpagelocators import AllLocators as AL
from orangehrm.pom.utilities.events import Events
from selenium.webdriver import ActionChains


class HomePage(Events):
    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(self.driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # calling all the locators from allpageLocators>>AllLocators
        self.bus_link = AL.bus_link
        self.trains_link = AL.trains_link
        self.hotels_link = AL.hotels_link
        self.rentals_link = AL.rentals_link
        self.leaving_from_textbox = AL.leaving_from_textbox
        self.source_cities_list = AL.source_cities_list
        self.going_to_textbox = AL.going_to_textbox
        self.destination_cities_list = AL.destination_cities_list
        self.date_of_journey_field = AL.date_of_journey_field
        self.month_group_pre_xpath = AL.month_group_pre_xpath
        self.month_group_post_xpath = AL.month_group_post_xpath
        self.year_group_pre_xpath = AL.year_group_pre_xpath
        self.year_group_post_xpath = AL.year_group_post_xpath
        self.days_group_pre_xpath = AL.days_group_pre_xpath
        self.days_group_post_xpath = AL.days_group_post_xpath
        self.next_icon = AL.next_icon
        self.search_button = AL.search_button
        self.select_seat_xpath_part_one = AL.select_seat_xpath_part_one
        self.select_seat_xpath_part_two = AL.select_seat_xpath_part_two
        self.select_seat_xpath_part_three = AL.select_seat_xpath_part_three
        self.bus_partners_list = AL.bus_partners_list
        self.bus_partners_type_list = AL.bus_partners_type_list
        self.select_seat_button = AL.select_seat_button

    # click the welcome username link on home page
    def clickBusLink(self, locator_type="id"):
        self.clickelement(self.bus_link, locator_type)

    def clickLeavingFromTextBox(self, locator_type="xpath"):
        self.clickelement(self.leaving_from_textbox, locator_type)

    def enterSourceCityName(self, req_src_city_name, locator_type="xpath"):
        self.sendkeyselement(req_src_city_name, self.leaving_from_textbox, locator_type)

    def selectSourceCityName(self, expected_src_city_name, locator_type="xpath"):
        self.waitForPresenceOfElement(5, self.source_cities_list, locator_type)
        cities_names = self.getElements(self.source_cities_list, locator_type)
        for city_name in cities_names:
            print(city_name.text)
            if city_name.text.casefold() == expected_src_city_name.casefold():
                city_name.click()
                break

    def clickGoingToTextBox(self, locator_type="xpath"):
        self.clickelement(self.going_to_textbox, locator_type)

    def enterDestinationCityName(self, req_dst_city_name, locator_type="xpath"):
        self.sendkeyselement(req_dst_city_name, self.going_to_textbox, locator_type)

    def selectDestinationCitiesNames(self, expected_dst_city_name, locator_type="xpath"):
        self.waitForPresenceOfElement(5, self.destination_cities_list, locator_type)
        destination_cities = self.getElements(self.destination_cities_list, locator_type)
        for city_name in destination_cities:
            print(city_name.text)
            if city_name.text.casefold() == expected_dst_city_name.casefold():
                # self.action.move_to_element(city_name).click().perform()
                city_name.click()
                break

    def clickDate(self, req_group_name, expected_month, expected_year, req_day, locator_type="xpath"):
        self.clickelement(self.date_of_journey_field, locator_type)
        month_final_xpath = self.month_group_pre_xpath + req_group_name + self.month_group_post_xpath
        actual_month = self.getElementText(month_final_xpath, locator_type)
        print("Actual Month Is: " + actual_month)
        year_final_xpath = self.year_group_pre_xpath + req_group_name + self.year_group_post_xpath
        actual_year = self.getElementText(year_final_xpath, locator_type)
        print("Actual Year Is: " + actual_year)
        if (actual_month.casefold() == expected_month.casefold()) and (actual_year == expected_year):
            all_days_final_xpath = self.days_group_pre_xpath + req_group_name + self.days_group_post_xpath
            all_days_list = self.getElements(all_days_final_xpath, locator_type)
            for day in all_days_list:
                print("Days Are: " + day.text)
                # print("Days Status: " + str(day.is_enabled()))
                if day.text.casefold() == req_day.casefold():
                    # self.action.move_to_element(day).click().perform()
                    day.click()
                    # date_of_journey = self.getelement(self.date_of_journey_field, locator_type)
                    # print("Selected Date Is: " + date_of_journey.get_attribute("name"))
                    break
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
        # self.waitElementToBeClickable(5, self.search_button, locator_type)
        self.clickelement(self.search_button, locator_type)

    def getBusPartnersList(self, req_bus_partner, req_bus_partner_type, locator_type="xpath"):
        self.waitForPresenceOfElement(5, self.bus_partners_list, locator_type)
        bus_partners = self.getElements(self.bus_partners_list, locator_type)
        bus_partners_type = self.getElements(self.bus_partners_type_list, locator_type)

        for bus_partner in bus_partners:
            print("Bus Partner  : " + bus_partner.text)
            if bus_partner.text.casefold() == req_bus_partner.casefold():
                for bus_partner_type in bus_partners_type:
                    print("Bus Partner Type : " + bus_partner_type.text)
                    if bus_partner_type.text.casefold() == req_bus_partner_type.casefold():
                        print("Actual " + bus_partner_type.text + " and req bus partner type " + req_bus_partner_type + "are equal")
                        self.clickelement(self.select_seat_button, locator_type)
                        break

    def getBusPartnersTypeList(self, locator_type="xpath"):
        self.getElements(self.bus_partners_type_list, locator_type)

    def selectSeat(self, req_bus_partner, req_bus_partner_type, locator_type="xpath"):
        select_seat_final_xpath = self.select_seat_xpath_part_one + req_bus_partner + self.select_seat_xpath_part_two + req_bus_partner_type + self.select_seat_xpath_part_three
        self.clickelement(select_seat_final_xpath, locator_type)
