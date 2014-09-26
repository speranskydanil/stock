from django.contrib import admin

from blog.models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article)

