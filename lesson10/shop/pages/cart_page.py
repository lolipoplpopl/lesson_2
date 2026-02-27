import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from pages.checkout_page import CheckoutPage


class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Перейти к оформлению заказа")
    def proceed_to_checkout(self) -> CheckoutPage:
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
        return CheckoutPage(self.driver)
