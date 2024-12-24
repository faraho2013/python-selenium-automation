from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@then('Verify search results shown for {product}')
def verify_search_result(context, product):
    context.app.search_results_page.verify_search_result(product)

@when('Add {product} to the cart')
def add_to_cart(context, product):
    context.app.search_results_page.add_to_cart(product)

@when('Add to cart from side nav')
def add_to_cart_from_side_nav(context):
    context.app.search_results_page.add_to_cart_from_side_nav()

@then('Verify search term for {product} in url')
def verify_search_term_in_url(context, product):
    context.app.search_results_page.verify_search_term_in_url(product)

@then("Verify added to cart message")
def verify_cart_empty(context):
    expected_result = 'Added to cart'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '[data-test="modal-drawer-heading"] .h-text-lg').text
    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'