

from Task_Parsing_Project import get_html
from bs4 import BeautifulSoup

def get_item_details(url:str) -> dict:
    data = {}
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")

#     # ищем описание
    # desc_div = soup.find("div", {"class":"rows"})
    # desc = desc_div.find("span", {"class":"prouct_name"}).text
    # data["description"] = desc

#     # ищем цену
    price = soup.find_all("span", attrs={"class":"price"}).text
    data['price'] = price

    return data
