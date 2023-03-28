Feature: validate the login feature
  Background:
    Given Launch the browser
    When Open the URL https://www.abhibus.com/ website
#    Then The login portal has been opened

  @valid_login @Login
  Scenario: Login with valid credentials
#    Given Launch the browser
#    When Open the URL https://www.abhibus.com/ website
    Then Click on the Login link
    And Enter a valid Mobile number
    And Click the Login or Signup button
    And OTP request message to be displayed
    Then Close the browser

  @invalid_login @Login
 Scenario Outline: Login with invalid mobile number
    Then Click on the Login link
    And Enter an invalid mobile number "<mobilenumber>"
    And Click the Login or Signup button
    And Error message is displayed when mobile number is invalid
    Then Close the browser
    Examples:
      | mobilenumber |
      | 00123423     |
      | 901068         |


  @invalid_login
 Scenario: Login with empty mobile number
   Then Click on the Login link
    And Enter Mobile number is empty
    And Click the Login or Signup button
    And Error message is displayed when mobile number is empty
    Then Close the browser
