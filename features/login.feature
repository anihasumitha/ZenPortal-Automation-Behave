Feature: Login functionality for Guvi-Zen portal

  Scenario: Username input box is visible
    Given the user is on the Guvi login page
    Then the username input field should be visible

  Scenario: Password input box is visible
    Given the user is on the Guvi login page
    Then the password input field should be visible

  Scenario: Submit button is enabled
    Given the user is on the Guvi login page
    Then the login button should be enabled

  Scenario Outline: Login with different credentials
    Given the user is on the Guvi login page
    When the user enters username "<username>" and password "<password>"
    And the user click login button
    Then login should "<result>"

    Examples:
      | username | password | result  |
      | aniha2525@gmail.com   | Aniha@guvi123 | success |
      | invalid  | hello2  | failure |


  Scenario: Logout button is clickable after successful login
    Given the user is logged in with valid credentials
    Then the logout button should enabled