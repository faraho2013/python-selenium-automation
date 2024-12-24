from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchResultPage(BasePage):
    SEARCH_RESULT_HEADING = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    ADD_TO_CART_BUTTON_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")

    def verify_search_result(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULT_HEADING)

    def verify_search_term_in_url(self, product):
        self.verify_partial_url(product)

    def add_to_cart(self, product):
        self.wait_for_element_to_be_clickable(*self.ADD_TO_CART_BUTTON).click()

    def add_to_cart_from_side_nav(self):
        self.wait_for_element_to_be_clickable(*self.ADD_TO_CART_BUTTON_SIDE_NAV).click()