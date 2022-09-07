from django.shortcuts import render
from api.models import Article

# Create your views here.
def home(request):
    data = Article.objects.all()    
    return render(request, 'editor/home.html', {'article': data})