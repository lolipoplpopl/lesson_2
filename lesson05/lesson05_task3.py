from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_input_field():
    # Используем браузер Firefox
    driver = webdriver.Firefox()

    try:
        driver.get("http://the-internet.herokuapp.com/inputs")

        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )

        input_field.send_keys("Sky")

        input_field.clear()

        input_field.send_keys("Pro")

        print("Операции с полем ввода выполнены успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_input_field()
