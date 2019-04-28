from django.contrib import admin
from blog_message.models import Blog_Message,User_Message
# Register your models here.
admin.site.register(Blog_Message)
admin.site.register(User_Message)