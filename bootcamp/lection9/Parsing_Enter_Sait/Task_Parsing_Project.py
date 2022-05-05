import requests
from bs4 import BeautifulSoup



BASE_URL = "https://enter.kg"


def get_html(html):

    response =requests.get(html) 
    return response.text


def get_links(html):
    soup = BeautifulSoup(get_html(html), 'html.parser')
    product_links_container = soup.find_all('div', attrs={'class': 'row'})
    list_ = []
    for div in product_links_container:
        res = div.find('a', attrs={'class': 'product-image-link'}).get(('href'))
        list_.append(res)
    return list_


def all_product():
    all_products_links = get_links(html)
    sum_links = []
    for product_url in all_products_links:
        name_links = BASE_URL + product_url
        sum_links.append(name_links)
    return sum_links


def get_all_html():
    list1 = []
    proverka = all_product()
    for i in proverka:
        x = requests.get(i)
        list1.append(x.text)
    return list1[0]



def get_item_details():
    details = get_all_html()
    soup = BeautifulSoup(details, "html.parser")

    ves_price = []
    price1 = soup.find_all('span', attrs={'class':'price'})
    for i in price1:
        res1 = i.text
        ves_price.append(res1)
    return ves_price


html = BASE_URL+'/diskovody_opticheskie-privody_bishkek'

print(get_item_details())





