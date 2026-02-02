from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.checkout_overview_page import CheckoutOverviewPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_personal_info(self, first_name, last_name, postal_code):
        first_name_field = self.driver.find_element(By.ID, "first-name")
        last_name_field = self.driver.find_element(By.ID, "last-name")
        postal_code_field = self.driver.find_element(By.ID, "postal-code")

        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        postal_code_field.send_keys(postal_code)
        return self

    def continue_to_overview(self):
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()
        return CheckoutOverviewPage(self.driver)
