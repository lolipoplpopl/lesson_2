from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Настройка драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Открытие страницы
    driver.get("http://uitestingplayground.com/classattr")
    
    # Поиск синей кнопки по CSS-классу (используется частичное совпадение)
    blue_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
    
    # Клик по кнопке
    blue_button.click()
    
    # Обработка алерта (если появится)
    alert = driver.switch_to.alert
    alert.accept()
    
finally:
    # Закрытие браузера
    driver.quit()
