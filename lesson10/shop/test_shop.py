import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.login_page import LoginPage
from pages.checkout_overview_page import CheckoutOverviewPage


@allure.feature("Корзина покупок")
@allure.severity(allure.severity_level.CRITICAL)
class TestShoppingCart:
    @allure.title("Проверка итоговой суммы корзины")
    @allure.description("Тест проверяет корректность расчета общей суммы")
    def test_shopping_cart_total(self) -> None:
        firefox_driver_path = (
            r"C:\Users\freebook\Downloads\geckodriver-v0.36.0-win64"
            r"\geckodriver.exe"
        )

        driver = webdriver.Firefox(service=FirefoxService(firefox_driver_path))

        try:
            with allure.step("Выполнить авторизацию"):
                login_page = LoginPage(driver)
                main_page = login_page.open().login("standard_user",
                                                   "secret_sauce")

            with allure.step("Добавить товары в корзину"):
                (main_page.wait_for_load()
                 .add_backpack_to_cart()
                 .add_tshirt_to_cart()
                 .add_onesie_to_cart()
                 .go_to_cart()
                 .proceed_to_checkout()
                 .fill_personal_info("Иван", "Петров", "123456")
                 .continue_to_overview())

            with allure.step("Проверить итоговую сумму"):
                overview_page = CheckoutOverviewPage(driver)
                total_text = overview_page.get_total_amount()
                total_value = total_text.split("$")[1]

                error_msg = f"Expected $58.29, but got ${total_value}"
                assert total_value == "58.29", error_msg

        finally:
            driver.quit()


if __name__ == "__main__":
    TestShoppingCart().test_shopping_cart_total()
