from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    about = models.TextField()
    contact = models.TextField()
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

