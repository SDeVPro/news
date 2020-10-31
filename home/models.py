from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from post.models import Article


class Setting(models.Model):
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    about = RichTextUploadingField()
    contact = RichTextUploadingField()
    icon = models.ImageField(upload_to='images/', blank=True)
    facebook = models.EmailField(max_length=255, blank=True)
    instagram = models.EmailField(max_length=255, blank=True)
    telegram = models.EmailField(max_length=255, blank=True)
    youtube =  models.EmailField(max_length=255, blank=True)
    twitter = models.EmailField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('Read', 'Uqilgan'),
        ('Closed', 'Yopilgan'),
    )
    name = models.CharField(blank=True, max_length=222)
    email = models.CharField(blank=True, max_length=222)
    subject = models.TextField(blank=True, max_length=255)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=15, default='New', choices=STATUS)
    ip = models.CharField(max_length=155, blank=True)
    note = models.CharField(max_length=155, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','subject', 'message']
        widgets = {
            'name':TextInput(attrs={'class':'input', 'placeholder':'Name'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your message', 'rows':'5'}),
        }

class Favorite(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    article = models.ForeignKey(Article,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.article.title

class FavoriteForm(ModelForm):
    model = Favorite
    fields = ['title','rate']