from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shopping_cart_total():
    firefox_driver_path = (
        r"C:\Users\freebook\Downloads\geckodriver-v0.36.0-win64\geckodriver.exe"
    )

    driver = webdriver.Firefox(service=FirefoxService(firefox_driver_path))
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

        add_backpack = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        )
        add_tshirt = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        add_onesie = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        )

        add_backpack.click()
        add_tshirt.click()
        add_onesie.click()

        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        first_name = driver.find_element(By.ID, "first-name")
        last_name = driver.find_element(By.ID, "last-name")
        postal_code = driver.find_element(By.ID, "postal-code")

        first_name.send_keys("Иван")
        last_name.send_keys("Петров")
        postal_code.send_keys("123456")

        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        total_element = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_text = total_element.text
        total_value = total_text.split("$")[1]

        error_msg = f"Expected $58.29, but got ${total_value}"
        assert total_value == "58.29", error_msg

    finally:
        driver.quit()
