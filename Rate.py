import requests
from bs4 import BeautifulSoup

url_usd = 'https://www.banki.ru/products/currency/usd/'
url_evro = 'https://www.banki.ru/products/currency/cash/eur/moskva/'

response_usd = requests.get(url_usd)
soup_usd = BeautifulSoup(response_usd.text, 'lxml')

response_evro = requests.get(url_evro)
soup_evro = BeautifulSoup(response_evro.text, 'lxml')


data_dollar = float(soup_usd.find('div', class_= 'Text__sc-vycpdy-0 jBQTbF').text.replace('₽', '').replace(',', '.'))
data_evro = float(soup_evro.find('div', class_= 'Text__sc-vycpdy-0 jBQTbF').text.replace('₽', '').replace(',', '.'))

print(f'    Exchange rate:')
print(f'    1 $ = {data_dollar} ₽')
print(f'    1 € = {data_evro} ₽')
print('---------------------')

rate_evro_to_dollar = round(data_evro/data_dollar, 2)
rate_dollar_to_evro = round(data_dollar/data_evro, 2)

while True:
    currency = input('Enter the currency: ').lower()

    if currency == 'dollar':
        count = float(input('Amount in dollars: '))
        result_rub = round(data_dollar *  count, 2)
        result_evro = round(count * rate_dollar_to_evro, 2)
        print(f'Amount in rubles: {result_rub}')
        print(f'Amount in evro: {result_evro}')

    elif currency == 'evro':
        count = float(input('Amount in evro: '))
        result_rub = round(data_evro * count, 2)
        result_dollar = round(rate_evro_to_dollar * count, 2)
        print(f'Amount in rubles: {result_rub}')
        print(f'Amount in dollars: {result_dollar}')

    elif currency == 'rubles':
        count = int(input('Amount in rubles: '))
        result_dollar = round(count/data_dollar, 2)
        result_evro = round(count/data_evro, 2)
        print(f'Amount in dollars: {result_dollar}')
        print(f'Amount in evro: {result_evro} ')

    elif currency == 'exit':
        break
