from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.sign_in_page import SignInPage
from pages.side_nav_sign_in_page import SideNavSignIn
from pages.target_app_page import TargetAppPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.terms_and_cond_page import TermsAndConditionsPage

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.cart_page = CartPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.side_nav_sign_in_page = SideNavSignIn(driver)
        self.target_app_page = TargetAppPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.terms_and_cond_page = TermsAndConditionsPage(driver)

# app = Application(driver)
# app.base_page()
# app.header.search_product()
# app.main_page.open_main()