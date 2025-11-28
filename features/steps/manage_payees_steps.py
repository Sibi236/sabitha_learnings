from behave import given, when, then
from selenium.webdriver.common.by import By

@given('the user opens the Stake web application')
def step_open_app(context):
    context.driver.get("https://renter-web-app-staging.stake.rent/")

@given('the user enters "{value}" in the phone or email field')
def step_enter_email(context, value):
    email_field = context.driver.find_element(By.ID, "emailOrPhone")   
    email_field.clear()
    email_field.send_keys(value)

@given('the user clicks on "Sign In"')
def step_click_signin(context):
    pass

@given('the user enters verification code "{code}"')
def step_enter_code(context, code):
    pass

@given('the user clicks "Next"')
def step_click_next(context):
    pass

@given('the user navigates to the Pay Rent page')
def step_go_to_pay_rent(context):
    pass

@given('the user selects "Manage Payees" from Rent Payments section')
def step_manage_payees(context):
    pass

@when("the user clicks the Add New Payee button")
def step_click_add_payee(context):
    pass

@then('the Add New Payee popup should be displayed')
def step_popup_displayed(context):
    pass

@then('all mandatory fields should be visible:')
def step_fields_visible(context):
    for row in context.table:
        print("Check field:", row['field'])

@when('the user enters valid payee details')
def step_enter_details(context):
    for row in context.table:
        print(f"Field: {row['field']}  Value: {row['value']}")

@when('the user clicks "Continue"')
def step_continue(context):
    pass

@then('the user should see "Payee added successfully"')
def step_success_message(context):
    pass

@then('the new payee should appear in the list')
def step_list(context):
    pass

@when('the user enters existing payee details')
def step_existing(context):
    pass

@then('the user should see "Payee already exists"')
def step_duplicate(context):
    pass

@then('the user should see "Couldn\'t add payee. Try again"')
def step_failed(context):
    pass

@when('the user clicks "Cancel"')
def step_cancel(context):
    pass

@then('the Add New Payee popup should close')
def step_popup_close(context):
    pass

@when('the server returns an error')
def step_server_error(context):
    # Simulate server error / failed API response
    # You can mock this or set a flag in the UI logic
    context.server_error = True
    pass

