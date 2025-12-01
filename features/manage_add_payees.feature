Feature: Manage Payees - Add New Payee
  As a Stake user
  I want to add a new payee under Manage Payees
  So that rent payments can be processed securely

  Background:
    Given the user opens the Stake web application
    And the user enters "sibi@stake.rent" in the phone or email field
    And the user clicks on "Sign In"
    And the user enters verification code "555555"
    And the user clicks "Next"
    And the user navigates to the Pay Rent page
    And the user selects "Manage Payees" from Rent Payments section

  @add_new_payee
  Scenario: User adds a new payee successfully
    When the user clicks the Add New Payee button
    Then the Add New Payee popup should be displayed
    And all mandatory fields should be visible:
      | field                 |
      | Full Name             |
      | Routing Number        |
      | Account Number        |
      | Confirm Account Number|
    When the user enters valid payee details:
      | field                 | value       |
      | Full Name             | John Carter |
      | Routing Number        | 123456789   |
      | Account Number        | 987654321   |
      | Confirm Account Number| 987654321   |
    And the user clicks "Continue"
    Then the user should see "Payee added successfully"
    And the new payee should appear in the list

  @duplicate_payee
  Scenario: User tries to add an existing payee
    When the user clicks the Add New Payee button
    And the user enters existing payee details
    And the user clicks "Continue"
    Then the user should see "Payee already exists"

  @failed_response
  Scenario: Add payee fails due to server issue
    When the user clicks the Add New Payee button
    And the user enters valid payee details
    And the server returns an error
    Then the user should see "Couldn't add payee. Try again"

  @cancel_button
  Scenario: User cancels Add New Payee popup
    When the user clicks the Add New Payee button
    And the user clicks "Cancel"
    Then the Add New Payee popup should close
