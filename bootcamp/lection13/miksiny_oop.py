
#  Mixins - Primesi 

# v konce nazvanie hranit Mixin  

# PostMixin 

# ne doljen hranit sostoyanie 


# class CreateMixin:
#     def create(self):
#         print("Create")

# class UpdateMixin:
#     def update(self):
#         print("Update")

# class DeleteMixin:
#     def delete(self):
#         print("Delete")

# class CreateRestoran(CreateMixin,
#                     UpdateMixin,
#                     DeleteMixin):
#     def __init__(self, name, address) -> None:
#         self.name = name
#         self.address = address

#     def create_retoran(self):
#             self.create()



# from multiprocessing import AuthenticationError


# users = {
#         "user1": 123,
#         "user2": 321
# }

# def login_required(func):
#     def wrapper(user):
#         print(user)
#         if user not in users.values:
#             raise AuthenticationError("User is not Authenticated")
#         func(user)
#         print("Uspeshno avtorizovan")
#         return

#     return wrapper
# @login_required
# def some_page(user):
#     pass

# some_page(user="john")

# from multiprocessing import AuthenticationError


# class View():
#     def __init__(self) -> None:
#         self.users = ["john", "Raychel"]

#     # def dispatch(self):
#     #     print("Metod dispatch")
#     #     self.users


# class LoginRequiredMixin:
#     def dispatch(self, request, user):
#         if user not in self.users:
#             raise AuthenticationError("User is not Authenticated")
#         return self.users

# class AboutPage(View, LoginRequiredMixin):
#     pass

# obj = AboutPage()
# obj.dispatch("test", "john")







