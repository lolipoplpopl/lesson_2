from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_blue_button_click():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("http://uitestingplayground.com/classattr")

        xpath_locator = "//button[contains(@class, 'btn-primary')]"
        blue_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_locator))
        )
        blue_button.click()

        alert = wait.until(EC.alert_is_present())
        alert.accept()

        print("Тест успешно завершен!")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_blue_button_click()
