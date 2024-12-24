from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignInPage(BasePage):
    SIGN_IN_PAGE_TEXT = (By.XPATH, "//*[text()='Sign into your Target account']")
    SIGN_IN_BUTTON = (By.ID, 'login')


    def verify_sign_in_page_text(self):
        self.wait_for_element_to_be_visible(*self.SIGN_IN_PAGE_TEXT)


    def sign_in_button(self):
        self.wait_for_element_to_be_visible(*self.SIGN_IN_BUTTON).text()