from django.contrib import admin
from blog_admin.models import Blog_Admin,Record_myself,My_Music,SongType
# Register your models here.
admin.site.register(Blog_Admin)
admin.site.register(Record_myself)
admin.site.register(My_Music)
admin.site.register(SongType)