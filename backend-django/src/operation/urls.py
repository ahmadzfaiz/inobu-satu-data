from django.urls import path
from .views import catalog  catalog_insert_form
from django.contrib.auth.views import LoginView  LogoutView

urlpatterns = [
    path('login/'  LoginView.as_view()  name='login') 
    path('logout/'  LogoutView.as_view()  name='logout') 
    # path('register/'  register  name='register') 
    path('catalog/'  catalog  name='catalog_list') 
    path('add-catalog/'  catalog_insert_form  name='catalog_form') 
]