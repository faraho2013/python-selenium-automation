from behave import given, when, then


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()