from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from post.models import Article,Category, Comment
from user.models import UserProfile
from user.forms import SignUpForm,UserUpdateForm,ProfileUpdate
from home.models import Favorite
# Create your views here.
@login_required(login_url='/login')
def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id = current_user.id)
    context = {
        'category':category,
        'profile':profile,
    }
    return render(request,'userprofile.html',context)

def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage']=userprofile.image.url
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"Login error! Username or Password is incorrect")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    context = {'category':category,}
    return render(request,'login_form.html',context)
def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request,user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request,'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')
    form = SignUpForm()
    category = Category.objects.all()
    context = {'category':category,
               'form':form,
               }
    return render(request,'signup_form.html',context)
def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdate(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Your account has been updated!")
            return HttpResponseRedirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdate(instance=request.user.userprofile)
        context = {
                'category': category,
                'user_form':user_form,
                'profile_form': profile_form,
            }
        return render(request,'user_update.html',context)

@login_required(login_url='/login')
def user_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Your password was succesfully updated!")
        else:
            messages.error(request,"Please correct the error below.<br>"+str(form.errors))
            return HttpResponseRedirect('user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request,'user_password.html',{'form':form,'category':category})


@login_required(login_url='/login')
def user_comments(request):
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id = current_user.id)
    context = {'category':category,
               'comments':comments,
               }
    return render(request,'user_comments.html',context)

@login_required(login_url='/login')
def deletecomments(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request,'Comment deleted!')
    return HttpResponseRedirect('/user/comments')


def favourite(request):
    category = Category.objects.all()
    current_user = request.user
    fav = Favorite.objects.filter(user_id=current_user.id).order_by('-id')
    context = {
        'category':category,
        'fav':fav,
    }
    return render(request,'user_favourite.html',context)