from orangehrm.pom.pages.homepage import HomePage
from orangehrm.pom.pages.leftpanel import LeftPanel


class HomePageTest:
    def __init__(self, driver):
        self.driver = driver

    def verifySourceCity(self, req_city_name, expected_city_name):
        driver = self.driver
        hp = HomePage(driver)
        hp.clickBusLink()
        hp.clickLeavingFromTextBox()
        hp.enterSourceCityName(req_city_name)
        hp.selectSourceCityName(expected_city_name)

    def verifyDestinationCity(self, req_city_name, expected_city_name):
        driver = self.driver
        hp = HomePage(driver)
        hp.clickBusLink()
        hp.clickGoingToTextBox()
        hp.enterDestinationCityName(req_city_name)
        hp.selectDestinationCitiesNames(expected_city_name)

    def verifyUserSelectsValidDate(self, req_group_name1, req_group_name2, expected_month, expected_year, req_day):
        driver = self.driver
        hp = HomePage(driver)
        hp.selectDate(req_group_name1, req_group_name2, expected_month, expected_year, req_day)

    def verifySearchBuses(self, req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name, req_group_name1,
                          req_group_name2, expected_month, expected_year, req_day):
        driver = self.driver
        hp = HomePage(driver)

        hp.clickBusLink()
        hp.clickLeavingFromTextBox()
        hp.enterSourceCityName(req_src_city_name)
        hp.selectSourceCityName(expected_src_city_name)
        hp.clickGoingToTextBox()
        hp.enterDestinationCityName(req_dst_city_name)
        hp.selectDestinationCitiesNames(expected_dst_city_name)
        hp.selectDate(req_group_name1, req_group_name2, expected_month, expected_year, req_day)
        hp.clickSearchButton()

    def verifySelectSeat(self, req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name, req_group_name1,
                         req_group_name2, expected_month, expected_year, req_day, req_bus_partner, req_bus_partner_type):
        driver = self.driver
        hp = HomePage(driver)
        hp.clickBusLink()
        hp.clickLeavingFromTextBox()
        hp.enterSourceCityName(req_src_city_name)
        hp.selectSourceCityName(expected_src_city_name)
        hp.clickGoingToTextBox()
        hp.enterDestinationCityName(req_dst_city_name)
        hp.selectDestinationCitiesNames(expected_dst_city_name)
        hp.selectDate(req_group_name1, req_group_name2, expected_month, expected_year, req_day)
        hp.clickSearchButton()
        hp.clickSelectSeatButton(req_bus_partner, req_bus_partner_type)
        hp.getSeatsList()

    def verifyShowIcon(self, req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name, req_group_name1,
                       req_group_name2, expected_month, expected_year, req_day):
        driver = self.driver
        hp = HomePage(driver)
        hp.clickBusLink()
        hp.clickLeavingFromTextBox()
        hp.enterSourceCityName(req_src_city_name)
        hp.selectSourceCityName(expected_src_city_name)
        hp.clickGoingToTextBox()
        hp.enterDestinationCityName(req_dst_city_name)
        hp.selectDestinationCitiesNames(expected_dst_city_name)
        hp.selectDate(req_group_name1, req_group_name2, expected_month, expected_year, req_day)
        hp.clickSearchButton()
        HomePage(driver).clickShowIcon()

    def verifyPriceDropIsSelected(self, req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name, req_group_name1,
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
        hp.selectDestinationCitiesNames(expected_dst_city_name)
        hp.selectDate(req_group_name1, req_group_name2, expected_month, expected_year, req_day)
        hp.clickSearchButton()
        lp.selectPriceDropCheckbox()
