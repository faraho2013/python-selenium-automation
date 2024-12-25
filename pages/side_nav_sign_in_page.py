from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SideNavSignIn(BasePage):
    SIGN_IN_ON_SIDE_NAV = (By.XPATH, "//button[text()='Sign in']")
    TERMS_AND_COND = (By.XPATH, "//a[text()='Target terms and conditions']")

    def side_nav_sign_in(self):
        self.wait_for_element_to_be_clickable(*self.SIGN_IN_ON_SIDE_NAV).click()

    def click_terms_and_conditions_link(self):
        self.wait_for_element_to_be_clickable(*self.TERMS_AND_COND).click()

