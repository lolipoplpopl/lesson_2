import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from pages.checkout_overview_page import CheckoutOverviewPage


class CheckoutPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнить личную информацию: {first_name} {last_name}, почтовый индекс {postal_code}")
    def fill_personal_info(self, first_name: str, last_name: str, postal_code: str) -> 'CheckoutPage':
        first_name_field = self.driver.find_element(By.ID, "first-name")
        last_name_field = self.driver.find_element(By.ID, "last-name")
        postal_code_field = self.driver.find_element(By.ID, "postal-code")

        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        postal_code_field.send_keys(postal_code)
        return self

    @allure.step("Перейти к обзору заказа")
    def continue_to_overview(self) -> CheckoutOverviewPage:
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()
        return CheckoutOverviewPage(self.driver)
