Feature: Email Send
  As a user of the email service Protonmail
  I want to send an email with an attachment after logging in

  Scenario: Successfully send an email with an attachment
    Given I am logged in and see my inbox
    When I click on the new message button
    And I fill in the recipient, subject and attach a file
    Then I click the send button