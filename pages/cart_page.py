from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class CartPage(BasePage):
    CART_EMPTY_TEXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_cart_empty(self):
        expected_result = 'Your cart is empty'
        actual_result = self.driver.find_element(*self.CART_EMPTY_TEXT).text
        assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'
