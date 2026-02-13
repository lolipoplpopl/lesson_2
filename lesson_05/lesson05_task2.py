from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_id_button():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("http://uitestingplayground.com/dynamicid")

        xpath_locator = (
            "//button[contains(@class, 'btn-primary') and "
            "text()='Button with Dynamic ID']"
        )
        blue_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_locator))
        )
        blue_button.click()

        print("Клик по кнопке с динамическим ID выполнен успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_dynamic_id_button()
