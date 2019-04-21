# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

#  Scenario: User can search for a product
#    Given Open Google page
#    When Input dress into search field
#    And Click on search icon
#    Then Product results for dress are shown
#    And First result contains dress

  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Input dress into Amazon search field
    And Click on Amazon search icon
    Then Amazon product results for dress are shown

  Scenario:  User can search for solutions of Cancelling an order on Amazon
    Given Open Amazon page
    When Click on Help button
    And Input cancel order into Help search field
    And Click Go button
    Then Cancel Items or Orders text is shown

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Orders button
    Then Verify Email and Password fields are shown

  Scenario: Hamburger menu can be opened and closed
    Given Open Amazon page
    When Click Hamburger menu button
    Then Verify Shop by category text is present
    Then Click on closing X of the menu
    Then Click on Try Prime button from Amazon logo
    Then Verify Try Prime button is present




