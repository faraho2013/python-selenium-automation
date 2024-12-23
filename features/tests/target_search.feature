Feature: Tests for search

  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify search results shown for tea
    Then Verify search term for tea in url

  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search results shown for coffee

  Scenario: User can search for a mug
    Given Open target main page
    When Search for a mug
    Then Verify search results shown for a mug

  Scenario: User can search for tree
    Given Open target main page
    When Search for tree
    Then Verify search results shown for tree
    When Add tree to the cart
    When Add to cart from side nav
    Then Verify added to cart message

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search results shown for <product>
    Examples:
    |product    |
    |coffee     |
    |tea        |
    |mug        |
    |tree       |