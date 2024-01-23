import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from abhibus.pom.utilities.data import Data


@pytest.fixture(scope="class")
def setUp():
    # global driver
    browser = "chrome"
    if browser.casefold() == "chrome":
        # self.driver = webdriver.Chrome("/usr/local/google/home/sateeshg/git-pythonselenium/abhibus/drivers/chromedriver119")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver = webdriver.Chrome()
        print("Chrome Browser Launched")
    elif browser.casefold() == "firefox":
        # driver = webdriver.Firefox(executable_path="/abhibus/drivers/geckodriver")
        driver = webdriver.Firefox(service=GeckoDriverManager().install())
        print("Firefox Browser Launched")

    driver.maximize_window()
    driver.get(Data.url)
    print("URL Launch Successful")
    yield driver
    time.sleep(3)
