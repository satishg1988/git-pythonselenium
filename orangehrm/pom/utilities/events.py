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
        try:
            element = self.getelement(locator, locator_type)
            element.click()
            print("Clicked the element: " + locator)
        except:
            print("Not able to click the element: " + locator)
        return element

    def clearelement(self, locator, locator_type="id"):
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
        print("Element displayed: " + text_received)
        return text_received

    # def getElementsText(self, req_empname, locator, locator_type="id"):
    #     element = self.getElements(locator, locator_type)
    #     for ele in element:
    #         ele_text = ele.text
    #         print("Elements received are: " + ele_text)
    #         if req_empname == ele_text:
    #             print("Element present in the list: " + ele_text)
    #             # ele.click()
    #             break
    #     return element

    def selectElementByVisibleText(self, req_dropdown_value, locator, locator_type="id"):
        select_subunit = Select(self.getelement(locator, locator_type))
        select_subunit.select_by_visible_text(req_dropdown_value)

    def getTitle(self):
        return self.driver.title

    def verifyTextContains(self, actual_text, expected_text):
        if actual_text.casefold() in expected_text.casefold():
            print("Verification Pass")
            return True
        else:
            return False
            print("verification Failed")

    # def waitelement(self, locator, locator_type="id"):
    #     element = None
    #     try:
    #         bytype = self.bytype(locator_type)
    #         wait = WebDriverWait(self.driver, 20, poll_frequency=1,
    #                              ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
    #                                                  ElementNotSelectableException])
    #         element = wait.until(EC.element_to_be_clickable(bytype))
    #         print("From waitelement: Element found")
    #     except:
    #         print("From waitelement: Element not found")
    #     return element
