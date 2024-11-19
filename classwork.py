import requests
from bs4 import BeautifullSoup

url = 'https://'

response = requests.get(url)
soup = BeautifullSoup(response.text, 'html.parser')

#Очистка данных
# tr - каждый ряд таблицы
# td - каждая ячейка внутри ряда таблицы
rows = soup.find_all('tr')
data = []

for row in rows:
    cols = row.find_all('td')
    cleaned_cols = [col.text.strip() for col in cols] # укороченный вариант цикла for
    data.append(cleaned_cols)

print(data)


#Преобразование данных
data_1 = [
    ['100', '200', '300']
    ['400', '500', '600']
    ]
#С сайта мы получаем именно списки.
numbers = []

for row in data_1:
    for text in row:
        num = float(text)
        numbers.append(num)
        
print(numbers)

#фильтрация
list = []
for row in data_1:
    for i in row:
        if int(i)>100:
            list.append(int(i))
print(list)