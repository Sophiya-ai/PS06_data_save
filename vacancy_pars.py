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

url = 'https://tomsk.hh.ru/vacancies/programmist'

driver.get(url)
WebDriverWait(driver, 3)

vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--hhzAtjuXrYFMBMspDjrF font-inter')

parsed_data = []
for vacancy in vacancies:
    try:
        #title = vacancy.find_element(By.CSS_SELECTOR, 'span[data-qa="serp-item__title-text"]').text
        title_el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-qa="serp-item__title-text"]')))
        title = title_el.text
        company = vacancy.find_element(By.CSS_SELECTOR,
        salary = vacancy.find_element(By.CSS_SELECTOR,
        link = vacancy.find_element(By.CSS_SELECTOR,