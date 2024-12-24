from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SideNavSignIn(BasePage):
    SIGN_IN_ON_SIDE_NAV = (By.XPATH, "//button[text()='Sign in']")


    def side_nav_sign_in(self):
        self.wait_for_element_to_be_clickable(*self.SIGN_IN_ON_SIDE_NAV).click()