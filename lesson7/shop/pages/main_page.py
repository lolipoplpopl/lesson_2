from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import CartPage


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
        cart_icon = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        )
        cart_icon.click()
        return CartPage(self.driver)
