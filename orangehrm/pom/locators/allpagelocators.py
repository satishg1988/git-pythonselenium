class AllLocators:
    # All locators from the Orange HRM login page
    username_textbox = "//input[@id='txtUsername']"
    password_textbox = "//input[@id='txtPassword']"
    login_button = "btnLogin"

    # All locators on the Orange HRM landing page
    title = "//h1[text()='Dashboard']"
    welcome_user_link = "//a[contains(text(), 'Welcome')]"
    logout_link = "//a[contains(text(), 'Logout')]"
    header_leave_link = "//a[@id='menu_leave_viewLeaveModule']"
    header_menu_bar = "//ul[@id='mainMenuFirstLevelUnorderedList']//b"

    # All locators on the Leave-->Leave List page
    fromdate_field = "//input[@id='calFromDate']/following-sibling::img"
    todate_field = "//input[@id='calToDate']/following-sibling::img"
    year_leavelist = "//select[@data-handler='selectYear']//option"
    month_leavelist = "//select[@data-handler='selectMonth']//option"
    day_leavelist = "//div[@id='ui-datepicker-div']//tr//a"
    leavestatus_checkbox = "//div[@class='checkbox_group label_first']/label[text()='All']"
    employee_searchbox = "//input[@id='leaveList_txtEmployee_empName']"
    # employee_name = "//div[ @class ='ac_results'] // li[contains(text(), 'Whi')]"
    employee_names = "//div[@class='ac_results']//li"
    subunit_dropdown = "//select[@id='leaveList_cmbSubunit']"
    past_employees_checkbox = "//input[@id='leaveList_cmbWithTerminated']"
    search_button = "//input[@id='btnSearch']"
