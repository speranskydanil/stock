from django.contrib import admin

from blog.models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'author', 'verified')
    list_filter = ['publication_date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)

