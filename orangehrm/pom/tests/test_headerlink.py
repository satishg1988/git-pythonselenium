from orangehrm.pom.pages.homepage import HomePage
from orangehrm.pom.pages.loginpage import LoginPage
from orangehrm.pom.utilities.data import Data


class TestHeaderLinks(Data):
    def test_headerLink(self):
        driver = self.driver

        lp = LoginPage(driver)
        hp = HomePage(driver)

        lp.validLogin(Data.uname, Data.pwd)
        lp.verifyLoginSuccess()
        hp.clickWelcomeUserLink()
