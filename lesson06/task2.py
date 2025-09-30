from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    url = "http://uitestingplayground.com/textinput"
    driver.get(url)

    input_selector = "input#newButtonName"
    text_input = driver.find_element(By.CSS_SELECTOR, input_selector)
    text_input.clear()
    text_input.send_keys("SkyPro")

    button_selector = "button#updatingButton"
    button = driver.find_element(By.CSS_SELECTOR, button_selector)
    button.click()

    wait = WebDriverWait(driver, 10)
    condition = EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, button_selector), "SkyPro"
    )
    wait.until(condition)

    updated_button = driver.find_element(By.CSS_SELECTOR, button_selector)
    print(updated_button.text)

finally:
    driver.quit()
