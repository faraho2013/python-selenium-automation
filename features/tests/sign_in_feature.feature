Feature: Test for sign in

  Scenario: A user can sign in
    Given Open target main page
    When Click sign in on header
    When Click sign in from side nav
    Then Verify sign in form opened