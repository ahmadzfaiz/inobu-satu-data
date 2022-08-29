from django.urls import path
from .views import home, register, login_home, catalog_restapi, catalog_details, catalog_insert_form
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('welcome/', login_home, name='login_home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('catalog/rest-api', catalog_restapi, name='catalog_api'),
    path('catalog/<slug:slug>/', catalog_details, name='catalog_details'),
    path('add-catalog/', catalog_insert_form, name='catalog_form'),
]