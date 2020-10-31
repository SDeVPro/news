from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='index'),
    path('addtofavorite/<int:id>', views.addtofavorite, name='addtofavorite'),
    path('deletefav/<int:id>',views.deletefav, name='deletefav'),
]