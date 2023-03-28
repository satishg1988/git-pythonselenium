class AllLocators:
    # All locators from the AbhiBus login page
    login_or_register_link = "//span[@id='AccLogin']"
    close_icon = "//div[@class='close']"
    mobile_num_textbox = "//input[@id='mobileNo']"
    login_signup_otp_button = "//input[@value='Login/Signup with OTP']"
    login_with_google_button = "//a[@id='customBtn']//span[text() = 'Google ']"
    otp_request_message = "//input[@id='mobileNo']//parent::div//div[@class='errortxt']"
    otp_sent_success_message = "//div[@class='formData']//form//div[@id='Succ-Otpmsg']"
    error_msg_mobile_empty = "//input[@id='mobileNo']//..//div"
    error_msg_mobile_invalid = "//input[@id='mobileNo']//..//div"
    get_first_ride_free_checkbox = "//span[text()='Get First Ride FREE ']//..//input[@id='chk_refer_code']"

    # All locators from the Home Page
    bus_link = "pills-home-tab"
    trains_link = "pills-profile-tab"
    hotels_link = "pills-contact-tab"
    rentals_link = "pills-rental-tab"
    leaving_from_textbox = "//label[text()='Leaving from']//..//input[@id='source']"
    source_cities_list = "//ul[@id='ui-id-1']//li"
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
    select_seat_xpath_part_one = "//div[@class='search-column1']//h2[@title='"
    select_seat_xpath_part_two = "']//..//p[@title='"
    select_seat_xpath_part_three = "']//..//..//..//div[@class='col3 booksts clearfix']//span[@class='book']"
    seats_list = "//a[contains(@href, 'OU6')]"
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
    offers_header_option = "//ul[@class='navbar-nav ml-auto']//a[contains(text(), 'Offers')]"
    bus_bookings_offer_heading = "//div[@class='container']//..//h1"

    # All locators from the Get Free Rides Page
    get_free_rides_header_option = "//ul[@class='navbar-nav ml-auto']//a[contains(text(), 'Get Free Rides')]"
