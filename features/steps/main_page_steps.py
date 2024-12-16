from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

TARGET_CIRCLE_ON_MAIN = (By.ID, "utilityNav-circle")
ADD_TO_CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_BUTTON_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SEARCH_FOR_PRODUCT = (By.ID, "search")
@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@given('Open target circle from main page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    context.driver.wait.until(EC.visibility_of_element_located(TARGET_CIRCLE_ON_MAIN))
    context.driver.find_element(*TARGET_CIRCLE_ON_MAIN).click()


@when('Search for {product}')
def search_product(context, product):
    context.driver.wait.until(EC.visibility_of_element_located(SEARCH_FOR_PRODUCT))
    context.driver.find_element(*SEARCH_FOR_PRODUCT).send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)


@when('Add {product} to the cart')
def search_product(context, product):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BUTTON_SIDE_NAV))
    context.driver.find_element(*ADD_TO_CART_BUTTON_SIDE_NAV).click()

@when('Click on Cart icon')
def click_cart(context):
    context.driver.wait.until(EC.visibility_of_element_located(ADD_TO_CART_ICON))
    context.driver.find_element(*ADD_TO_CART_ICON).click()

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