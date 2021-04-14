from django.shortcuts import render
from .models import Article

def show_home(request):
    article_list = Article.objects.all()
    context = {'article_list': article_list}
    return render(request, 'home.html', context)