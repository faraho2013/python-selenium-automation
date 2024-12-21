from itertools import product

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchResultPage(BasePage):
    SEARCH_RESULT_HEADING = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search_result(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULT_HEADING).text
        assert product in actual_result, f'Expected text {product} not in actual {actual_result}'

