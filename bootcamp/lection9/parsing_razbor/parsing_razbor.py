from itertools import count, product
import requests
from bs4 import BeautifulSoup
import csv


def get_soup(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_every_element(html):
    links = []
    divs = html.find_all('div', attrs ={'class':'row'})
    for div in divs:
        a = div.find("a").get(("href"))
        if a[0] == '/':
            links.append(a)
    return links
  

def get_one_link():
    every_element = get_every_element(html)
    html1 = ''
    count = 0
    for every in every_element:
        full_every = url + every
        response = requests.get(full_every)
        # soup = BeautifulSoup(response.text, 'html.parser')
        html1 += response.text
        count += 1
        print(count)
    return html1


def img_title_price():
    all_html = get_one_link()
    soup = BeautifulSoup(all_html, 'html.parser')
    
    all_imgs = []
    imgs = soup.find_all('img')
    for img in imgs:
        all_imgs.append(img.get('src'))


    all_price = []
    prices = soup.find_all('span', attrs = {'class':'price'})
    for i in prices:
        res = i.text
        all_price.append(res)


    all_name = []
    name  =soup.find_all('span', attrs={'class': 'prouct_name'})
    for x in name:
        res1 = x.text
        all_name.append(res1)
    # print(all_name)


    return list(zip(all_imgs, all_price, all_name)) 




URL = 'https://enter.kg/fleshki_bishkek'
html = get_soup(URL) 
url = 'https://enter.kg'
print(img_title_price())