from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from .models import Catalog, Tag, Dashboard, Document
from .forms import *
from rest_framework.authtoken.models import Token


# BASIC VIEW
def home(request):
    return render(request, 'home.html')

@login_required
def login_home(request):
    return render(request, 'login_home.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            
            if user is not None:
                login(request, user)
                return HttpResponse('You are authenticated')
            
            else:
                return HttpResponse('Invalid Login')
        
    else:
        form = LoginForm()
    
    return render(request, 'account/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'user_form': user_form})

    else: 
        user_form = UserRegistration()

    return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def my_profile(request):   
    username = request.user
    full_name = request.user.get_full_name()
    try:
        auth = Token.objects.get(user_id=username.id)
    except Token.DoesNotExist:
        auth = None
    
    return render(request, 'account/profile_details.html', {'username': username, 'full_name': full_name, 'auth': auth})


# CATALOG REST API VIEW
@login_required
@permission_required(['operation.view_catalog'])
def catalog_restapi(request):
    if 'q' in request.GET:
        q = request.GET['q']
        catalog = Catalog.objects.filter(title__icontains=q).order_by('-published')

    else:
        catalog = Catalog.objects.all().order_by('-published')

    return render(request, 'catalog/catalog_restapi.html', {'catalog_list': catalog})

# @permission_required(['operation.add_catalog'])
@login_required
def catalog_insert_form(request):
    if request.method == 'POST':
        catalog_form = CatalogInsertForm(request.POST)

        if catalog_form.is_valid():
            catalog = catalog_form.save(commit=False)
            catalog.author = request.user
            catalog.save()
            catalog_form.save_m2m()
            return redirect('catalog_api')
        
    else:
        catalog_form = CatalogInsertForm()
    
    return render(request, 'catalog/catalog_restapi_add.html', {'catalog_form': catalog_form})

@login_required
def catalog_update_form(request, slug):
    catalog = get_object_or_404(Catalog, slug=slug)
    form = CatalogUpdateForm(request.POST or None, instance=catalog)

    if form.is_valid():
        form.save()
        return redirect('catalog_api')

    return render(request, 'catalog/catalog_restapi_update.html', {'form':form})

@login_required
def catalog_delete_form(request, slug):
    catalog = get_object_or_404(Catalog, slug=slug)
    catalog.delete()
    return redirect('catalog_api')

@login_required
def catalog_details(request, slug):
    catalog = get_object_or_404(Catalog, slug=slug)
    return render(request, 'catalog/catalog_restapi_details.html', {'catalog': catalog})

@login_required
def catalog_insert_tag(request):
    tag_list = Tag.objects.all()

    if request.method == 'POST':
        tag = CatalogInsertTag(request.POST)

        if tag.is_valid():
            tag.save()
            return redirect('home')
        
    else:
        tag = CatalogInsertTag()
    
    return render(request, 'catalog/catalog_restapi_tag.html', {'tag': tag, 'tag_list': tag_list})


# PRODUCT DASHBOARD VIEW
@login_required
def product_dashboard(request):
    if 'q' in request.GET:
        q = request.GET['q']
        dashboard = Dashboard.objects.filter(title__icontains=q).order_by('-published')
    
    else:
        dashboard = Dashboard.objects.all().order_by('-published')

    return render(request, 'product/dashboard.html', {'dashboard': dashboard})

@login_required
def product_dashboard_details(request, slug):
    dashboard = get_object_or_404(Dashboard, slug=slug)
    return render(request, 'product/dashboard_details.html', {'dashboard': dashboard})

@login_required
def dashboard_insert_form(request):
    if request.method == 'POST':
        dashboard_form = DashboardInsertForm(request.POST)

        if dashboard_form.is_valid():
            dashboard = dashboard_form.save(commit=False)
            dashboard.author = request.user
            dashboard.save()
            dashboard_form.save_m2m()
            return redirect('product_dashboard')
        
    else:
        dashboard_form = DashboardInsertForm()
    
    return render(request, 'product/dashboard_add.html', {'dashboard_form': dashboard_form})

@login_required
def dashboard_update_form(request, slug):
    dashboard = get_object_or_404(Dashboard, slug=slug)
    form = DashboardUpdateForm(request.POST or None, instance=dashboard)

    if form.is_valid():
        form.save()
        return redirect('product_dashboard')

    return render(request, 'product/dashboard_update.html', {'form':form})

@login_required
def dashboard_delete_form(request, slug):
    dashboard = get_object_or_404(Dashboard, slug=slug)
    dashboard.delete()
    return redirect('product_dashboard')

# PRODUCT DOCUMENT VIEW
@login_required
def product_document(request):
    if 'q' in request.GET:
        q = request.GET['q']
        document = Document.objects.filter(title__icontains=q).order_by('-published')

    else:
        document = Document.objects.all().order_by('-published')
        
    return render(request, 'product/document.html', {'document': document})

@login_required
def product_document_details(request, slug):
    document = get_object_or_404(Document, slug=slug)
    return render(request, 'product/document_details.html', {'document': document})

@login_required
def document_insert_form(request):
    if request.method == 'POST':
        document_form = DocumentInsertForm(request.POST)

        if document_form.is_valid():
            document = document_form.save(commit=False)
            document.author = request.user
            document.save()
            document_form.save_m2m()
            return redirect('product_document')
        
    else:
        document_form = DocumentInsertForm()
    
    return render(request, 'product/document_add.html', {'document_form': document_form})

@login_required
def document_update_form(request, slug):
    document = get_object_or_404(Document, slug=slug)
    form = DocumentUpdateForm(request.POST or None, instance=document)

    if form.is_valid():
        form.save()
        return redirect('product_document')

    return render(request, 'product/document_update.html', {'form':form})

@login_required
def document_delete_form(request, slug):
    document = get_object_or_404(Document, slug=slug)
    document.delete()
    return redirect('product_document')

# DOCUMENTATION VIEW
@login_required
def documentation(request):
    docs = Dashboard.objects.all().order_by('-published')
    return render(request, 'documentation/home.html', {'docs': docs})