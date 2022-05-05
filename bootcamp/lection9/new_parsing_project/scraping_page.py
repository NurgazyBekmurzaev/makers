import time

import requests
from bs4 import BeautifulSoup
from helpers import get_tags, is_disabled

# find - return soup object
# find_all() - return list(python list) of find object


BASE_URL = "https://www.kivano.kg"

def get_last_page():
    html = get_html(BASE_URL + '/elektronika')
    soup = BeautifulSoup(html, "html.parser")
    last_page = soup.find("li", {"class":"last"}).text
    return last_page


def get_html(url):
    """Получает ссылку и возвращает
    его структуру html ввиде текста
    """
    response = requests.get(url)
    return response.text


def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_links_container = soup.find('div', attrs={'class': 'list-view'})
    res = product_links_container.find_all('div', attrs={'class': 'listbox_title'})
    list_of_a = get_tags(res, 'a', attrs={})
    return list_of_a


def get_all_links():
    all_links = []
    # находим номер последней страницы
    last_page = get_last_page()
    url = BASE_URL + "/elektronika?page={}"
    # проходимся по каждой странице
    for page in range(116, int(last_page)+1):
        print(page)
        html = get_html(url.format(page))
        # добавляем в список новые ссылки на продукты
        all_links += get_links(html)

    return all_links


if __name__ == '__main__':
    print(get_all_links())








