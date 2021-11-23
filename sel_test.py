from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://google.com')


wait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[contains(@aria-label,'Найти')]"))).send_keys(
    "test"
)

wait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[contains(@value,'Поиск в Google')]"))).click()


driver.quit()

