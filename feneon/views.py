from django.shortcuts import render
from .models import NewsItem

def home(request):
    news_items = NewsItem.objects.all()
    return render(request, 'feneon/home.html', {'news_items': news_items})


# Create your views here.
