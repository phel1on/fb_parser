
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://proghub.ru/')

"""wait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@='Тесты']"))).click()"""
btn_test = driver.find
btn_test.click()
