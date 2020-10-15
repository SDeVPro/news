from django.contrib import admin
from home.models import Setting

# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','create_at']
admin.site.register(Setting, SettingAdmin)