import time, csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://tomsk.hh.ru/vacancies/programmist'

driver.get(url)
time.sleep(3)

vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--hhzAtjuXrYFMBMspDjrF font-inter')

parsed_data = []