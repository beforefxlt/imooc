from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all()  # all方法返回的就是一个集合对象 ,可以理解成列表
    return render(request, 'blgo2/index.html', {'hello': articles})


def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'blgo2/article_page.html', {'hello': article})
