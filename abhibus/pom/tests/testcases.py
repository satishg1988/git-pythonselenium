import os
import sys
import unittest

import pytest

from abhibus.pom.utilities.data import Data
import HtmlTestRunner
from abhibus.pom.browsersetup.browseractions import Browser
from abhibus.pom.pages.homepage import HomePage
from abhibus.pom.pages.leavelistpage import LeaveList
from abhibus.pom.pages.loginpage import LoginPage
from abhibus.pom.pages.menuoptions import MenuOptions


sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


class TestCases(unittest.TestCase, Data):

    # Runs once before all the tests
    @classmethod
    def setUpClass(cls):
        b = Browser
        b.browserSetUp(cls, "firefox")
        # b.parallelBrowserSetup(cls)
        b.launchUrl(cls, Data.url)

    # Runs once before every test
    def setUp(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.validLogin(Data.uname, Data.pwd)
        lp.verifyLoginSuccess()

    # @pytest.mark.run(order=1)
    # def test_validLogin(self):
    #     driver = self.driver
    #     lp = LoginPage(driver)
    #     lp.verifyloginSuccess()

    @pytest.mark.run(order=2)
    def test_headerLink(self):
        driver = self.driver

        hp = HomePage(driver)
        hp.clickWelcomeUserLink()

    @pytest.mark.run(order=3)
    def test_headerMenuOptions(self):
        driver = self.driver
        # hp = HomePage(driver)
        llp = LeaveList(driver)
        # mo = MenuOptions(driver)
        # mo.clickHeaderMenuOptions("Leave")
        llp.clickApplyLeaveSubMenu("Leave", "Apply")
        llp.clickAddEntitlementsSubMenu("Leave", "Entitlements", "Add Entitlements")
        llp.clickLeaveListSubMenu("Leave", "Leave List")
        llp.click_fromdate_leavelist("1994", "SEP", "11")
        llp.click_todate_leavelist("2021", "JUN", "22")
        llp.selectLeaveStatus()
        llp.searchEmployeeName("te", "Garry White")
        llp.selectSubUnit('  Sales')
        llp.selectPastEmployees()
        llp.clickSearch()

    # Runs once after every test
    def tearDown(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.clickLogoutLink()

    # Runs once after all the tests
    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/PycharmProjects/git-pythonselenium/abhibus/reports'))
