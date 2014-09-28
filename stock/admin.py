from django.contrib import admin

from stock.models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message', 'created_at')
    list_filter = ['created_at']

admin.site.register(Message, MessageAdmin)

