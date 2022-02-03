import os
import sys
import unittest

import pytest

from orangehrm.pom.utilities.data import Data
import HtmlTestRunner
from orangehrm.pom.browsersetup.browseractions import Browser
from orangehrm.pom.pages.homepage import HomePage
from orangehrm.pom.pages.leavelistpage import LeaveList
from orangehrm.pom.pages.loginpage import LoginPage
from orangehrm.pom.pages.menuoptions import MenuOptions

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
    def test_02_toVerifyValidLogin(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.validLogin(Data.uname, Data.pwd)
        lp.verifyLoginSuccess("Dashboard")

    @pytest.mark.run(order=1)
    def test_01_toVerifyInValidLogin(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.inValidLogin()
        lp.verifyLoginFailure("Username cannot be empty")

    @pytest.mark.run(order=3)
    def test_03_toVerifyWelcomeLink(self):
        driver = self.driver
        lp = LoginPage(driver)
        hp = HomePage(driver)
        lp.validLogin(Data.uname, Data.pwd)
        hp.clickWelcomeUserLink()
        hp.verifyWelcomeUser("Welcome")

    @pytest.mark.run(order=4)
    def test_04_headerMenuOptions(self):
        driver = self.driver
        lp = LoginPage(driver)
        # hp = HomePage(driver)
        llp = LeaveList(driver)
        # mo = MenuOptions(driver)

        # mo.clickHeaderMenuOptions("Leave")
        lp.validLogin(Data.uname, Data.pwd)
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
    # def tearDown(self):
    #     driver = self.driver
    #     hp = HomePage(driver)
    #     hp.clickLogoutLink()

    # Runs once after all the tests
    @classmethod
    def tearDown(cls):
        driver = cls.driver
        # hp = HomePage(driver)
        # hp.clickLogoutLink()
        driver.close()
        driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/PycharmProjects/git-pythonselenium/orangehrm/reports'))
