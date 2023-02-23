Feature: validate the login feature
#  Background:
#    Given Launch the browser
#    When Open the URL https://www.abhibus.com/ website
#    Then The login portal has been opened

  @valid_login
  Scenario: Login with valid credentials
    Given Launch the browser
    When Open the URL https://www.abhibus.com/ website
    Then Click on the Login link
    And Enter Mobile number "9010682626"
    And Click the Login or Signup button
    Then Close the browser