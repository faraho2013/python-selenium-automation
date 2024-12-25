Feature: Tests for Target App page

  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And Store original window
    When Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And Close current page
    And Return to original window

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target main page
    And Store original window
    When Click sign in on header
    When Click sign in from side nav
    And Click on Target terms and conditions link
    When Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close current page
    And Return to original window