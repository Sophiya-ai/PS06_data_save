import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()  # Можно настроить опции, если требуется
options.add_argument("--no-sandbox") #для устранения возможных проблем доступа к системе
options.add_argument("--disable-dev-shm-usage") #для использования разделяемой памяти, что может предотвратить сбои при недостатке ресурсов
driver = webdriver.Chrome(options=options)

url = 'https://www.divan.ru/category/svet'

driver.get(url)
WebDriverWait(driver, 3)

all_light = driver.find_elements(By.CSS_SELECTOR, 'div[data-qa="vacancy-serp__vacancy vacancy-serp__vacancy_standard_plus"]')
print(all_light)