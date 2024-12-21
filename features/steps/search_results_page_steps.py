from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify search results shown for {product}')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_result(product)

@then("Verify added to cart message")
def verify_cart_empty(context):
    expected_result = 'Added to cart'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '[data-test="modal-drawer-heading"] .h-text-lg').text
    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'