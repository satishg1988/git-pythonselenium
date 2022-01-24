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

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


class LoginTest(unittest.TestCase, Data):

    # Runs once before all the tests
    @classmethod
    def setUpClass(cls):
        b = Browser
        b.browserSetUp(cls, "CHROME")
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
        hp.click_welcome_admin_link()

    @pytest.mark.run(order=3)
    def test_headerMenuOptions(self):
        driver = self.driver
        hp = HomePage(driver)
        llp = LeaveList(driver)

        hp.click_header_menu_options("LEAVE")
        hp.click_header_leave_link()
        llp.click_fromdate_leavelist("1994", "SEP", "11")
        llp.click_todate_leavelist("2021", "JUN", "22")
        llp.selectLeaveStatus()
        llp.searchEmployeeName("te")
        llp.selectSubUnit('  Sales')

    # Runs once after every test
    def tearDown(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.click_logout_link()

    # Runs once after all the tests
    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/PycharmProjects/git-pythonselenium/orangehrm/reports'))
