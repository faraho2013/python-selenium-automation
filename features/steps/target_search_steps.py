from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart?prehydrateClick=true']").click()


@then('Verify message is shown')
def verify_message_is_shown(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//*[text()='Your cart is empty']").text
    assert expected_result == actual_result, f' Expected text {expected_result} did not match {actual_result}'

@when('Click on Sign in')
def click_on_sign_in(context):
    context.driver.find_element(By.XPATH, "//*[text()='Sign in']").click()
    context.driver.find_element(By.XPATH, "//button[text()='Sign in']").click()

@then('Verify Sign in form is opened')
def verify_sign_in_form_is_opened(context):
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.XPATH, "//*[@id='__next']/div/div/div/div[1]/div/h1/span").text
    assert expected_result == actual_result, f'Expected text {expected_result} did not match {actual_result}'

