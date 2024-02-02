from abhibus.pom.pages.homepage import HomePage
from abhibus.pom.pages.leftpanel import LeftPanel


def test_verifySourceCity(setUp, partial_src_city_name="hyd", expected_src_city_name="Hyderabad"):
    hp = HomePage(setUp)
    hp.clickBusLink()
    hp.clickFromStation()
    hp.enterSourceCityName(partial_src_city_name)
    assert hp.selectSourceCityName(expected_src_city_name).casefold() == expected_src_city_name.casefold()
    print("Source City Verified Successfully")


def test_verifyDestinationCity(setUp, partial_city_name="janga", expected_dst_city_name="Jangareddy Gudem"):
    hp = HomePage(setUp)
    hp.clickBusLink()
    hp.clickToStation()
    hp.enterToStationName(partial_city_name)
    assert hp.selectDestinationCityName(expected_dst_city_name).casefold() == expected_dst_city_name.casefold()
    print("Destination city verified successfully")


def test_getDefaultDate(setUp, expected_default_date="02/02/2024"):
    hp = HomePage(setUp)
    assert hp.getDefaultDate().casefold() == expected_default_date.casefold()


def test_verifyUserSelectsValidDate(setUp, expected_month="February", expected_year="2024", req_day="3"):
    hp = HomePage(setUp)
    hp.clickDate(expected_month, expected_year, req_day)

def verifySearchBuses(self, req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name,
                      req_group_name1,
                      req_group_name2, expected_month, expected_year, req_day):
    driver = self.driver
    hp = HomePage(driver)

    hp.clickBusLink()
    hp.clickLeavingFromTextBox()
    hp.enterSourceCityName(req_src_city_name)
    hp.selectSourceCityName(expected_src_city_name)
    hp.clickGoingToTextBox()
    hp.enterDestinationCityName(req_dst_city_name)
    hp.selectDestinationCityName(expected_dst_city_name)
    hp.selectDate(req_group_name1, req_group_name2, expected_month, expected_year, req_day)
    hp.clickSearchButton()


def verifySelectSeat(self, req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name,
                     req_group_name1,
                     req_group_name2, expected_month, expected_year, req_day, req_bus_partner, req_bus_partner_type,
                     req_departure_time,
                     req_seat_nums):
    driver = self.driver
    hp = HomePage(driver)
    hp.clickBusLink()
    hp.clickLeavingFromTextBox()
    hp.enterSourceCityName(req_src_city_name)
    hp.selectSourceCityName(expected_src_city_name)
    hp.clickGoingToTextBox()
    hp.enterDestinationCityName(req_dst_city_name)
    hp.selectDestinationCityName(expected_dst_city_name)
    hp.selectDate(req_group_name1, req_group_name2, expected_month, expected_year, req_day)
    hp.clickSearchButton()
    hp.clickSelectSeatButton(req_bus_partner, req_bus_partner_type, req_departure_time)
    hp.selectRequiredSeat(req_seat_nums)
    hp.selectBoardingPoint(req_bus_partner, req_bus_partner_type, req_departure_time)
    hp.selectDroppingPoint(req_bus_partner, req_bus_partner_type, req_departure_time)
    hp.clickContinueToPaymentButton(req_bus_partner, req_bus_partner_type, req_departure_time)


def verifyShowIcon(self, req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name,
                   req_group_name1,
                   req_group_name2, expected_month, expected_year, req_day):
    driver = self.driver
    hp = HomePage(driver)
    hp.clickBusLink()
    hp.clickLeavingFromTextBox()
    hp.enterSourceCityName(req_src_city_name)
    hp.selectSourceCityName(expected_src_city_name)
    hp.clickGoingToTextBox()
    hp.enterDestinationCityName(req_dst_city_name)
    hp.selectDestinationCityName(expected_dst_city_name)
    hp.selectDate(req_group_name1, req_group_name2, expected_month, expected_year, req_day)
    hp.clickSearchButton()
    HomePage(driver).clickShowIcon()


def verifyPriceDropIsSelected(self, req_src_city_name, expected_src_city_name, req_dst_city_name,
                              expected_dst_city_name, req_group_name1,
                              req_group_name2, expected_month, expected_year, req_day):
    driver = self.driver
    hp = HomePage(driver)
    lp = LeftPanel(driver=self.driver)
    hp.clickBusLink()
    hp.clickLeavingFromTextBox()
    hp.enterSourceCityName(req_src_city_name)
    hp.selectSourceCityName(expected_src_city_name)
    hp.clickGoingToTextBox()
    hp.enterDestinationCityName(req_dst_city_name)
    hp.selectDestinationCityName(expected_dst_city_name)
    hp.selectDate(req_group_name1, req_group_name2, expected_month, expected_year, req_day)
    hp.clickSearchButton()
    pricedrop_checkbox_defstatus, pricedrop_checkbox_status = lp.selectPriceDropCheckbox()
    assert pricedrop_checkbox_defstatus is False, "Pricedrop checkbox status: failed"
    print("Price Drop checkbox default status verification successful")
    assert pricedrop_checkbox_status is True, "Pricedrop checkbox status: Failed"
    print("Price Drop checkbox status verification successful")
