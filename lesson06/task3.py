from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    driver.get(url)

    images = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )

    WebDriverWait(driver, 10).until(
        lambda driver: all(
            image.get_attribute("complete")
            for image in driver.find_elements(By.TAG_NAME, "img")
        )
    )

    third_image = driver.find_elements(By.TAG_NAME, "img")[2]
    src_value = third_image.get_attribute("src")

    print(src_value)

finally:
    driver.quit()
