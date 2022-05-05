
# klass metody, statik metody i instans metody

# class A:
#     a = "Class var"  # peremennye klassa 
#     def __init__(self, b) -> None:
#         self.b = "Instance Var"  # peremennye obiekta


# print(A.a)
# print(A().b)



# class SomeClass:

#     def __init__(self, a, b) -> None:
#         self.a = a 
#         self.b = b 
#     def func(self):
#         pass

#     @classmethod
#     def func_two(cls):
#         pass

#     @staticmethod
#     def func_three():
#         pass

# # SomeClass().func_three()

# DELIVERY_PRICE = 120 

# class Order:
#     orders = []
#     def __init__(self, name, address, product, price, count) -> None:
#         self.name = name
#         self.address = address
#         self.product = product
#         self.price = price
#         self.count = count 

#     def create_order(self):
#         order = {
#                 "name": self.name, 
#                 "address": self.address,
#                 "product": self.product,
#                 "price": self.price,
#                 "count": self.count,
#                 "delivery": self.set_delivery(self.count, DELIVERY_PRICE)
#                 }
#         self.orders.append(order)
#     @staticmethod
#     def set_delivery(count, price):
#         return price * count / 2

# order1 = Order("john", "California", "IceCream", 250, 5)

# order2 = Order("Raychel", "LA", "IceCream", 250, 10)

# order1.create_order()
# print(order1.orders)

# order2.create_order()
# print(order2.orders)

# print(Order.orders)



# class Parser():
#     def parse_image(self.html):
#         soup = BeautifulSoup(html, "html.parser")
#         return soup.find("image")

#     def parser_data(self):

#         {
#             "image": self.parse_image()
#         }



# class Pizza:
#     def __init__(self, name, radius, *ingredients) -> None:
#         self.name = name
#         self.ingredients = ingredients
#         self.radius = radius
#         self.create_pizza()

#     def create_pizza(self):
#         print(f"Created Pizza -> {self.name} with radius {self.radius} ingredients {self.ingredients}")

#     @classmethod
#     def create_pepperoni(cls, radius):
#         name = "Pepperoni"
#         ingredients = ("suasage", "chees", "dough", "origano")
#         return cls(name, radius, *ingredients)

#     @classmethod
#     def create_margarita(cls, radius):
#         name = "Margarita"
#         ingredients = ("pomidor", "chees", "dough", "origano")
#         return cls(name, radius, *ingredients)

#     @classmethod
#     def create_four_chees(cls, radius):
#         name = "Four Cheese"
#         ingredients = ("cheese another", "chees", "dough", "origano")
#         return cls(name, radius, *ingredients)


# Pizza.create_pepperoni(30)
# Pizza.create_margarita(40)
# Pizza.create_four_chees(50)






