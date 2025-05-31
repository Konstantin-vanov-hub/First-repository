import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
url_usd = 'https://www.banki.ru/products/currency/usd/'
url_euro = 'https://www.banki.ru/products/currency/cash/eur/moskva/'

response_usd = requests.get(url_usd)
soup_usd = BeautifulSoup(response_usd.text, 'lxml')

response_euro = requests.get(url_euro)
soup_euro = BeautifulSoup(response_euro.text, 'lxml')

data_dollar = float(soup_usd.find('div', class_= 'Text__sc-vycpdy-0 jBQTbF').text.replace('₽', '').replace(',', '.'))
data_euro = float(soup_euro.find('div', class_= 'Text__sc-vycpdy-0 jBQTbF').text.replace('₽', '').replace(',', '.'))

rate_euro_to_dollar = round(data_euro/data_dollar, 2)
rate_dollar_to_euro = round(data_dollar/data_euro, 2)

root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x400")  

currensy = ['Dollar', 'Euro', 'Ruble']
default_font = ('Arial', 10)
default_font_bold = font.Font(family='Arial',size=10, weight ='bold')

bottom_frame = tk.Frame(root)
bottom_frame.pack(side='bottom', pady=10)

result_label_summa = tk.Label(root, text='Value:',font=default_font)
result_label_summa.pack()

entry = tk.Entry(root, width=30, font=default_font)
entry.pack(pady=(10, 5))

result_label_from = tk.Label(root, text='From:',font=default_font)
result_label_from.pack()

combobox1 = ttk.Combobox(values=currensy, width=28, font=default_font)
combobox1.pack(pady=5)

result_label_to = tk.Label(root, text='To:',font=default_font)
result_label_to.pack()

combobox2 = ttk.Combobox(values=currensy, width=28, font=default_font)
combobox2.pack(pady=5)

result_label_title = tk.Label(root, text='RATE:',font=default_font_bold)
result_label_title.pack()
result_label_dollar = tk.Label(root, text=f'1$ = {data_dollar}₽',font=default_font)
result_label_euro = tk.Label(root,text=f'1€ = {data_euro}₽',font=default_font)
result_label_dollar.pack(pady=(5,0))
result_label_euro.pack(pady=(5,0))

result_label_title = tk.Label(root, text='RESULT:',font=default_font_bold)
result_label_title.pack()
result_output = tk.Label(root, text='',font=default_font_bold)
result_output.pack()


def get_entry():
    try:
        text = int(entry.get())
        a = combobox1.get()
        b = combobox2.get()
    except ValueError:
        result_output.config(text='Invalid value')
    

    if a == 'Dollar' and b == 'Euro':
        def dollar_to_euro():
            result_euro = round((text) * rate_dollar_to_euro, 2)
            return result_euro
        result_output.config(text=f'{dollar_to_euro()}€')

    if a == 'Dollar' and b == 'Ruble':
        def dollar_to_rubles():
            result_rub = round(data_dollar *  text, 2)
            return result_rub
        result_output.config(text=f'{dollar_to_rubles()}₽')

    if a == 'Euro' and b == 'Dollar':
        def euro_to_dollar():
            result_dollar = round(rate_euro_to_dollar * text, 2)
            return result_dollar
        result_output.config(text=f'{euro_to_dollar()}$')

    if a == 'Euro' and b =='Ruble':
        def euro_to_ruble():
            result_rub = round(data_euro * text, 2)
            return result_rub
        result_output.config(text=f'{euro_to_ruble()}₽')

    if a == 'Ruble' and b == 'Dollar':
        def ruble_to_dollar():
            result_dollar = round(text/data_dollar, 2)
            return result_dollar
        result_output.config(text=f'{ruble_to_dollar()}$')

    if a == 'Ruble' and b == 'Euro':
        def ruble_to_euro():
            result_euro = round(text/data_euro, 2)
            return result_euro
        result_output.config(text=f'{ruble_to_euro()}€')

btn_main = tk.Button(root, text='Convert',font=default_font,width=20, command=get_entry)
btn_main.pack(side='bottom', pady=(0, 20))
root.mainloop()