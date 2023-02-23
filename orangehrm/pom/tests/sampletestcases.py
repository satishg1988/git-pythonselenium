import os
import sys
import unittest
import allure
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
    def test_toVerifyValidLogin(self):
        driver = self.driver

        lt = LoginTest(driver)
        lt.validLogin(Data.mobilenumber, "We have sent the verification code to")

    @pytest.mark.run(order=1)
    @pytest.mark.login
    def test_toVerifyInValidLoginWhenMobileNumberIsEmpty(self):
        driver = self.driver

        lt = LoginTest(driver)
        lt.inValidLoginWhenMobileNumberEmpty("Please enter valid mobile number")

    @pytest.mark.login
    @pytest.mark.run(order=3)
    def test_toVerifyInValidLoginWhenMobileNumberIsInvalid(self):
        driver = self.driver

        lt = LoginTest(driver)
        lt.inValidLoginWhenMobileNumberInvalid(Data.invalid_mobile_number, "Please enter valid mobile number")

    @pytest.mark.login
    @pytest.mark.run(order=4)
    def test_toVerifyDefaultStatusOfGetFreeRideCheckbox(self):
        driver = self.driver

        lt = LoginTest(driver)
        lt.verifyFirstRideFreeCheckBox(False)

    @pytest.mark.login
    @pytest.mark.run(order=5)
    def test_toClickGoogleLink(self):
        driver = self.driver
        lt = LoginTest(driver)
        lt.verifyClickLoginWithGoogleLink()

    @pytest.mark.mybookings
    @pytest.mark.run(order=6)
    def test_03_toVerifyPrintBookings(self):
        driver = self.driver
        mb = MyBookings(driver)
        mb.clickPrintBookingsHeaderOption()

    @pytest.mark.mybookings
    @pytest.mark.run(order=7)
    def test_toVerifyCancelBooking(self):
        driver = self.driver
        mb = MyBookings(driver)
        mb.clickCancelBookingHeaderOption()

    @pytest.mark.offers
    @pytest.mark.run(order=8)
    def test_toVerifyUserIsOnOffersPage(self):
        driver = self.driver
        ot = OffersTest(driver)
        ot.verifyTextOfBusBookingsOfferHeading("Bus Booking Offers")

    @pytest.mark.getfreerides
    @pytest.mark.run(order=9)
    def test_toVerifyUserIsOnGetFreeRidesPage(self):
        driver = self.driver
        gfr = GetFreeRides(driver)
        gfr.clickGetFreeRidesHeaderOption()

    @pytest.mark.homepage
    @pytest.mark.run(order=10)
    def test_toVerifySourceCity(self):
        driver = self.driver
        hpt = HomePageTest(driver)
        hpt.verifySourceCity("elu", "Eluru")

    def test_toVerifyDestinationCity(self):
        driver = self.driver
        hpt = HomePageTest(driver)
        hpt.verifyDestinationCity("hyd", "Hyderabad")

    def test_toVerifyUserSelectsValidDate(self):
        driver = self.driver
        hpt = HomePageTest(driver)
        hpt.verifyUserSelectsValidDate("first", "last", "March", "2023", "9")

    def test_toVerifySearchBuses(self):
        driver = self.driver
        hpt = HomePageTest(driver)
        hpt.verifySearchBuses("elu", "Eluru", "hyd", "Hyderabad", "first", "last", "February", "2023", "16")

    def test_toVerifyBusPartnersList(self):
        driver = self.driver
        hpt = HomePageTest(driver)
        hpt.verifyBusPartnersList("elu", "Eluru", "hyd", "Hyderabad", "first", "last", "February", "2023", "18",
                                  "KKaveri Travels", "NON-AC Seater (2 + 2)")

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
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="/usr/local/google/home/sateeshg/git-pythonselenium/orangehrm/reports"))
