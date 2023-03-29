import os
import sys
import unittest
import HtmlTestRunner
import pytest

from orangehrm.pom.browsersetup.browseractions import Browser
from orangehrm.pom.pages.homepage import HomePage
from orangehrm.pom.tests.test_homepage import HomePageTest
from orangehrm.pom.pages.loginpage import LoginPage
from orangehrm.pom.tests.test_login import LoginTest
from orangehrm.pom.utilities.data import Data
from orangehrm.pom.pages.offers import Offers
from orangehrm.pom.tests.test_offers import OffersTest
from orangehrm.pom.pages.mybookings import MyBookings
from orangehrm.pom.pages.getfreerides import GetFreeRides
from orangehrm.pom.tests.test_leftpanel import LeftPanelTest

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


class TestCases(unittest.TestCase, Data):

    # Runs once before all the tests
    @classmethod
    def setUp(cls):
        b = Browser
        b.browserSetUp(cls, "Chrome")
        # b.parallelBrowserSetup(cls)
        b.launchUrl(cls, Data.url)

    @pytest.mark.run(order=2)
    @pytest.mark.login
    # @pytest.mark.skip
    def test_toVerifyValidLogin(self):
        driver = self.driver

        lt = LoginTest(driver)
        # lt.verifyValidLogin(Data.mobilenumber, "We have sent the verification code to")
        lt.verifyValidLogin(Data.mobilenumber, "Your OTP request will be proccessed.")

    @pytest.mark.run(order=1)
    @pytest.mark.login
    def test_toVerifyInValidLoginWhenMobileNumberIsEmpty(self):
        driver = self.driver

        # lt = LoginTest(driver)
        LoginTest(driver).inValidLoginWhenMobileNumberEmpty("Please enter valid mobile number")
        # lt.inValidLoginWhenMobileNumberEmpty("Please enter valid mobile number")

    @pytest.mark.login
    @pytest.mark.run(order=3)
    def test_toVerifyInValidLoginWhenMobileNumberIsInvalid(self):
        driver = self.driver

        lt = LoginTest(driver)
        lt.inValidLoginWhenMobileNumberInvalid(Data.invalid_mobile_number, "Please enter valid mobile number")

    @pytest.mark.login
    @pytest.mark.run(order=4)
    # @pytest.mark.skip
    def test_toVerifyDefaultStatusOfGetFreeRideCheckbox(self):
        driver = self.driver

        lt = LoginTest(driver)
        lt.verifyFirstRideFreeCheckBox(False)

    @pytest.mark.login
    @pytest.mark.run(order=5)
    # @pytest.mark.skip
    def test_toClickGoogleLink(self):
        driver = self.driver
        lt = LoginTest(driver)
        lt.verifyClickLoginWithGoogleLink(True)

    @pytest.mark.mybookings
    @pytest.mark.run(order=6)
    @pytest.mark.skip
    def test_03_toVerifyPrintBookings(self):
        driver = self.driver
        mb = MyBookings(driver)
        mb.clickPrintBookingsHeaderOption()

    @pytest.mark.mybookings
    @pytest.mark.run(order=7)
    @pytest.mark.skip
    def test_toVerifyCancelBooking(self):
        driver = self.driver
        mb = MyBookings(driver)
        mb.clickCancelBookingHeaderOption()

    @pytest.mark.offers
    @pytest.mark.run(order=8)
    @pytest.mark.skip
    def test_toVerifyUserIsOnOffersPage(self):
        driver = self.driver
        ot = OffersTest(driver)
        ot.verifyTextOfBusBookingsOfferHeading("Bus Booking Offers")

    @pytest.mark.getfreerides
    @pytest.mark.run(order=9)
    @pytest.mark.skip
    def test_toVerifyUserIsOnGetFreeRidesPage(self):
        driver = self.driver
        gfr = GetFreeRides(driver)
        gfr.clickGetFreeRidesHeaderOption()

    @pytest.mark.homepage
    @pytest.mark.run(order=10)
    @pytest.mark.skip
    def test_toVerifySourceCity(self):
        driver = self.driver
        hpt = HomePageTest(driver)
        hpt.verifySourceCity("elu", "Eluru")

    @pytest.mark.skip
    def test_toVerifyDestinationCity(self):
        driver = self.driver
        hpt = HomePageTest(driver)
        hpt.verifyDestinationCity("hyd", "Hyderabad")

    # @pytest.mark.skip
    def test_toVerifyUserSelectsValidDate(self):
        driver = self.driver
        hpt = HomePageTest(driver)
        hpt.verifyUserSelectsValidDate("first", "last", "March", "2023", "31")

    @pytest.mark.skip
    def test_toVerifySearchBuses(self):
        driver = self.driver
        hpt = HomePageTest(driver)
        hpt.verifySearchBuses("elu", "Eluru", "hyd", "Hyderabad", "first", "last", "March", "2023", "31")

    # @pytest.mark.skip
    def test_toVerifySelectSeat(self):
        driver = self.driver
        hpt = HomePageTest(driver)
        hpt.verifySelectSeat("elu", "Eluru", "hyd", "Hyderabad", "first", "last", "March", "2023", "31",
                             "Dharani Tours and Travels", "NON-AC Seater/Sleeper (2 + 1)")

    def test_toVerifyClickShowIcon(self):
        driver = self.driver
        hpt = HomePageTest(driver)
        hpt.verifyShowIcon("elu", "Eluru", "hyd", "Hyderabad", "first", "last", "March", "2023", "31")

    def test_toVerifyPriceDropIsSelected(self):
        driver = self.driver
        hpt = HomePageTest(driver)
        hpt.verifyPriceDropIsSelected("elu", "Eluru", "hyd", "Hyderabad", "first", "last", "March", "2023", "31")

    def test_toVerifyUserSelectsBusType(self):
        lpt = LeftPanelTest(driver=self.driver)
        lpt.verifyBusType("elu", "Eluru", "hyd", "Hyderabad", "first", "last", "March", "2023", "31", ["AC", "SLEEPER"])

    def test_toVerifyUserSelectsReqBusPartners(self):
        lpt = LeftPanelTest(driver=self.driver)
        lpt.verifyBusPartner("elu", "Eluru", "hyd", "Hyderabad", "first", "last", "March", "2023", "31",
                             "or", ["Orange Tours and Travels", "APSRTC", "morning star travels"])

    def test_toVerifyBoardingPoints(self):
        lpt = LeftPanelTest(driver=self.driver)
        lpt.verifyBoardingPoints("elu", "Eluru", "hyd", "Hyderabad", "first", "last", "March", "2023", "31",
                                 "elr", ["Satrampadu Elr", "Eluru", "Fire Station-elr"])

    def test_toVerifyDroppingPoints(self):
        lpt = LeftPanelTest(driver=self.driver)
        lpt.verifyDroppingPoints("elu", "Eluru", "hyd", "Hyderabad", "first", "last", "March", "2023", "31",
                                 "x road", ["Allywn X Road , Near Orange Travels Office ,Bata Showroom", "Alwyn x road",
                                            "Uppal X road"])

    def test_toVerifyFilteringBus(self):
        lpt = LeftPanelTest(driver=self.driver)
        lpt.verifyBusFilters("elu", "Eluru", "hyd", "Hyderabad", "first", "last", "March", "2023", "31",
                             ["AC", "SLEEPER"],
                             "or", ["Orange Tours and Travels"],
                             "elr", ["Satrampadu Elr", "Eluru", "Fire Station-elr"],
                             "x road", ["Allywn X Road , Near Orange Travels Office ,Bata Showroom", "Alwyn x road",
                                        "Uppal X road"])

    # Runs once after every test
    def tearDown(self):
        driver = self.driver
        driver.close()
        driver.quit()

    # Runs once after all the tests
    # @classmethod
    # def tearDown(cls):
    #     driver = cls.driver
    # hp = HomePage(driver)
    # hp.clickLogoutLink()
    # driver.close()
    # driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="/usr/local/google/home/sateeshg/git-pythonselenium/orangehrm/reports"))
