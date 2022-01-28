class AllLocators:
    # All locators from the Orange HRM login page
    username_textbox = "//input[@id='txtUsername']"
    password_textbox = "//input[@id='txtPassword']"
    login_button = "btnLogin"

    # All locators on the Orange HRM landing page
    title = "//h1[text()='Dashboard']"
    welcome_user_link = "//a[contains(text(), 'Welcome')]"
    logout_link = "//a[contains(text(), 'Logout')]"
    header_menu_options = "//ul[@id='mainMenuFirstLevelUnorderedList']//b"
    sub_menu_options = "//a[@class='firstLevelMenu']//parent::li//ul//a"
    # current_submenu_options = "//li[@class='current main-menu-first-level-list-item']//ul//a[@class='arrow']"
    header_leave_link = "//a[@id='menu_leave_viewLeaveModule']"
    leave_list_link = "//a[text()='Leave List']"
    add_entitlements = "Add Entitlements"
    # //a[@id='menu_leave_viewLeaveModule']/parent::li/ul/li/a[text()='Leave List']

    # All locators on the Leave-->Leave List page
    fromdate_field = "//input[@id='calFromDate']/following-sibling::img"
    todate_field = "//input[@id='calToDate']/following-sibling::img"
    year_leavelist = "//select[@data-handler='selectYear']//option"
    month_leavelist = "//select[@data-handler='selectMonth']//option"
    day_leavelist = "//div[@id='ui-datepicker-div']//tr//a"
    leavestatus_checkbox = "//div[@class='checkbox_group label_first']/label[text()='All']"
    employee_searchbox = "//input[@id='leaveList_txtEmployee_empName']"
    employee_names = "//div[@class='ac_results']//li"
    subunit_dropdown = "//select[@id='leaveList_cmbSubunit']"
    past_employees_checkbox = "//input[@id='leaveList_cmbWithTerminated']"
    search_button = "//input[@id='btnSearch']"
    # past_employees_checkbox = "//label[text()='Include Past Employees']"
