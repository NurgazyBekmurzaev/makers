# import requests
# from bs4 import BeautifulSoup
# import csv

# URL = 'https://www.mashina.kg/search/porsche/panamera/?currency=2&sort_by=upped_at%20desc&time_created=all'
# url = 'https://www.mashina.kg'


# def get_soup(URL):
#     response = requests.get(URL)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     return soup


# def get_every_element():
#     soup = get_soup(URL)
#     links = []
#     divs = soup.find_all('div', attrs ={'class':'list-item list-label'})
#     for div in divs:
#         a = div.find("a").get(("href"))
#         links.append(a)
#     return links
  

# def get_one_link():
#     every_element = get_every_element()
#     html1 = ''
#     count = 0
#     for every in every_element:
#         full_every = url + every
#         response = requests.get(full_every)
#         html1 += response.text
#         count += 1
#         print(count)
#     return html1


# def img_title_price():
#     all_html = get_one_link()
#     soup = BeautifulSoup(all_html, 'html.parser')


#     all_name = []
#     name  = soup.find_all('div', attrs = {'class': 'head-left clr'})
#     for nm in name:
#         res1 = nm.find("h1").text
#         all_name.append(res1)
    

#     all_price = []
#     prices = soup.find_all("div", attrs = {"class":"price-types"})
#     for prc in prices:
#         res = prc.find("h2").text
#         all_price.append(res)


#     all_imgs = []
#     imgs = soup.find_all("div", attrs = {"class": "right-side image-content"})
#     for img in imgs:
#         res_img = img.find("a").get(("href"))
#         all_imgs.append(res_img)


#     all_comments = []
#     new_comment = soup.find_all('div', attrs = {'class': 'seller-comments'})
#     for cmmt in new_comment:
#         res2 = cmmt.find("h2", attrs = {'class': 'comment'}).text
#         all_comments.append(res2)
 

#     return (all_imgs, all_price, all_name, all_comments)


  


# print(img_title_price())






