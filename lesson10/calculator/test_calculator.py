import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
class TestCalculator:
    @allure.title("Тест калькулятора с задержкой 45 секунд")
    @allure.description("Проверка работы калькулятора с установленной задержкой вычислений")
    def test_calculator_with_delay(self) -> None:
        driver = webdriver.Chrome()
        calculator = CalculatorPage(driver)

        try:
            with allure.step("Открыть страницу калькулятора"):
                calculator.open()

            with allure.step("Установить задержку 45 секунд"):
                calculator.set_delay(45)

            with allure.step("Выполнить вычисление 7 + 8"):
                calculator.click_button("7")
                calculator.click_button("+")
                calculator.click_button("8")
                calculator.click_button("=")

            with allure.step("Проверить результат вычисления"):
                result = calculator.get_result()
                assert result == "15", f"Expected 15, but got {result}"

        finally:
            driver.quit()
