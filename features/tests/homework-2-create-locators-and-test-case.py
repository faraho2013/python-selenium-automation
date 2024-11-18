from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# ---------1.Practice with locators. Create locators + search strategy------------
# Amazon logo
# amazon_logo = driver.find_element(By.XPATH, "//i[@role='img']")

# Email field
# amazon_email_field = driver.find_element(By.ID, 'ap_email')

# Continue button
# amazon_continue_button = driver.find_element(By.ID, 'continue')

# Conditions of use link
# amazon_conditions_of_use_link = driver.findElement(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")

# Privacy Notice link
# amazon_privacy_notice_link = driver.findElement(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]")

# Need help link
# amazon_need_help_link = driver.findElement(By.XPATH, "//*[@class='a-expander-prompt']")

# Forgot your password link
# amazon_forgot_your_password_link = driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with Sign-In link or More ways to get support
# more_ways_to_get_support = driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon account button
# create_your_amazon_account_button = driver.find_element(By.ID, 'createAccountSubmit')

# -------2.Create a test case for the SignIn page using python & selenium script.------

# 1. Open the url
driver.get('https://www.target.com/')

# 2. Click SignIn button
driver.find_element(By.XPATH, "//*[text()='Sign in']").click()
sleep(2)

# 3. Click SignIn from side navigation
driver.find_element(By.XPATH, "//button[text()='Sign in']").click()
sleep(2)

# 4. Verify SignIn page opened:
# 4.a “Sign into your Target account” text is shown,
driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']").click()

# 4.b SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)
driver.find_element(By.ID, 'login')
sleep(2)

print('Test Passed')
driver.quit()
