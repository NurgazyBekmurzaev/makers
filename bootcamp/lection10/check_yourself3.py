# """
# 1)	В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.
# """

# with open('kakoito.txt', 'r') as f:
#     len_ = f.readlines()
#     print(f'{len(len_)} - kol-vo' )
#     count = 1
    
#     for x in len_:
#         delate =x.rstrip('\n')

#         bukvy = 0
#         znaki = 0

#         for i in delate.lower():
            
#             if i in 'qwertyuiopasdfghjklzxcvbnm':
#                 bukvy += 1
#             else:
#                 znaki += 1
#         print(f'{bukvy} и {znaki} - bukvy i simvoly v {count} stroke')
#         count  += 1

# 2)	Спарсить vesti.kg только названия новостей(title) и записать результат в csv файл
# """

# import requests
# from bs4 import BeautifulSoup
# import csv

# URL = 'https://www.vesti.kg/politika.html'

# url = 'https://www.vesti.kg'


# def get_soup(URL):
#     response = requests.get(URL)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     return soup

# def write_to_csv(data):
#     print(data)
#     with open('Hackatoon1.csv', 'a') as h1_csv:
#         writer = csv.writer(h1_csv, delimiter=',')
#         writer.writerow((data))



# def get_one_link():
#     every_element = ttls_vesti()
#     html1 = ''
#     count = 0
#     for every in every_element:
#         full_every = url + every
#         response = requests.get(full_every)
#         html1 += response.text
#         count += 1
#         print(count)
#     return html1


# # def get_every_element():
# #     soup = get_soup(URL)
# #     links = []
# #     divs = soup.find_all('div', attrs ={'class':'itemContainer itemContainerLast'})
# #     for div in divs:
# #         a = div.find("a").text
# #         links.append(a)
# #     return links
  


# def ttls_vesti():
#     all_html = get_one_link()
#     soup = BeautifulSoup(all_html, 'html.parser')

#     all_ttls = []
#     ttls = soup.find_all("div", attrs = {"class": "itemList"})
#     for ttl in ttls:
#         res_ttl = ttl.find("a").text
#         all_ttls.append(res_ttl) 

#     return list(zip(all_ttls))


# def main():
#     open('Checkyourself4.csv', 'w').close()
#     all_ttls = ttls_vesti()
#     for data in all_ttls:
#         write_to_csv(data)
#         return all_ttls

# print(main())



# Checkyourself_3 Uluk


# import requests
# from bs4 import BeautifulSoup as BS
# import csv


# base_url = 'https://vesti.kg/'


# def get_soup(url):
#     response = requests.get(url).text
#     soup = BS(response, 'html.parser')
#     return soup

# def get_title():
#     soup = get_soup(base_url)
#     res = soup.find_all('div', class_="itemBody")
#     list_ = [x.find('a').text for x in res]
#     return list_
    

# data = get_title()
# print(data)

# with open('Check_yourself3.csv', "w", newline="") as file:
#     writer = csv.writer(file, delimiter=' ',
#     quotechar=',', quoting=csv.QUOTE_MINIMAL)
#     writer.writerows(data)




