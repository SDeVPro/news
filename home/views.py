import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from post.models import Category, Article, Images, Comment
from .models import Setting, ContactForm, ContactMessage, Favorite, FavoriteForm
from django import forms

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


def about(request):
    setting = Setting.objects.all()
    category = Category.objects.all()
    context = {
        'setting':setting,
        'category':category,
    }
    return render(request, 'about.html',context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name =form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Sizning xabaringiz yuborildi!")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.all()
    form = ContactForm
    category = Category.objects.all()
    context = {
            'setting':setting, 'form':form, 'category':category,
        }
    return render(request, 'contact.html',context)


def category_article(request,id,slug):
    category = Category.objects.all()
    catdata = Category.objects.get(pk=id)
    post = Article.objects.filter(category_id=id)
    context = {
        'category':category,
        'catdata':catdata,
        'post':post,
    }
    return render(request,'catefory_article.html',context)

def post_detail(request, id, slug):
    category = Category.objects.all()
    post = Article.objects.get(pk=id)
    comments = Comment.objects.filter(article_id=id)
    images = Images.objects.filter(article_id=id)
    context = {
        'category':category,
        'post':post,
        'images':images,
        'comments':comments,
    }
    return render(request, 'article_detail.html', context)
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    catid = forms.IntegerField()
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                articles = Article.objects.filter(title__icontains=query)
            else:
                articles = Article.objects.filter(title__icontains=query, category_id=catid)

            category = Category.objects.all()
            context = {
                'articles':articles,
                'category':category,
                'query':query,
            }
            return render(request, 'search.html',context)
    return HttpResponseRedirect('/')

def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term','')
        articles = Article.objects.filter(title__icontains=q)
        results = []
        for rs in articles:
            articles_json = {}
            articles_json = rs.title
            results.append(articles_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return  HttpResponse(data,mimetype)


def addtofavorite(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    check = Favorite.objects.filter(article_id=id)
    if check:
        control = 1
    else:
        control = 0
    if request.method == 'POST':
        form = FavoriteForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = Favorite.objects.get(article_id=id)
                data.save()
            else:
                data = Favorite()
                data.user_id = current_user.id
                data.article_id = id
                data.save()
        messages.success(request,"Article added to Favourite")
        return HttpResponseRedirect(url)
    else:
        if control == 1:
            data = Favorite.objects.get(article_id=id)
            data.save()
        else:
            data = Favorite()
            data.user_id = current_user.id
            data.article_id = id
            data.save()
        messages.success(request,"Article added to Favourite")
        return HttpResponseRedirect(url)

@login_required(login_url='login')
def deletefav(request,id):
    Favorite.objects.filter(id=id).delete()
    messages.success(request,"Your item deleted!")
    return HttpResponseRedirect('/favorite')


def favorite(request):
    category = Category.objects.all()
    current_user = request.user
    favorite = Favorite.objects.filter(user_id=current_user.id)
    context = {
        'category':category,
        'favorite':favorite,
    }
    return render(request,'favorite.html',context)
