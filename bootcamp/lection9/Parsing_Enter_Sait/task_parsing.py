# import requests
# source = requests.get('https://stackoverflow.com/questions').status_code
# print(source)


# import requests
# from bs4 import BeautifulSoup
# import lxml
# source = requests.get('http://www.example.com/').text
# my_page = BeautifulSoup(source, 'lxml')
# print('h1: ', my_page.h1.text)
# print('p: ', my_page.p.text)
# print('a: ', my_page.find('a').get('href'))


# import requests
# from bs4 import BeautifulSoup
# import lxml
# source = requests.get('https://www.wikipedia.org/').text
# de = BeautifulSoup(source, 'lxml')
# res = de.find(id="js-link-box-de")
# print(res.strong.text)
# print(res.small.text)


# import requests
# from bs4 import BeautifulSoup
# import lxml
# def getTitle(url):
#     source = requests.get(url).text
#     soup = BeautifulSoup(source, 'lxml')
#     if soup.h1:
#         return soup.h1.text
#     else:
#         return 'Title could not be found'

# print(getTitle('http://www.example.com/'))


# import requests
# from bs4 import BeautifulSoup
# import lxml
# source = requests.get('https://www.makers.kg').text
# soup = BeautifulSoup(source, 'lxml')
# t = soup.find_all('h3', 'feature-cards-card-info-title')
# for x in t:
#     print(x.text)


# import requests
# from bs4 import BeautifulSoup
# import lxml
# source = requests.get('https://www.makers.kg').text
# soup = BeautifulSoup(source, 'lxml')
# images = soup.find_all('img', 'feature-cards-card-image')
# for image in images:
#     res = 'https://www.makers.kg' + image['src'][1:]
#     print(res) 


# import requests
# from bs4 import BeautifulSoup
# import lxml
# source = requests.get('https://www.makers.kg').text
# soup = BeautifulSoup(source, 'lxml')
# post = soup.find_all('div', 'feature-cards-card-info-subtitle')
# for x in post:
#     print(x.text)


# import requests
# from bs4 import BeautifulSoup
# def get_info(url):
#     u = 'https://www.makers.kg'
#     source = requests.get(u).text
#     soup = BeautifulSoup(source, 'lxml')
#     name = [x.h3.text for x in soup.find_all('div', 'feature-cards-card-wrapper')]
#     description = [x.text for x in soup.find_all('div', 'feature-cards-card-info-subtitle')]
#     image_link = [u + x['src'][1:] for x in soup.find_all('img', 'feature-cards-card-image')]
#     res = []
#     count = 0
#     for x in name:
#         dict_ = {'name': name[count], 'description': description[count], 'image_link': image_link[count]}
#         res.append(dict_)
#         count += 1
#     return res
# print(get_info('https://www.makers.kg'))



# Task 9

# import re
# import requests
# from bs4 import BeautifulSoup as bs
# source = requests.get('https://enter.kg/').text
# soup = bs(source, 'lxml')
# ul_html = soup.find('div', {'id':'main'}).find_all('a')
# category_list = [a.get_text(strip=True) for a in ul_html]
# def find_category(categories, keyword):
#     res = []
#     for x in categories:
#         if re.search(keyword, x, re.IGNORECASE):
#             res.append(x)
#     return res
# print(find_category(category_list, 'Ноутбуки'))


# task10
# import re
# import requests
# from bs4 import BeautifulSoup as bs
# source = requests.get('https://www.imdb.com/chart/top').text
# soup = bs(source, 'lxml')
# title_list = soup.find_all('td', {'class':'titleColumn'})
# def get_link(title_list, name):
#     res = 'https://www.imdb.com'
#     for x in title_list:
#         if re.search(name, x.get_text(strip=True), re.IGNORECASE):
#             res += x.find('a').get('href')
#             break
#     return res
# print(get_link(title_list, 'pulp'))


