from django.urls import path, re_path, include
from .views import home, register, login_home, catalog_restapi, catalog_details, catalog_insert_form, catalog_update_form, catalog_delete_form, catalog_insert_tag
from django.contrib.auth.views import LoginView, LogoutView
import django_sql_dashboard

urlpatterns = [
    path('', home, name='home'),
    path('welcome/', login_home, name='login_home'),
    path('welcome/login/', LoginView.as_view(), name='login'),
    path('welcome/logout/', LogoutView.as_view(), name='logout'),
    path('welcome/register/', register, name='register'),
    path('catalog/rest-api', catalog_restapi, name='catalog_api'),
    path('catalog/<slug:slug>/', catalog_details, name='catalog_details'),
    path('add-catalog/', catalog_insert_form, name='catalog_form'),
    path('update-catalog/<slug:slug>/', catalog_update_form, name='catalog_update_form'),
    path('delete-catalog/<slug:slug>/', catalog_delete_form, name='catalog_delete_form'),
    path('add-tag/', catalog_insert_tag, name='catalog_tag'),
    path("sql-query/", include(django_sql_dashboard.urls)),
]