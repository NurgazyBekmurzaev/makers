# import requests
# from bs4 import BeautifulSoup as BS

# base_url = 'https://24.kg'

# def get_soup(url):
#     if url.startswith("https:"):
#         html = requests.get(url).text
#     else:
#         html = requests.get(base_url + url).text

#     soup = BS(html, "html.parser")
#     return soup

# def get_categories():
#     soup = get_soup(base_url)
#     cat_block = soup.find('ul', {"class": "navbar-nav"})
#     a_tags = cat_block.find_all("a")
#     return [tag.get("href") for tag in a_tags]

# def get_news_title(cat_url):
#     soup = get_soup(cat_url)
#     title_divs = soup.find_all("div", {"class": "one"})
#     return [div.find("a").get("href") for div in title_divs]

# def get_news_article(news_url):
#     soup = get_soup(news_url)
#     article_block = soup.find("div", {"itemprop": "articleBody"})
#     if article_block:
#         return article_block.text
    
# def main():
#     all_news = []
#     # poluchaem spisok s ssylkami na vse kategorii
#     categories_urls = get_categories()
#     # prohodimsya po kajdoi ssylke
#     for category_url in categories_urls:
#         print(category_url)
#         # poluchaem vse zagolovki po dannoi kategorii
#         news_url = get_news_title(category_url)
#         # poluchaem teks odnoi novosti
#         for n_url in news_url:
#             res_text = get_news_article(n_url)
#             all_news.append(res_text)

#     return all_news
# print(main())


