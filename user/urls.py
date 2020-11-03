from django.urls import path
from user import views
urlpatterns = [
    path('', views.index, name='index'),
    path('update/',views.user_update, name='user_update'),
    path('password/',views.user_password,name='user_password'),
    path('comments/',views.user_comments,name='user_comments'),
    path('deletecomments/<int:id>/', views.deletecomments,name='deletecomments'),
    path('favourite/',views.favourite,name='favourite'),

]