from pages.base_page import BasePage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.main_page import MainPage
from pages.cart_page import CartPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultPage(driver)
        self.main_page = MainPage(driver)
        self.cart_page = CartPage(driver)

# app = Application(driver)
# app.base_page()
# app.header.search_product()
# app.main_page.open_main()