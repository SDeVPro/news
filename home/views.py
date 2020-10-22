from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from post.models import Category, Article
from .models import Setting, ContactForm, ContactMessage


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