from django.contrib import admin
from home.models import Setting, ContactMessage, Favorite

# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','create_at']
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user','article']
    list_filter = ['user']
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject','email','ip']
    readonly_fields = ('name','subject', 'email','message','ip')
    list_filter = ['status']
admin.site.register(Setting, SettingAdmin)
admin.site.register(Favorite,FavoriteAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)