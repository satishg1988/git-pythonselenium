class AllLocators:
    # All locators from the AbhiBus login page
    login_or_register_link = "//a[@id='login-link']//span[text() = 'Login/SignUp']"
    login_button = "//button[@class='btn btn-login filled primary md inactive button']"
    close_icon = "//div[@class='close']"
    mobile_num_textbox = "//input[@class='true mobileNo-input']"
    login_signup_otp_button = "//div[@id='login-validation']"
    login_with_google_button = "//a[@id='login-google-link']//span[text() = 'Sign in with google']"
    otp_request_message = "//div[@id='login-otp']//p"
    otp_sent_success_message = "//div[@class='formData']//form//div[@id='Succ-Otpmsg']"
    error_msg_mobile_empty = "//input[@id='mobileNo']//..//div"
    error_msg_mobile_invalid = "//input[@id='mobileNo']//..//div"
    get_first_ride_free_checkbox = "//span[text()='Get First Ride FREE ']//..//input[@id='chk_refer_code']"

    # All locators from the Home Page
    bus_link = "pills-home-tab"
    trains_link = "pills-profile-tab"
    hotels_link = "pills-contact-tab"
    rentals_link = "pills-rental-tab"
    leaving_from_textbox = "//input[@placeholder='From Station']"
    source_cities_list = "//div[@id='search-from']//ul//li//div[@class=' col']"
    going_to_textbox = "//label[text()='Going to']//..//input[@id='destination']"
    destination_cities_list = "//ul[@id='ui-id-2']//li"
    date_of_journey_field = "//label[text()='Date of Journey']//..//input[@id='datepicker1']"
    # day_field = "//div[@class='ui-datepicker-title']//span[text()='"
    # day_field_xpath = "']//..//..//..//table//a"
    # months_list = "//div[@class='ui-datepicker-title']"
    # years_list = "//span[@class='ui-datepicker-year']"

    month_group_pre_xpath = "//div[@class='ui-datepicker-group ui-datepicker-group-"
    month_group_post_xpath = "']//span[@class='ui-datepicker-month']"
    year_group_pre_xpath = "//div[@class='ui-datepicker-group ui-datepicker-group-"
    year_group_post_xpath = "']//span[@class='ui-datepicker-year']"
    days_group_pre_xpath = "//div[@class='ui-datepicker-group ui-datepicker-group-"
    days_group_post_xpath = "']//table[@class='ui-datepicker-calendar']//td"

    previous_icon = "//a[@title='Prev']"
    next_icon = "//a[@title='Next']"
    search_button = "Search"
    selectseat_button_xpath_part_one = "//div[@class='search-column1']//h2[@title='"
    selectseat_button_xpath_part_two = "']//..//p[@title='"
    selectseat_button_xpath_part_three = "']//..//..//..//div[@class ='col1 column-left bustrack-icon']//h2//span[contains(text(), '"
    selectseat_button_xpath_part_four = "')]//..//..//..//div[@class ='col3 booksts clearfix']//span[@ class ='book']"
    # //div[@class ='search-column1']//h2[@title='']//..//p[@title='NON-AC Sleeper (2 + 1)']//..//..//..//div[@class ='col1 column-left bustrack-icon']//h2//span[contains(text(),'23:25')]//..//..//..//div[@class ='col3 booksts clearfix']//span[@ class ='book']

    seat_button_xpath_part_one = "//a[contains(@href, '"
    seat_button_xpath_part_two = "')]"
    # //div[@class ='search-column1']//h2[@title='Dharani Tours and Travels']//..//p[@title='NON-AC Sleeper (2 + 1)']//..//..//..//div[@class ='col1 column-left bustrack-icon']//h2//span[contains(text(),'23:25')]//..//..//..//select[@id="boardingpoint_id"]
    boardingpoint_dropdown_xpath_part_one = "//div[@class ='search-column1']//h2[@title='"
    boardingpoint_dropdown_xpath_part_two = "']//..//p[@title='"
    boardingpoint_dropdown_xpath_part_three = "']//..//..//..//div[@class ='col1 column-left bustrack-icon']//h2//span[contains(text(),'"
    boardingpoint_dropdown_xpath_part_four = "')]//..//..//..//select[@id='boardingpoint_id']"

    droppingpoint_dropdown_xpath_part_one = "//div[@class ='search-column1']//h2[@title='"
    droppingpoint_dropdown_xpath_part_two = "']//..//p[@title='"
    droppingpoint_dropdown_xpath_part_three = "']//..//..//..//div[@class ='col1 column-left bustrack-icon']//h2//span[contains(text(),'"
    droppingpoint_dropdown_xpath_part_four = "')]//..//..//..//select[@id='droppingpoint_id']"

    continuetopayment_button_xpath_part_one = "//div[@class ='search-column1']//h2[@title='"
    continuetopayment_button_xpath_part_two = "']//..//p[@title='"
    continuetopayment_button_xpath_part_three = "']//..//..//..//div[@class ='col1 column-left bustrack-icon']//h2//span[contains(text(),'"
    continuetopayment_button_xpath_part_four = "')]//..//..//..//input[@id='btnEnable1' and @value='Continue to Payment ']"

    # boardingpoint_dropdown = "//form[@id='frmSeat1483023986']//select[@id='boardingpoint_id']"
    boardingpoint_dropdown_list = "//form[@id='frmSeat1483023986']//select[@id='boardingpoint_id']//option"
    # //div[@class ='search-column1']//h2[@title='Dharani Tours and Travels']//..//p[@title='NON-AC Sleeper (2 + 1)']//..//..//..//div[@class ='col1 column-left bustrack-icon']//h2//span[contains(text(),'23:25')]//..//..//..//select[@id='droppingpoint_id']
    # //div[@class ='search-column1']//h2[@title='Dharani Tours and Travels']//..//p[@title='NON-AC Sleeper (2 + 1)']//..//..//..//div[@class ='col1 column-left bustrack-icon']//h2//span[contains(text(),'23:25')]//..//..//..//input[@id='btnEnable1' and @value='Continue to Payment ']
    # droppingpoint_dropdown = "//form[@id='frmSeat1450508119']//select[@id='droppingpoint_id']"
    droppingpoint_dropdown_list = "//form[@id='frmSeat1450508119']//select[@id='droppingpoint_id']//option"
    # continue_to_payment_button = "//form[@id='frmSeat1450508119']//input[@id='btnEnable1' and @value='Continue to Payment ']"
    # "//div[@class='borderdtd']//li//a"

    expand_icon_tsrtc = "ShowBtnHide11"
    # bus_partners_list = "//div[@class='search-column1']//h2"
    # bus_partners_type_list = "//div[ @class ='search-column1']//h2//..//p"
    # select_seat_button = "//a[@class='btn-seatselect book1']"
    show_icon = "span.ShowBtnHide1"
    hide_icon = "span.ShowBtnHide2"

    # All locator from the "Filters" - left panel
    price_drop_checkbox = "//span[contains(text(), 'Price Drop')]//..//input[@type='checkbox']"
    bus_type_filters = "//div[@class='f-bustype-sec']//li"
    clearall_bustype = "//div[ @class ='f-bus-type']//small"
    expand_collapse_bus_partner = "//parent::span[contains(text(), 'Bus Partner')]"
    bus_partner_searchbox = "//div[@class='f-operator-type']//div[@class='f-operator-checkbox2']//input[@placeholder='Search for Bus Partner']"
    bus_partners_list = "//div[@class='f-operator-type']//div[@class='f-operator-checkbox filter-list']//li//label"
    boarding_point_expand_collapse = "//span[contains(text(), 'Boarding Point')]"
    boarding_point_searchbox = "//input[@placeholder='Search for Boarding Point']"
    boarding_points_list = "//div[@class='f-boarding-point']//div[@class='f-b-p-search filter-list']//li//label"
    dropping_point_expand_collapse = "//span[contains(text(), 'Dropping Point')]"
    dropping_point_searchbox = "//input[@placeholder='Search for Dropping Point']"
    dropping_points_list = "//div[@class='f-dropping-point']//div[@class='f-d-p-search filter-list']//li//label"
    depature_time_filters = "//div[@class='f-depature-sec']//li"


    # All locators from the My Bookings Page
    my_bookings_header_option = "//a[contains(text(), 'My Bookings')]"
    print_booking_header_option = "//a[contains(text(), 'Print Booking')]"
    cancel_booking_header_option = "//a[contains(text(), 'Cancel Booking')]"

    # All locators from the Offers Page
    offers_header_option = "//nav[@id='header-right-nav']//span[text()='Offers']"
    bus_bookings_offer_heading = "//div[@id='offer-cards-tab-container']//h1"
    offercards_title = "//div[@id='offer-cards-tab-content']//div[@class='container card   sm ']//h3"
    offercards_viewdetails_btn_one = "//div[@id='offer-cards-tab-content']//div[@class='container card   sm ']//h3[text()='"
    offercards_viewdetails_btn_two = "']//../..//a"
    copy_code_btn = "//button[contains(text(), 'Copy Code')]"
    code_copied_msg = "//div[@class='row text-success']"

    #All locators from the Track Tickets Page
    track_ticket_option = "//nav[@id='header-right-nav']//span[text()='Track Ticket']"
    track_ticket_heading = "//div[@id='pre-cancellation-container']//h5"
    ticket_details_button = "//div[@id='pre-cancellation-retrive']//a[text()='Ticket Details']"
    errormsg_bookingid_empty = "//div[@class='container text-input  ']//span"
    errormsg_mobilenumber_empty = "//div[@class='container number-input mobileNo-input ']//span[@class='error']"


    # All locators from the Get Free Rides Page
    get_free_rides_header_option = "//ul[@class='navbar-nav ml-auto']//a[contains(text(), 'Get Free Rides')]"
