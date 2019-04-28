"""wcz_boke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog_admin import views as admin_views
from blog_user import views as user_views
from blog_block import views as block_views
from blog_subject import views as subject_views
from blog_message import views as message_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.index, name='home'),
    path('useradd/', user_views.useradd, name='useradd'),
    path('yzm/', user_views.yzm, name='yzm'),
    path('userlogin/', user_views.userlogin, name='userlogin'),
    path('userlogout/', user_views.userlogout, name='userlogout'),
    path('create/subject/',user_views.create_subject,name="create_subject"),  
    path('check/username/<str:username>/',user_views.check_username,name="check_username"),  
    path('send/email/',user_views.send_email,name="send_email"),  
    path('check/email/<str:emailyzm>/',user_views.check_email,name="check_email"),  
    path('check/yzm/<str:yzm>/',user_views.check_yzm,name="check_yzm"),  
    path('reset/userpwd/',user_views.reset_pwd,name="reset_pwd"),  
    path('set/userpwd/<str:status>/',user_views.set_pwd,name="set_pwd"),  
    path('date/save/',user_views.save_date,name="save_date"),  
    path('subject/type/',user_views.subject_type,name="subject_type"),  
    path('add/subject/',subject_views.subjectadd,name="subjectadd"),
    path('show/subject/<str:id>/',subject_views.show_subject,name="show_subject"),
    path('add/message/',message_views.messageadd,name="messageadd"),
    path('del/message/<str:subject_id>/<str:message_id>/',message_views.messagedel,name="messagedel"),
    path('user/search/',user_views.user_search,name="user_search"),
    path('nav/',user_views.nav_bar,name="nav_bar"),
    path('save/img/',subject_views.img_save,name="img_save"),
    path('newest_subject/',user_views.newest_subject,name="newest_subject"),
    path('show_subject/message/<str:subject_id>/',message_views.show_message,name="show_message"),
    path('recordmy/',admin_views.record_myself,name="recordmy"),
    path('myself/',admin_views.myself,name="myself"),
    path('study_back/',user_views.study_back,name="study_back"),
    path('music/',user_views.music,name="music"),
    path('usermes/',user_views.usermes,name="usermes"),
    path('show/usermes/',message_views.show_usermes,name="show_usermes"),
    path('show/myself/',admin_views.show_record_myself,name="show_record_myself"),
    path('bottomlist/',user_views.lastjz,name="lastjz"),
]
