from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse

# Create your views here.
from post.models import CommentForm, Comment


def index(request):
    return HttpResponse("Post app")


def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.article_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request, "Sizning kommentariyangiz qo'shildi!")
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)