from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage

class Header(BasePage):
    SEARCH_FOR_PRODUCT = (By.ID, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    ADD_TO_CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN_ON_MAIN = (By.XPATH, "//*[text()='Sign in']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FOR_PRODUCT)
        self.click(*self.SEARCH_BUTTON)
        sleep(5)

    def click_cart(self):
        # self.click(*self.ADD_TO_CART_ICON)
        self.wait_for_element_and_click(*self.ADD_TO_CART_ICON)

    def header_sign_in(self):
        self.wait_for_element_and_click(*self.SIGN_IN_ON_MAIN)

