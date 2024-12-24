from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element_to_be_visible(self, *locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"The element by {locator} is not visible"
        )

    def wait_for_element_to_be_invisible(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f"The element by {locator} is visible"
        )

    def wait_for_element_to_be_clickable(self, *locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"The element by {locator} is not clickable"
        )

    def wait_for_element_and_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"The element by {locator} is not clickable"
        ).click()

    def verify_partial_text(self, expected_text, *locator):
        actual_result = self.find_element(*locator).text
        assert expected_text in actual_result, f'Expected {expected_text} not in actual {actual_result}'

    def varify_text(self, expected_text, *locator):
        actual_result = self.find_element(*locator).text
        assert expected_text == actual_result, f'Expected {expected_text} but got {actual_result}'

    def verify_partial_url(self, expected_url, *locator):
        actual_url = self.driver.current_url
        assert expected_url in actual_url, f'Expected partial url {expected_url} not in actual {actual_url}'

    def varify_url(self, expected_url, *locator):
        actual_url = self.find_element(*locator).text
        assert expected_url == actual_url, f'Expected url {expected_url} but got {actual_url}'

# page = BasePage
# element = page.find_element((By.CSS_SELECTOR, "[id*='addToCartButton']"))
# element.text