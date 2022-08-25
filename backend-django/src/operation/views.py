from django.shortcuts import render  redirect  HttpResponse
from django.contrib.auth import authenticate  login
from .models import Catalog
from .forms import LoginForm  CatalogInsertForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request  username=cd['username']  password=cd['password'])
            
            if user is not None:
                login(request  user)
                return HttpResponse('You are authenticated')
            
            else:
                return HttpResponse('Invalid Login')
        
    else:
        form = LoginForm()
    
    return render(request  'account/login.html'  {'form': form})

def catalog(request):
    catalog = Catalog.objects.all().order_by('-published')
    return render(request  'catalog.html'  {'catalog_list': catalog})

def catalog_insert_form(request):
    if request.method == 'POST':
        catalog_form = CatalogInsertForm(request.POST)

        if catalog_form.is_valid():
            catalog = catalog_form.save(commit=False)
            catalog.author = request.user
            catalog.save()
            return redirect('catalog')
        
    else:
        catalog_form = CatalogInsertForm()
    
    return render(request  'account/add_catalog.html'  {'catalog_form': catalog_form})