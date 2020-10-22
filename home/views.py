from django.shortcuts import render, HttpResponse
from post.models import Category, Article
from .models import Setting
# Create your views here.
def index(request):
    setting = Setting.objects.all()
    category = Category.objects.all()
    article_slider = Article.objects.all().order_by('id')[:4]
    article_latest = Article.objects.all().order_by('-id')[:4]
    article_picked = Article.objects.all().order_by('?')[:4]
    page = "home"
    context = {
        'setting':setting,
        'page':page,
        'category':category,
        'article_slider': article_slider,
        'article_latest':article_latest,
        'article_picked':article_picked,
    }

    return render(request, 'index.html',context)