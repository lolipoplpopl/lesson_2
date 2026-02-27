import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.driver.get(url)

    @allure.step("Установить задержку {delay} секунд")
    def set_delay(self, delay: int) -> None:
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay))

    @allure.step("Нажать кнопку {value}")
    def click_button(self, value: str) -> None:
        button = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    @allure.step("Получить результат вычисления")
    def get_result(self, timeout: int = 50) -> str:
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result_display, "15")
        )
        return self.driver.find_element(*self.result_display).text
