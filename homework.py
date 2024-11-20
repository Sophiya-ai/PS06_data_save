import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()  # Можно настроить опции, если требуется
options.add_argument("--no-sandbox") #для устранения возможных проблем доступа к системе
options.add_argument("--disable-dev-shm-usage") #для использования разделяемой памяти, что может предотвратить сбои при недостатке ресурсов
driver = webdriver.Chrome(options=options)

url = 'https://www.divan.ru/category/svet'

driver.get(url)
WebDriverWait(driver, 5)

all_light = driver.find_elements(By.CLASS_NAME, 'LlPhw')
WebDriverWait(driver, 15)

print(len(all_light))

light_pars = []

for light in all_light:
    prices = []
    try:
        name = light.find_element(By.CLASS_NAME, 'ProductName').text
        print(name)
        prices = light.find_elements(By.CLASS_NAME, 'ui-LD-ZU')
        price = prices[0].text.strip(' руб.')
        print(price)
        try:
            old_price = prices[1].text.strip(' руб.')
            print(old_price)
        except:
            old_price = "скидка не применялась"
        link = light.find_element(By.TAG_NAME, 'link').get_attribute('href')
        print(link)

    except Exception as e:
        print(f'Ошибка при парсинге: {e}')
        continue

    light_pars.append([name,price,old_price,link])

driver.quit()

with open('lights.csv', 'w', newline = '', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Наименование", "Цена", "Цена без скидки","Ссылка на товар"])
    writer.writerows(light_pars)