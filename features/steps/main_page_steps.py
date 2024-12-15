from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@given('Open target circle from main page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    context.driver.find_element(By.ID, 'utilityNav-circle').click()
    sleep(1)


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)


@when('Add {product} to the cart')
def search_product(context, product):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'][id*='addToCart']").click()
    sleep(5)


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@then('Verify at least 1 header link is shown')
def verify_header_links(context):
    el = context.driver.find_element(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind element:')
    print(el)


@then('Verify {expected_amount} header links are shown')
def verify_header_links_amount(context, expected_amount):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind elements:')
    print(links)
    print(type(len(links)))

    assert len(links) == int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'

@then('Verify {expected_amount} target circle links are shown')
def verify_header_links_amount(context, expected_amount):
    links = context.driver.find_elements(By.CSS_SELECTOR, ".cell-item-content")
    print('\nFind elements:')
    print(links)
    print(type(len(links)))

    assert len(links) > int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'