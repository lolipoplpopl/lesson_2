from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username, password):
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()
        return MainPage(self.driver)


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_load(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )
        return self

    def add_backpack_to_cart(self):
        add_backpack = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        )
        add_backpack.click()
        return self

    def add_tshirt_to_cart(self):
        add_tshirt = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        add_tshirt.click()
        return self

    def add_onesie_to_cart(self):
        add_onesie = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        )
        add_onesie.click()
        return self

    def go_to_cart(self):
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        return CartPage(self.driver)


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def proceed_to_checkout(self):
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
        return CheckoutPage(self.driver)


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


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_total_amount(self):
        total_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total_element.text


def test_shopping_cart_total():
    firefox_driver_path = (
        r"C:\Users\freebook\Downloads\geckodriver-v0.36.0-win64\geckodriver.exe"
    )

    driver = webdriver.Firefox(service=FirefoxService(firefox_driver_path))

    try:
        # Используем Page Object паттерн
        login_page = LoginPage(driver)
        main_page = login_page.open().login("standard_user", "secret_sauce")

        main_page.wait_for_load()\
            .add_backpack_to_cart()\
            .add_tshirt_to_cart()\
            .add_onesie_to_cart()\
            .go_to_cart()\
            .proceed_to_checkout()\
            .fill_personal_info("Иван", "Петров", "123456")\
            .continue_to_overview()

        overview_page = CheckoutOverviewPage(driver)
        total_text = overview_page.get_total_amount()
        total_value = total_text.split("$")[1]

        error_msg = f"Expected $58.29, but got ${total_value}"
        assert total_value == "58.29", error_msg

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shopping_cart_total()
