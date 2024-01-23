import time
import threading

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from webdriver_manager.firefox import GeckoDriverManager


class Browser:
    def browserSetUp(self, browser):
        if browser.casefold() == "chrome":
            # self.driver = webdriver.Chrome("/usr/local/google/home/sateeshg/git-pythonselenium/abhibus/drivers/chromedriver119")
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            # self.driver = webdriver.Chrome()
            print("Chrome Browser Launched")
        elif browser.casefold() == "firefox":
            self.driver = webdriver.Firefox(
                executable_path="/abhibus/drivers/geckodriver")
            # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            print("Firefox Browser Launched")
        self.driver.maximize_window()
        # self.driver.get(url)


    # def parallelBrowserSetup(self):
    #     desired_cap = {
    #         'platform': "Debian GNU/Linux rodete",
    #         'browserName': "chrome",
    #         # [{browserName = safari, version =, platform = MAC}]
    #     }
    #     print("Initiating remote driver on platform: " + desired_cap["platform"] + " browser: " + desired_cap["browserName"])
    #     time.sleep(5)
    #     self.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=desired_cap)
    #     self.driver.maximize_window()

    def launchUrl(self, url):
        self.driver.get(url)
        print("URL Launch Successful")
        time.sleep(3)

    # def thread_parallel_browser(self, url):
    #     # b = Browser()
    #     threads = []
    #     for t in range(2):
    #         thread = threading.Thread(target=Browser().browserSetUp("chrome", url))
    #         threads.append(thread)
    #         thread.start()
    #
    #     for thread in threads:
    #         thread.join()
