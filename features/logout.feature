Feature: Email Logout
  As a user of the email service Protonmail
  After logging in I want to logout

  Scenario: Successful logout
    Given I am logged in and see my inbox
    When I press my profile button and logout
    Then I should be redirected to the login site

