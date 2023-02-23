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
    days_group_post_xpath = "']//table[@class='ui-datepicker-calendar']//td//a"

    previous_icon = "//a[@title='Prev']"
    next_icon = "//a[@title='Next']"
    search_button = "Search"
    select_seat_xpath_part_one = "//div[@class='search-column1']//h2[@title='"
    select_seat_xpath_part_two = "']//..//p[@title='"
    select_seat_xpath_part_three = "']//..//..//..//div[@class='col3 booksts clearfix']//span[@class='book']"
    expand_icon = "ShowBtnHide11"
    bus_partners_list = "//div[@class='search-column1']//h2"
    bus_partners_type_list = "//div[ @class ='search-column1']//h2//..//p"
    select_seat_button = "//a[@class='btn-seatselect book1']"

    # //div[ @class ="search-column1"] // h2[@ title="Orange Tours and Travels"] //..// p[@ title="VOLVO AC Multi Axle Sleeper (2 + 1)"]

    # All locators from the My Bookings Page
    my_bookings_header_option = "//a[contains(text(), 'My Bookings')]"
    print_booking_header_option = "//a[contains(text(), 'Print Booking')]"
    cancel_booking_header_option = "//a[contains(text(), 'Cancel Booking')]"

    # All locators from the Offers Page
    offers_header_option = "//ul[@class='navbar-nav ml-auto']//a[contains(text(), 'Offers')]"
    bus_bookings_offer_heading = "//div[@class='container']//..//h1"

    # All locators from the Get Free Rides Page
    get_free_rides_header_option = "//ul[@class='navbar-nav ml-auto']//a[contains(text(), 'Get Free Rides')]"
