from django.contrib import admin
from post.models import Category, Article, Images

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_at']
    list_filter = ['title']
class ArticleImageInline(admin.TabularInline):
    model = Images
    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image']
    list_filter = ['title']
    readonly_fields = ('image_tag',)
    inlines = [ArticleImageInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Images)