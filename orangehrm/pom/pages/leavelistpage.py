import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from orangehrm.pom.locators.allpagelocators import AllLocators
from orangehrm.pom.utilities.allscreenshots import ScreenShots
from orangehrm.pom.utilities.events import Events


class LeaveList(Events):
    def __init__(self, driver):
        self.driver = driver
        # calling all the locators from allpageLocators>>AllLocators
        self.fromdate_field = AllLocators.fromdate_field
        self.year_leavelist = AllLocators.year_leavelist
        self.month_leavelist = AllLocators.month_leavelist
        self.day_leavelist = AllLocators.day_leavelist
        self.todate_field = AllLocators.todate_field
        self.leavestatus_checkbox = AllLocators.leavestatus_checkbox
        self.employee_searchbox = AllLocators.employee_searchbox
        self.employee_names = AllLocators.employee_names
        self.subunit_dropdown = AllLocators.subunit_dropdown
        self.past_employees_checkbox = AllLocators.past_employees_checkbox
        self.search_button = AllLocators.search_button

    def click_fromdate_leavelist(self, req_year, req_month, req_day):
        self.driver.find_element(By.XPATH, self.fromdate_field).click()
        # selecting year in from date
        fromyear = self.driver.find_elements(By.XPATH, self.year_leavelist)
        print("Total Years: " + str(len(fromyear)))
        for year in fromyear:
            if year.text == req_year:
                year.click()
                print(req_year + " month clicked")
                # time.sleep(2)
                break
        else:
            print(req_year + " not found")
            self.driver.find_element(By.XPATH, self.fromdate_field).click()

        # selecting month in from date
        frommonth = self.driver.find_elements(By.XPATH, self.month_leavelist)
        print("Total Months: " + str(len(frommonth)))
        for month in frommonth:
            if req_month.casefold() == month.text.casefold():
                month.click()
                print(req_month + " month clicked")
                break
        else:
            print(req_month + " not found")
            self.driver.find_element(By.XPATH, self.fromdate_field).click()
        # time.sleep(2)

        # click day in from date
        fromday = self.driver.find_elements(By.XPATH, self.day_leavelist)
        print("Total days:" + str(len(fromday)))
        for day in fromday:
            if req_day.casefold() == day.text.casefold():
                day.click()
                print(req_day + " day clicked")
                # Calling screenshots method
                # ss = ScreenShots
                # ss.captureScreenShots(self)
                break
        else:
            print(req_day + " not found")
            self.driver.find_element(By.XPATH, self.fromdate_field).click()
        # time.sleep(2)

    def click_todate_leavelist(self, req_year, req_month, req_day):
        self.driver.find_element(By.XPATH, self.todate_field).click()
        # selecting year in to date
        toyear = self.driver.find_elements(By.XPATH, self.year_leavelist)
        print("Total Years: " + str(len(toyear)))
        for year in toyear:
            if year.text == req_year:
                year.click()
                print(req_year + " year clicked")
                # time.sleep(2)
                break
        else:
            print(req_year + " not found")
            self.driver.find_element(By.XPATH, self.todate_field).click()
        # selecting month in to date
        tomonth = self.driver.find_elements(By.XPATH, self.month_leavelist)
        print("Total Months: " + str(len(tomonth)))
        for month in tomonth:
            if req_month.casefold() == month.text.casefold():
                month.click()
                print(req_month + " month clicked")
                break
        else:
            print(req_month + " not found")
            self.driver.find_element(By.XPATH, self.todate_field).click()
        # time.sleep(2)

        # click day in to date
        today = self.driver.find_elements(By.XPATH, self.day_leavelist)
        print("Total days:" + str(len(today)))
        for day in today:
            if req_day.casefold() == day.text.casefold():
                day.click()
                print(day.text + " day clicked")
                break
        else:
            print(req_day + " not found")
            self.driver.find_element(By.XPATH, self.todate_field).click()
        # time.sleep(2)

    def selectLeaveStatus(self, locator_type="xpath"):
        if not self.driver.find_element(By.XPATH, self.leavestatus_checkbox).is_selected():
            self.clickelement(self.leavestatus_checkbox, locator_type)

    def searchEmployeeName(self, partial_name, req_empname, locator_type="xpath"):
        self.sendkeyselement(partial_name, self.employee_searchbox, locator_type)
        # self.getElementsText(req_empname, self.employee_names, locator_type)
        # self.clickelement(self.employee_names, locator_type)
        element = self.getElements(self.employee_names, locator_type)
        for ele in element:
            ele_text = ele.text
            print("Elements received are: " + ele_text)
            if req_empname == ele_text:
                print("Element present in the list: " + ele_text)
                ele.click()
                break

    def selectSubUnit(self, req_dropdown_value):
        # select_subunit = Select(self.driver.find_element(By.XPATH, self.subunit_dropdown))
        # select_subunit.select_by_visible_text('  Sales')
        self.selectElement(req_dropdown_value, self.subunit_dropdown, locator_type="xpath")

    def selectPastEmployees(self):
        if not self.getelement(self.past_employees_checkbox, locator_type="xpath").is_selected():
            self.clickelement(self.past_employees_checkbox, locator_type="xpath")

    def clickSearch(self):
        self.clickelement(self.search_button, locator_type="xpath")