Feature: Manage Existing Payees
  As a Stake user
  I want to manage existing payees
  So that I can view, delete or handle errors while deleting payees

  Background:
    Given the user opens the Stake web application
    And the user enters "sibi@stake.rent" in the phone or email field
    And the user clicks on "Sign In"
    And the user enters verification code "555555"
    And the user clicks "Next"
    And the user navigates to the Pay Rent page
    And the user selects "Manage Payees" from Rent Payments section

  @view_payee_details
  Scenario: User views existing payee details
    When the user clicks on an existing payee
    Then the payee details popup should display the Name, Bank, Routing Number and Account Number

  @delete_payee
  Scenario: User deletes an existing payee
    When the user clicks on an existing payee
    And the user clicks the "Delete" button
    And the user confirms deletion
    Then the payee should be removed from the list

  @cannot_delete_scheduled
  Scenario: User tries to delete a payee with scheduled rent
    When the user clicks on an existing payee with scheduled rent
    And the user clicks the "Delete" button
    Then the user should see "You have an active rent payment scheduled. Cancel the payment before removing this payee."

  @delete_failed
  Scenario: Delete payee failed due to server issue
    When the user clicks on an existing payee
    And the user clicks the "Delete" button
    And the server returns an error
    Then the user should see "Couldn't delete payee. Try again"
