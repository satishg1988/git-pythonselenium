import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from orangehrm.pom.locators.allpagelocators import AllLocators
from orangehrm.pom.utilities.allscreenshots import ScreenShots
from orangehrm.pom.utilities.events import Events
from orangehrm.pom.pages.homepage import HomePage
from orangehrm.pom.pages.menuoptions import MenuOptions


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
        self.add_entitlements = AllLocators.add_entitlements

    def clickApplyLeaveSubMenu(self, req_head_menu, req_sub_menu):
        driver = self.driver
        # hp = HomePage(driver)
        # hp.clickSubMenuOptions(req_sub_menu)
        mo = MenuOptions(driver)
        mo.moveToHeaderMenuOptions(req_head_menu)
        mo.clickSubMenuOptions(req_sub_menu)

    def clickAddEntitlementsSubMenu(self, req_head_menu, req_sub_menu1, req_sub_menu2):
        driver = self.driver
        mo = MenuOptions(driver)
        mo.moveToHeaderMenuOptions(req_head_menu)
        mo.moveToSubMenuOptions(req_sub_menu1)
        mo.clickSubMenuOptions(req_sub_menu2)
        # self.clickelement(self.add_entitlements, locator_type="linktext")

    def clickLeaveListSubMenu(self, req_head_menu, req_sub_menu):
        driver = self.driver
        # hp = HomePage(driver)
        # hp.clickSubMenuOptions(req_sub_menu)
        mo = MenuOptions(driver)
        mo.moveToHeaderMenuOptions(req_head_menu)
        mo.clickSubMenuOptions(req_sub_menu)

    def selectFromYear(self, req_year):
        self.clickelement(self.fromdate_field, locator_type="xpath")
        # selecting year in from date
        fromyear = self.getElements(self.year_leavelist, locator_type="xpath")
        print("Total Years: " + str(len(fromyear)))
        for year in fromyear:
            if year.text == req_year:
                year.click()
                print(req_year + " month clicked")
                # time.sleep(2)
                break
        else:
            print(req_year + " not found")
            self.clickelement(self.fromdate_field, locator_type="xpath")

        # selecting month in from date
    def selectFromMonth(self, req_month):
        frommonth = self.getElements(self.month_leavelist, locator_type="xpath")
        print("Total Months: " + str(len(frommonth)))
        for month in frommonth:
            if req_month.casefold() == month.text.casefold():
                month.click()
                print(req_month + " month clicked")
                # time.sleep(2)
                break
        else:
            print(req_month + " not found")
            self.clickelement(self.fromdate_field, locator_type="xpath")

        # click day in from date
    def selectFromDay(self, req_day):
        fromday = self.getElements(self.day_leavelist, locator_type="xpath")
        print("Total days:" + str(len(fromday)))
        for day in fromday:
            if req_day.casefold() == day.text.casefold():
                day.click()
                print(req_day + " day clicked")
                # Calling screenshots method
                # ss = ScreenShots
                # ss.captureScreenShots(self)
                # time.sleep(2)
                break
        else:
            print(req_day + " not found")
            # self.driver.find_element(By.XPATH, self.fromdate_field).click()
            self.clickelement(self.fromdate_field, locator_type="xpath")
        # time.sleep(2)

    def selectToYear(self, req_year):
        self.clickelement(self.todate_field, locator_type="xpath")
        # selecting year in from date
        to_year = self.getElements(self.year_leavelist, locator_type="xpath")
        print("Total Years: " + str(len(to_year)))
        for year in to_year:
            if year.text == req_year:
                year.click()
                print(req_year + " month clicked")
                time.sleep(2)
                break
        else:
            print(req_year + " not found")
            self.clickelement(self.todate_field, locator_type="xpath")

        # selecting month in from date
    def selectToMonth(self, req_month):
        frommonth = self.getElements(self.month_leavelist, locator_type="xpath")
        print("Total Months: " + str(len(frommonth)))
        for month in frommonth:
            if req_month.casefold() == month.text.casefold():
                month.click()
                print(req_month + " month clicked")
                time.sleep(2)
                break
        else:
            print(req_month + " not found")
            self.clickelement(self.todate_field, locator_type="xpath")

        # click day in from date
    def selectToDay(self, req_day):
        fromday = self.getElements(self.day_leavelist, locator_type="xpath")
        print("Total days:" + str(len(fromday)))
        for day in fromday:
            if req_day.casefold() == day.text.casefold():
                day.click()
                print(req_day + " day clicked")
                # Calling screenshots method
                # ss = ScreenShots
                # ss.captureScreenShots(self)
                time.sleep(2)
                break
        else:
            print(req_day + " not found")
            # self.driver.find_element(By.XPATH, self.fromdate_field).click()
            self.clickelement(self.todate_field, locator_type="xpath")
        # time.sleep(2)

    # def click_todate_leavelist(self, req_year, req_month, req_day):
    #     self.driver.find_element(By.XPATH, self.todate_field).click()
    #     # selecting year in to date
    #     toyear = self.driver.find_elements(By.XPATH, self.year_leavelist)
    #     print("Total Years: " + str(len(toyear)))
    #     for year in toyear:
    #         if year.text == req_year:
    #             year.click()
    #             print(req_year + " year clicked")
    #             # time.sleep(2)
    #             break
    #     else:
    #         print(req_year + " not found")
    #         self.driver.find_element(By.XPATH, self.todate_field).click()
    #     # selecting month in to date
    #     tomonth = self.driver.find_elements(By.XPATH, self.month_leavelist)
    #     print("Total Months: " + str(len(tomonth)))
    #     for month in tomonth:
    #         if req_month.casefold() == month.text.casefold():
    #             month.click()
    #             print(req_month + " month clicked")
    #             break
    #     else:
    #         print(req_month + " not found")
    #         self.driver.find_element(By.XPATH, self.todate_field).click()
    #     # time.sleep(2)
    #
    #     # click day in to date
    #     today = self.driver.find_elements(By.XPATH, self.day_leavelist)
    #     print("Total days:" + str(len(today)))
    #     for day in today:
    #         if req_day.casefold() == day.text.casefold():
    #             day.click()
    #             print(day.text + " day clicked")
    #             break
    #     else:
    #         print(req_day + " not found")
    #         self.driver.find_element(By.XPATH, self.todate_field).click()
    #     # time.sleep(2)

    def selectFromDateLeaveList(self, req_year, req_month, req_day):
        driver = self.driver
        llp = LeaveList(driver)
        llp.selectFromYear(req_year)
        llp.selectFromMonth(req_month)
        llp.selectFromDay(req_day)
        print("Inner text is: " + str(self.driver.find_element(By.XPATH, "//input[@id='calFromDate']").get_attribute("value")))

    def selectToDateLeaveList(self, req_year, req_month, req_day):
        driver = self.driver
        llp = LeaveList(driver)
        llp.selectToYear(req_year)
        llp.selectToMonth(req_month)
        llp.selectToDay(req_day)

    def selectLeaveStatus(self):
        if not self.getelement(self.leavestatus_checkbox, locator_type="xpath").is_selected():
            self.clickelement(self.leavestatus_checkbox, locator_type="xpath")

    def searchEmployeeName(self, partial_name, req_empname):
        self.sendkeyselement(partial_name, self.employee_searchbox, locator_type="xpath")
        # self.getElementsText(req_empname, self.employee_names, locator_type)
        # self.clickelement(self.employee_names, locator_type)
        element = self.getElements(self.employee_names, locator_type="xpath")
        for ele in element:
            ele_text = ele.text
            print("Elements received are: " + ele_text)
            if req_empname == ele_text:
                print("Employee name present in the list: " + ele_text)
                ele.click()
                break
            else:
                print("Employee name is not present in the list: " + ele_text)

    def selectSubUnit(self, req_dropdown_value):
        # select_subunit = Select(self.driver.find_element(By.XPATH, self.subunit_dropdown))
        # select_subunit.select_by_visible_text('  Sales')
        self.selectElementByVisibleText(req_dropdown_value, self.subunit_dropdown, locator_type="xpath")

    def selectPastEmployees(self):
        if not self.getelement(self.past_employees_checkbox, locator_type="xpath").is_selected():
            self.clickelement(self.past_employees_checkbox, locator_type="xpath")

    def clickSearch(self):
        self.clickelement(self.search_button, locator_type="xpath")