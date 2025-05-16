import requests
from bs4 import BeautifulSoup

url_usd = 'https://www.banki.ru/products/currency/usd/'
url_euro = 'https://www.banki.ru/products/currency/cash/eur/moskva/'

response_usd = requests.get(url_usd)
soup_usd = BeautifulSoup(response_usd.text, 'lxml')

response_euro = requests.get(url_euro)
soup_euro = BeautifulSoup(response_euro.text, 'lxml')


data_dollar = float(soup_usd.find('div', class_= 'Text__sc-vycpdy-0 jBQTbF').text.replace('₽', '').replace(',', '.'))
data_euro = float(soup_euro.find('div', class_= 'Text__sc-vycpdy-0 jBQTbF').text.replace('₽', '').replace(',', '.'))

print(f'    Exchange rate:')
print(f'    1 $ = {data_dollar} ₽')
print(f'    1 € = {data_euro} ₽')
print('---------------------')

rate_euro_to_dollar = round(data_euro/data_dollar, 2)
rate_dollar_to_euro = round(data_dollar/data_euro, 2)

while True:
    currency = input('Enter the currency: ').lower()

    if currency == 'dollar':
        count = float(input('Amount in dollars: '))
        result_rub = round(data_dollar *  count, 2)
        result_euro = round(count * rate_dollar_to_euro, 2)
        print(f'Amount in rubles: {result_rub}')
        print(f'Amount in euro: {result_euro}')

    elif currency == 'euro':
        count = float(input('Amount in euro: '))
        result_rub = round(data_euro * count, 2)
        result_dollar = round(rate_euro_to_dollar * count, 2)
        print(f'Amount in rubles: {result_rub}')
        print(f'Amount in dollars: {result_dollar}')

    elif currency == 'rubles':
        count = int(input('Amount in rubles: '))
        result_dollar = round(count/data_dollar, 2)
        result_euro = round(count/data_euro, 2)
        print(f'Amount in dollars: {result_dollar}')
        print(f'Amount in euro: {result_euro} ')

    elif currency == 'exit':
        break
