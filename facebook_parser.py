from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import ChromiumOptions

# запуск драйвера
driver = webdriver.Chrome('chromedriver.exe')
#добавление юзер агента
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"')
driver = webdriver.Chrome(chrome_options=chrome_options)
# вход на страницу сайта
driver.get('https://www.facebook.com/NYCoin/')
#ожидание 5 сек для прогрузки стр
time.sleep(5)
# поиск строки ввода логина и передача ему ключа
#element = driver.find_element_by_xpath("//input[@class='inputtext login_form_input_box']").send_keys("phelion@mail.ru")
#ожидание 5 сек
#time.sleep(5)
# поиск строки с паролем и передача ему ключа
#element = driver.find_element_by_xpath("//input[@data-testid='royal_pass']").send_keys("isa5693065")
#ожидание 5 сек
#time.sleep(5)

#element = driver.find_element_by_xpath("//input[@data-testid='royal_login_button']").click()

#time.sleep(5)


#
#
#