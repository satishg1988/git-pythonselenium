from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class Browser():

    # def __init__(self, driver):
    #     self.driver = webdriver.Chrome("/Users/sateeshg/PycharmProjects/PythonSelenium/drivers/chromedriver")
    #     self.driver.maximize_window()

    def browserSetUp(self, browser):
        if browser.casefold() == "chrome":
            self.driver = webdriver.Chrome("E:/PycharmProjects/PythonSelenium/drivers/chromedriver97.exe")
            print("Firefox Browser Launched")
        elif browser.casefold() == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            print("Firefox Browser Launched")
        self.driver.maximize_window()

    def launchUrl(self, url):
        self.driver.get(url)
        print("URL Launch Successful")

