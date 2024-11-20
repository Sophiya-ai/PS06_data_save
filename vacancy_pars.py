import csv
#import time
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

vacancies = driver.find_elements(By.CSS_SELECTOR, 'div[data-qa="vacancy-serp__vacancy vacancy-serp__vacancy_standard_plus"]')
print(vacancies)

parsed_data = []
for vacancy in vacancies:
    try:
        #title = vacancy.find_element(By.CSS_SELECTOR, 'span[data-qa="serp-item__title-text"]').text
        title_el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-qa="serp-item__title-text"]')))
        title = title_el.text
        company = vacancy.find_element(By.CSS_SELECTOR,'span[data-qa="vacancy-serp__vacancy-employer-text"]').text
        try:
            salary = vacancy.find_element(By.CSS_SELECTOR, "div.compensation-labels--cR9OD8ZegWd3f7Mzxe6z span.magritte-text___pbpft_3-0-18").text
        except:
            salary = "Зарплата не указана"
        link = vacancy.find_element(By.CSS_SELECTOR,'a.magritte-link___b4rEM_4-3-12').get_attribute('href')
    except Exception as e:
        print(f'Возникла ошибка {e} при парсинге')
        continue

    parsed_data.append([title,company,salary,link])

driver.quit()

with open ('hh.csv', 'w', newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    # Создаём объект
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название вакансии', "Название компании", "Зарплата", "Ссылка на вакансию"])
    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)