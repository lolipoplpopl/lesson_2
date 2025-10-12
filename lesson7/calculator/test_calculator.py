from selenium import webdriver
from calculator_page import CalculatorPage


class TestCalculator:
    def test_calculator_with_delay(self):
        driver = webdriver.Chrome()
        calculator = CalculatorPage(driver)

        try:
            calculator.open()
            calculator.set_delay(45)

            calculator.click_button("7")
            calculator.click_button("+")
            calculator.click_button("8")
            calculator.click_button("=")

            result = calculator.get_result()
            assert result == "15", f"Expected 15, but got {result}"

        finally:
            driver.quit()
