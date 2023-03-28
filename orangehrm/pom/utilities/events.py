from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class Events:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def bytype(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "tagname":
            return By.TAG_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locator_type + " is not valid")

    def getelement(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            bytype = self.bytype(locator_type)
            element = self.driver.find_element(bytype, locator)
            print("Element found")
        except:
            print("Element not found")
        return element

    def getElements(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            bytype = self.bytype(locator_type)
            element = self.driver.find_elements(bytype, locator)
            print("Total Elements: " + str(len(element)))
            print("Elements found are: " + str(locator))
        except:
            print("Elements not found")
        return element

    def clickelement(self, locator, locator_type="id"):
        element = None
        try:
            element = self.getelement(locator, locator_type)
            element.click()
            print("Clicked the element: " + locator)
        except:
            print("Not able to click the element: " + locator)
        return element

    def clearelement(self, locator, locator_type="id"):
        element = None
        try:
            element = self.getelement(locator, locator_type)
            element.clear()
            print("Cleared the element " + locator)
        except:
            print("Not able to clear the element: " + locator)
        return element

    def sendkeyselement(self, reqdata, locator, locator_type="id"):
        try:
            element = self.getelement(locator, locator_type)
            element.send_keys(reqdata)
            print("Enter data to the element " + locator)
        except:
            print(locator + " Not clickable")
        return element

    def getElementText(self, locator, locator_type="id"):
        element = self.getelement(locator, locator_type)
        text_received = element.text
        print("Text received is : " + text_received)
        return text_received

    # def getElementsText(self, locator, locator_type="id"):
    #     ele_text = None
    #     element = self.getElements(locator, locator_type)
    #     for ele in element:
    #         ele_text = ele.text
    #     return ele_text

    def selectElementByVisibleText(self, req_dropdown_value, locator, locator_type="id"):
        select_element = Select(self.getelement(locator, locator_type))
        select_element.select_by_visible_text(req_dropdown_value)

    def selectElementsByVisibleText(self, req_dropdown_value, locator, locator_type="id"):
        select_element = Select(self.getElements(locator, locator_type))
        select_element.select_by_visible_text(req_dropdown_value)

    def isElementDisplayed(self, locator, locator_type="id"):
        element_displayed = None
        try:
            element = self.getelement(locator, locator_type)
            element_displayed = element.is_displayed()
        except:
            print("Element display failed")
        return element_displayed

    def getTitle(self):
        return self.driver.title

    def textContains(self, actual_text, expected_text):
        if actual_text.casefold() in expected_text.casefold():
            print("Verification Pass")
            return True
        else:
            print("verification Failed")
            return False

    def waitElementToBeClickable(self, wait_time, locator, locator_type="id"):
        element = None
        try:
            by_type = self.bytype(locator_type)
            wait = WebDriverWait(self.driver, wait_time, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            print("From waitelement: Element found")
        except:
            print("From waitelement: Element not found")
        return element

    def waitForPresenceOfElement(self, wait_time, locator, locator_type="id"):
        element = None
        try:
            by_type = self.bytype(locator_type)
            wait = WebDriverWait(self.driver, wait_time, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(EC.presence_of_element_located((by_type, locator)))
            print("From waitelement: Element found")
        except:
            print("From waitelement: Element not found")
        return element

    def isElementSelected(self, locator, locator_type="id"):
        element = self.getelement(locator, locator_type)
        element_selected = element.is_selected()
        return element_selected
