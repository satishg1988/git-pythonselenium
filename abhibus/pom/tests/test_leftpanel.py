from abhibus.pom.pages.leftpanel import LeftPanel
from abhibus.pom.tests.test_homepage import HomePageTest


class LeftPanelTest:
    def __init__(self, driver):
        self.driver = driver

    def verifyBusType(self, req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name, req_group_name1,
                      req_group_name2, expected_month, expected_year, req_day, req_bustype_list):
        hpt = HomePageTest(driver=self.driver)
        lp = LeftPanel(driver=self.driver)
        hpt.verifySearchBuses(req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name, req_group_name1,
                              req_group_name2, expected_month, expected_year, req_day)
        lp.selectBusTypeFilter(req_bustype_list)
        lp.getClearAllText()

    def verifyBusPartner(self, req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name,
                         req_group_name1, req_group_name2, expected_month, expected_year, req_day,
                         req_partial_buspartner_name, req_buspartner_list):
        hpt = HomePageTest(driver=self.driver)
        lp = LeftPanel(driver=self.driver)
        hpt.verifySearchBuses(req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name, req_group_name1,
                              req_group_name2, expected_month, expected_year, req_day)
        lp.expandOrCollapseBusPartner()
        lp.enterBusPartnerName(req_partial_buspartner_name)
        lp.getBusPartnersList(req_buspartner_list)

    def verifyBoardingPoints(self, req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name,
                             req_group_name1, req_group_name2, expected_month, expected_year, req_day,
                             partial_boardingpoint_name, req_boardingpoints_list):
        hpt = HomePageTest(driver=self.driver)
        lp = LeftPanel(driver=self.driver)
        hpt.verifySearchBuses(req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name, req_group_name1,
                              req_group_name2, expected_month, expected_year, req_day)
        lp.expandOrCollapseBoardingPoint()
        lp.enterBoardingPointName(partial_boardingpoint_name)
        lp.getBoardingPointsList(req_boardingpoints_list)

    def verifyDroppingPoints(self, req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name,
                             req_group_name1, req_group_name2, expected_month, expected_year, req_day,
                             partial_droppingpoint_name, req_droppingpoints_list):
        hpt = HomePageTest(driver=self.driver)
        lp = LeftPanel(driver=self.driver)
        hpt.verifySearchBuses(req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name, req_group_name1,
                              req_group_name2, expected_month, expected_year, req_day)
        lp.expandOrCollapseDroppingPoint()
        lp.enterDroppingPointName(partial_droppingpoint_name)
        lp.getDroppingPointsList(req_droppingpoints_list)

    def verifyBusFilters(self, req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name,req_group_name1,
                         req_group_name2, expected_month, expected_year, req_day,
                         req_bustype_list,
                         req_partial_buspartner_name, req_buspartner_list,
                         partial_boardingpoint_name, req_boardingpoints_list,
                         partial_droppingpoint_name, req_droppingpoints_list):
        hpt = HomePageTest(driver=self.driver)
        lp = LeftPanel(driver=self.driver)
        hpt.verifySearchBuses(req_src_city_name, expected_src_city_name, req_dst_city_name, expected_dst_city_name, req_group_name1,
                              req_group_name2, expected_month, expected_year, req_day)
        lp.selectBusTypeFilter(req_bustype_list)
        lp.getClearAllText()

        lp.expandOrCollapseBusPartner()
        lp.enterBusPartnerName(req_partial_buspartner_name)
        lp.getBusPartnersList(req_buspartner_list)

        lp.expandOrCollapseBoardingPoint()
        lp.enterBoardingPointName(partial_boardingpoint_name)
        lp.getBoardingPointsList(req_boardingpoints_list)

        lp.expandOrCollapseDroppingPoint()
        lp.enterDroppingPointName(partial_droppingpoint_name)
        lp.getDroppingPointsList(req_droppingpoints_list)

