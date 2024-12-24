from behave import given, when, then


@when('Click sign in on header')
def header_sign_in(context):
    context.app.header.header_sign_in()


@when('Click sign in from side nav')
def side_nav_sign_in(context):
    context.app.side_nav_sign_in_page.side_nav_sign_in()

@then('Verify sign in form opened')
def verify_sign_in_page_text(context):
    context.app.sign_in_page.verify_sign_in_page_text()