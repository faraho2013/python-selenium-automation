# Created by drfar at 12/10/2024
Feature: Test for shopping cart and sign in

  Scenario: Click on target cart icon
    Given Open target main page
    When Click on cart icon
    Then Verify message is shown

  Scenario: Click on Sign in icon
    Given Open target main page
    When Click on Sign in
    Then Verify Sign in form is opened