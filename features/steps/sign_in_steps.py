from behave import given, when, then


@when('Click sign in on header')
def header_sign_in(context):
    context.app.header.header_sign_in()


@when('Click sign in from side nav')
def side_nav_sign_in(context):
    context.app.side_nav_sign_in_page.side_nav_sign_in()

@when('Click on Target terms and conditions link')
def click_terms_and_conditions_link(context):
    context.app.side_nav_sign_in_page.click_terms_and_conditions_link()

@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.terms_and_cond_page.verify_tc_opened()

@then('Verify sign in form opened')
def verify_sign_in_page_text(context):
    context.app.sign_in_page.verify_sign_in_page_text()