# from scraping_page_enter import get_all_links, BASE_URL
# from scraping_details_enter import get_item_details
# import json

# def main():
#     products = []

#     # получаем ссылки на все продукты со всех страниц
#     all_products_links = get_all_links()

#     for product_url in all_products_links:
#         # получаем данные по каждому продукту и добавляем в список
#         product_details = get_item_details(BASE_URL + product_url)
#         products.append(product_details)

#     with open("db.json", "w", encoding='utf-8') as file:
#         # записываем полученный список с информацией о продуктах в файл
#         json.dump(products, file, ensure_ascii=False)

# if __name__ == '__main__':
#     main()