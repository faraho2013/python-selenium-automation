from pages.base_page import BasePage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.sign_in_page import SignInPage
from pages.side_nav_sign_in_page import SideNavSignIn

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultPage(driver)
        self.main_page = MainPage(driver)
        self.cart_page = CartPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.side_nav_sign_in_page = SideNavSignIn(driver)

# app = Application(driver)
# app.base_page()
# app.header.search_product()
# app.main_page.open_main()