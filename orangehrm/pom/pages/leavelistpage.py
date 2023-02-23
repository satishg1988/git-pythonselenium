import time

from selenium.common import exceptions
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from orangehrm.pom.locators.allpagelocators import AllLocators
from orangehrm.pom.pages.menuoptions import MenuOptions
from orangehrm.pom.utilities.events import Events


class LeaveList(Events):
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

        # calling all the locators from allpageLocators>>AllLocators
        self.fromdate_field = AllLocators.fromdate_field
        self.fromyear_field = AllLocators.fromyear_field
        self.frommonths_field = AllLocators.frommonths_field
        self.fromdate_placeholder = AllLocators.fromdate_placeholder

        self.todate_field = AllLocators.todate_field
        self.toyears_field = AllLocators.toyears_field
        self.tomonths_field = AllLocators.tomonths_field
        self.todate_placeholder = AllLocators.todate_placeholder

        self.year_leavelist = AllLocators.year_leavelist
        self.month_leavelist = AllLocators.month_leavelist
        self.day_leavelist = AllLocators.day_leavelist

        self.leavestatus_dropdown = AllLocators.leavestatus_dropdown
        self.leavestatus_dropdown_list = AllLocators.leavestatus_dropdown_list
        self.leavestatus_chips_close = AllLocators.leavestatus_chips_close

        self.leavetype_dropdown = AllLocators.leavetype_dropdown
        self.leavetype_dropdown_list = AllLocators.leavetype_dropdown_list

        # self.leavestatus_checkbox = AllLocators.leavestatus_checkbox
        self.employee_autosearchbox = AllLocators.employee_autosearchbox
        self.employee_names_list = AllLocators.employee_names_list

        # self.employee_names = AllLocators.employee_names
        self.subunit_dropdown = AllLocators.subunit_dropdown
        self.subunit_dropdown_list = AllLocators.subunit_dropdown_list
        self.pastemployees_toggle = AllLocators.pastemployees_toggle
        self.search_button = AllLocators.search_button
        self.add_entitlements = AllLocators.add_entitlements
        self.noof_records_count = AllLocators.noof_records_count
        self.noof_records_found_text = AllLocators.noof_records_found_text
        self.info_alert_closebutton = AllLocators.info_alert_closebutton
        self.approve_button = AllLocators.approve_button
        self.reject_button = AllLocators.reject_button

    def clickApplyLeaveSubMenu(self, req_leftpanel_option, req_rightpanel_menu):
        driver = self.driver
        # hp = HomePage(driver)
        # hp.clickSubMenuOptions(req_sub_menu)
        mo = MenuOptions(driver)
        mo.clickLeftPaneOptions(req_leftpanel_option)
        mo.clickRightPanelMenuOptions(req_rightpanel_menu)
        # mo.clickSubMenuOptions(req_sub_menu)

    def clickAddEntitlementsSubMenu(self, req_leftpanel_option, req_rightpanel_menu1, req_rightpanel_menu2):
        driver = self.driver
        mo = MenuOptions(driver)
        mo.clickLeftPaneOptions(req_leftpanel_option)
        mo.clickRightPanelMenuOptions(req_rightpanel_menu1)
        mo.clickRightPanelMenuOptions(req_rightpanel_menu2)
        # mo.clickSubMenuOptions(req_rightpanel_menu2)
        # self.clickelement(self.add_entitlements, locator_type="linktext")

    def clickLeaveListSubMenu(self, req_leftpanel_option, req_rightpanel_menu1):
        driver = self.driver
        # hp = HomePage(driver)
        # hp.clickSubMenuOptions(req_sub_menu)
        mo = MenuOptions(driver)
        mo.clickLeftPaneOptions(req_leftpanel_option)
        mo.clickRightPanelMenuOptions(req_rightpanel_menu1)

        # mo.moveToHeaderMenuOptions(req_head_menu)
        # mo.clickSubMenuOptions(req_sub_menu)

    def selectFromYear(self, req_year, locator_type="xpath"):
        self.clickelement(self.fromdate_field, locator_type)
        time.sleep(5)
        # selecting year in from date
        # from_year = self.getelement(self.fromyear_field, locator_type)
        # self.action.move_to_element(from_year).click().perform()
        # self.waitelement(self.fromyear_field, locator_type)
        self.clickelement(self.fromyear_field, locator_type)
        time.sleep(5)
        self.waitForPresenceOfAllElements(self.fromyear_field, locator_type)
        fromyear = self.getElements(self.year_leavelist, locator_type)
        print("Total Years: " + str(len(fromyear)))
        for year in fromyear:
            if year.text.casefold() == req_year.casefold():
                # year_wait = self.waitelement(year, locator_type)
                # year_wait.click()
                self.action.move_to_element(year).click().perform()
                print(req_year + " month clicked")
                # time.sleep(2)
                break
            else:
                print(req_year + " not found")
                self.clickelement(self.fromdate_field, locator_type)

        # selecting month in from date
    def selectFromMonth(self, req_month, locator_type="xpath"):
        self.clickelement(self.frommonths_field, locator_type)
        time.sleep(2)
        frommonth = self.getElements(self.month_leavelist, locator_type)
        print("Total Months: " + str(len(frommonth)))
        for month in frommonth:
            if req_month.casefold() == month.text.casefold():
                self.action.move_to_element(month).click().perform()
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
                self.action.move_to_element(day).click().perform()
                # day.click()
                print(req_day + " day clicked")
                time.sleep(2)
                break
        else:
            print(req_day + " not found")
            # self.driver.find_element(By.XPATH, self.fromdate_field).click()
            self.clickelement(self.fromdate_field, locator_type="xpath")
        # time.sleep(2)

    def selectToYear(self, req_year, locator_type="xpath"):
        # selecting year in to date
        todate = self.getelement(self.todate_field, locator_type)
        self.action.move_to_element(todate).click().perform()
        # self.clickelement(self.todate_field, locator_type)
        self.clickelement(self.toyears_field, locator_type)
        to_year = self.getElements(self.year_leavelist, locator_type)
        print("Total Years: " + str(len(to_year)))
        for year in to_year:
            if year.text == req_year:
                self.action.move_to_element(year).click().perform()
                print(req_year + " month clicked")
                time.sleep(2)
                break
        else:
            print(req_year + " not found")
            self.clickelement(self.todate_field, locator_type="xpath")

        # selecting month in from date
    def selectToMonth(self, req_month, locator_type="xpath"):
        self.clickelement(self.tomonths_field, locator_type)
        frommonth = self.getElements(self.month_leavelist, locator_type)
        print("Total Months: " + str(len(frommonth)))
        for month in frommonth:
            if req_month.lower() == month.text.lower():
                self.action.move_to_element(month).click().perform()
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

    def selectFromDateLeaveList(self, req_year, req_month, req_day, locator_type="xpath"):
        driver = self.driver
        llp = LeaveList(driver)
        llp.selectFromYear(req_year)
        llp.selectFromMonth(req_month)
        llp.selectFromDay(req_day)
        fromdate_inner_text = self.getelement(self.fromdate_placeholder, locator_type)
        print("The selected from date is: " + fromdate_inner_text.get_attribute("value"))

    def selectToDateLeaveList(self, req_year, req_month, req_day, locator_type="xpath"):
        driver = self.driver
        llp = LeaveList(driver)
        llp.selectToYear(req_year)
        llp.selectToMonth(req_month)
        llp.selectToDay(req_day)
        todate_inner_text = self.getelement(self.todate_placeholder, locator_type)
        print("The selected to date is: " + todate_inner_text.get_attribute("value"))

    def selectLeaveStatus(self, req_leavestatus, locator_type="xpath"):
        leave_status_chips = self.getElements(self.leavestatus_chips_close, locator_type)
        if leave_status_chips != "null":
            for leave_chip in leave_status_chips:
                self.action.move_to_element(leave_chip).click().perform()
                # leave_chip.click()
        leave_status = self.getelement(self.leavestatus_dropdown, locator_type)
        self.action.move_to_element(leave_status).click().perform()
        leave_statuses = self.getElements(self.leavestatus_dropdown_list, locator_type)
        print("Total Leave Statuses Are: " + str(len(leave_statuses)))
        for status in leave_statuses:
            print("Leave Statuses Are: " + status.text)
            if req_leavestatus.casefold() == status.text.casefold():
                status.click()
                print(req_leavestatus + " : dropdown option was selected")
                break
            else:
                print(req_leavestatus+" : Not Available In The Dropdown")

    def selectLeaveType(self, req_leave_type, locator_type="xpath"):
        self.clickelement(self.leavetype_dropdown, locator_type)
        leave_types = self.getElements(self.leavetype_dropdown_list, locator_type)
        print("Total Leave Types Are: " + str(len(leave_types)))
        for leave_type in leave_types:
            print("Leave Types Are: "+leave_type.text)
            if req_leave_type.casefold() == leave_type.text.casefold():
                leave_type.click()
                print(req_leave_type + ": Leave Type Option Was Selected")
                break
            else:
                print(req_leave_type + ": Leave Type Option Not Selected")

    def searchEmployeeName(self, partial_name, req_empname, locator_type="xpath"):
        emp_auto_search = self.getelement(self.employee_autosearchbox, locator_type)
        self.action.move_to_element(emp_auto_search).click().perform()
        # self.clickelement(self.employee_autosearchbox, locator_type)
        self.sendkeyselement(partial_name, self.employee_autosearchbox, locator_type)
        time.sleep(2)
        emp_names = self.getElements(self.employee_names_list, locator_type)
        print("Total Employees Are: " + str(len(emp_names)))
        for emp_name in emp_names:
            print("Elements received are: " + emp_name.text)
            if req_empname.casefold() == emp_name.text.casefold():
                emp_name.click()
                print(req_empname + " : Employee Was Selected")
                break
            else:
                print(req_empname + " : Employee name is not present in the list")

    def selectSubUnit(self, req_subunit, locator_type="xpath"):
        self.clickelement(self.subunit_dropdown, locator_type)
        sub_units = self.getElements(self.subunit_dropdown_list, locator_type)
        for sub_unit in sub_units:
            print("Sub Units Received Are:" + sub_unit.text)
            if req_subunit.casefold() == sub_unit.text.casefold():
                sub_unit.click()
                print("The " + req_subunit + ": Option Was Selected")
                break
            else:
                print("The " + req_subunit + ": Option Was Not Selected")
        # self.selectElementByVisibleText(req_dropdown_value, self.subunit_dropdown, locator_type="xpath")

    def selectPastEmployees(self, locator_type="xpath"):
        if not self.getelement(self.pastemployees_toggle, locator_type="xpath").is_selected():
            print("The Past Employees Toggle Is OFF")
            pastemp_toggle = self.getelement(self.pastemployees_toggle, locator_type)
            self.action.move_to_element(pastemp_toggle).click().perform()

    def clickSearch(self, locator_type="xpath"):
        self.clickelement(self.search_button, locator_type)
        time.sleep(2)

    def getRecordsCount(self, locator_type="xpath"):
        records_found = self.getElements(self.noof_records_count, locator_type)
        total_records = len(records_found)
        print("Total No Of Records Found Are: " + str(total_records))
        time.sleep(3)

    def getRecordsFoundText(self, locator_type="xpath"):
        # alert_close_button = self.getelement(self.info_alert_closebutton, locator_type)
        # action = ActionChains(self.driver)
        # action.move_to_element(alert_close_button).click().perform()
        records_found_text = self.getElementText(self.noof_records_found_text, locator_type)
        print("Text Is: " + records_found_text)

    def clickApproveActionButton(self, locator_type="xpath"):
        approve_buttons = self.getElements(self.approve_button, locator_type)
        print("Total Approve Buttons: " + str(len(approve_buttons)))

        for approve_button in approve_buttons:
            try:
                # ele = self.wait.until(EC.presence_of_element_located(self.bytype(locator_type)))
                self.clickSearch(locator_type)
                self.waitelement(self.approve_button, locator_type)
                # approve_button.click()
                self.action.move_to_element(approve_button).click().perform()

                # self.driver.refresh()
                # time.sleep(10)
            except exceptions.StaleElementReferenceException as e:
                print(e)


