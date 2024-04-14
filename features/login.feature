Feature: Email Login
  As a user of the email service Protonmail
  I want to login with my credentials

  Scenario: Successful login with correct credentials
    Given I am on the email login page
    When I enter my email address and password
    And I click on the login button
    Then I should be redirected to the inbox

