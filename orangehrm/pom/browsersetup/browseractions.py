import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class Browser():

    # def __init__(self, driver):
    #     self.driver = webdriver.Chrome("/Users/sateeshg/PycharmProjects/PythonSelenium/drivers/chromedriver")
    #     self.driver.maximize_window()

    def browserSetUp(self, browser):
        if browser.casefold() == "chrome":
            self.driver = webdriver.Chrome("E:/PycharmProjects/git-pythonselenium/orangehrm/drivers/chromedriver97.exe")
            print("Chrome Browser Launched")
        elif browser.casefold() == "firefox":
            self.driver = webdriver.Firefox(executable_path="E:/PycharmProjects/git-pythonselenium/orangehrm/drivers/geckodriver")
            print("Firefox Browser Launched")
        self.driver.maximize_window()

    def parallelBrowserSetup(self):
        desired_cap = {
            'platform': "windows 10",
            'browserName': "chrome",
        }
        print("Initiating remote driver on platform: " + desired_cap["platform"] + " browser: " + desired_cap["browserName"])
        time.sleep(5)
        self.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=desired_cap)
        self.driver.maximize_window()

    def launchUrl(self, url):
        self.driver.get(url)
        print("URL Launch Successful")

