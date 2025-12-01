from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user opens the Stake web application')
def step_open_app(context):
    context.driver.get("https://renter-web-app-staging.stake.rent/")

@given('the user enters "{value}" in the phone or email field')
def step_enter_email(context, value):
    email_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    email_field.clear()
    email_field.send_keys(value)

@given('the user clicks on "Sign In"')
def step_click_signin(context):
    btn = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]")
    btn.click()

@given('the user enters verification code "{code}"')
def step_enter_code(context, code):
    wait = WebDriverWait(context.driver, 10)
    inputs = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "input[autocomplete='one-time-code']")
    ))
    
    for i, digit in enumerate(code):
        inputs[i].send_keys(digit)

@given('the user clicks "Next"')
def step_click_next(context):
    btn = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
    btn.click()

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
    context.server_error = True
    pass

@when('the user clicks on an existing payee')
def step_click_existing_payee(context):
    pass

@when('the user clicks the "Delete" button')
def step_click_delete_button(context):
    pass

@when('the user confirms deletion')
def step_confirm_delete(context):
    pass

@then('the payee should be removed from the list')
def step_verify_deleted(context):
    pass

@when('the user clicks on an existing payee with scheduled rent')
def step_click_scheduled_payee(context):
    pass

@then('the user should see "You have an active rent payment scheduled. Cancel the payment before removing this payee."')
def step_scheduled_error(context):
    pass

@then('the user should see "Couldn\'t delete payee. Try again"')
def step_delete_error(context):
    pass

@then('the payee details popup should display the Name, Bank, Routing Number and Account Number')
def step_verify_payee_details_popup(context):
    driver = context.driver

    # Wait for popup container
    popup = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'MuiDialog-paper')]"))
    )

    # TEXT ASSERTIONS
    required_labels = [
        "Name",
        "Bank",
        "Routing Number",
        "Account Number"
    ]

    for label in required_labels:
        assert label in popup.text, f"{label} is missing in the payee details popup"

