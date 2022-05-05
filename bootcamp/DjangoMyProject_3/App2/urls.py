
from django.urls import path
from . import views
urlpatterns = [
    path('main', views.get_main, name='main'),
    path('', views.get_index, name='index')
    ]