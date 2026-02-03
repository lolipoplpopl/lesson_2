from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.checkout_page import CheckoutPage


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def proceed_to_checkout(self):
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
        return CheckoutPage(self.driver)
