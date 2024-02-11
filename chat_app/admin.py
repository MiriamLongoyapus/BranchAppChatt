# admin.py

from django.contrib import admin
from .models import User, Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'message_content', 'timestamp')
    search_fields = ('sender', 'message_content')
    list_filter = ('timestamp','sender')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name','last_name','is_agent','is_customer')
    search_fields = ('username',)
    list_filter = ('is_agent','is_customer')

admin.site.register(User, UserAdmin)
admin.site.register(Message, MessageAdmin)

