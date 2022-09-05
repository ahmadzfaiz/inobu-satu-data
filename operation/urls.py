from django.urls import path, re_path, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
import django_sql_dashboard
from django_sql_dashboard.views import SaveDashboardForm

urlpatterns = [
    path('', home, name='home'),

    # account management
    path('welcome/', login_home, name='login_home'),
    path('welcome/login/', LoginView.as_view(), name='login'),
    path('welcome/logout/', LogoutView.as_view(), name='logout'),
    path('welcome/register/', register, name='register'),
    path('account/', my_profile, name='my_profile'),
    path('account/change-password/', PasswordChangeView.as_view(), name='password_change'),
    path('account/change-password/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    # catalog data
    path('catalog/rest-api', catalog_restapi, name='catalog_api'),
    path('catalog/<slug:slug>/', catalog_details, name='catalog_details'),
    path('add-catalog/', catalog_insert_form, name='catalog_form'),
    path('update-catalog/<slug:slug>/', catalog_update_form, name='catalog_update_form'),
    path('delete-catalog/<slug:slug>/', catalog_delete_form, name='catalog_delete_form'),
    path('add-tag/', catalog_insert_tag, name='catalog_tag'),
    path("sql-query/", include(django_sql_dashboard.urls)),

    # product data - dashboard
    path('product/dashboard/', product_dashboard, name='product_dashboard'),
    path('product/dashboard/<slug:slug>/', product_dashboard_details, name='product_dashboard_details'),
    path('product/add-dashboard/', dashboard_insert_form, name='dashboard_add_form'),
    path('product/dashboard/update/<slug:slug>/', dashboard_update_form, name='dashboard_update_form'),
    path('product/dashboard/delete/<slug:slug>/', dashboard_delete_form, name='dashboard_delete_form'),

    # product data - document
    path('product/document/', product_document, name='product_document'),
    path('product/document/<slug:slug>/', product_document_details, name='product_document_details'),
    path('product/add-document/', document_insert_form, name='document_add_form'),
    path('product/document/update/<slug:slug>/', document_update_form, name='document_update_form'),
    path('product/document/delete/<slug:slug>/', document_delete_form, name='document_delete_form'),

    # documentation
    path('docs/', documentation, name='docs'),
]