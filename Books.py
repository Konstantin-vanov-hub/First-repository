import requests
import time
import csv
from bs4 import BeautifulSoup
from tqdm import tqdm

with open('Books.csv', 'w', newline = '', encoding = 'utf-8') as file:
    writer = csv.writer(file) 
    writer.writerow(['Title:','Price:','Stock:','Raiting:'])

    count = 0

    stars_list = ['One', 'Two', 'Three', 'Four', 'Five']

    page = 1

    for i in tqdm(range(1, 51), desc = 'Downloading: '):

        time.sleep(3)

        url = f'https://books.toscrape.com/catalogue/page-{page}.html'

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

        print(f'Page: {page}')

        page += 1

        for i in data:

            title = i.find('h3').find('a')['title']

            price = i.find('p', class_='price_color').text.replace('Â','')

            stock = i.find('p',class_='instock availability').text.strip()

            raiting = i.find('p',class_='star-rating')

            raiting_classes = raiting.get('class')

            star = [r for r in raiting_classes if r in stars_list][0]

            count += 1

            print(count, f'Title: {title} \n' 
                f'   Price: {price} \n'
                f'   Stock: {stock} \n' 
                f'   Reiting: {star} \n')

            writer.writerow([title, price, stock, star])