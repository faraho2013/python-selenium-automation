Feature: Tests for Main page UI

  Scenario: User can see header links
    Given Open target main page
    Then Verify at least 1 header link is shown

  Scenario: User can see correct amount of header links
    Given Open target main page
    Then Verify 6 header links are shown

  Scenario: User can see right amount of header links
    Given Open target circle from main page
    Then Verify 10 target circle links are shown
