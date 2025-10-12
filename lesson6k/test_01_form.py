from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    edge_driver_path = r"C:\Users\freebook\Desktop\table\msedgedriver.exe"

    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    wait = WebDriverWait(driver, 10)

    try:
        url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        driver.get(url)

        first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
        first_name.send_keys("Иван")

        last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
        last_name.send_keys("Петров")

        address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
        address.send_keys("Ленина, 55-3")

        email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
        email.send_keys("test@skypro.com")

        phone = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
        phone.send_keys("+7985899998787")

        city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
        city.send_keys("Москва")

        country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
        country.send_keys("Россия")

        job = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
        job.send_keys("QA")

        company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
        company.send_keys("SkyPro")

        submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_btn.click()

        zip_code_field = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.input-group"))
        )
        assert "alert-danger" in zip_code_field.get_attribute("class")

        valid_fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company"
        ]

        for field in valid_fields:
            field_element = driver.find_element(By.ID, field)
            parent_div = field_element.find_element(By.XPATH, "./..")
            assert "alert-success" in parent_div.get_attribute("class")

    finally:
        driver.quit()
