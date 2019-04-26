from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from blog_user.models import Blog_User
from blog_block.models import Blog_Block
from blog_subject.models import Blog_Subject
from blog_message.models import Blog_Message,User_Message
from django.core import serializers
from django.db.models import Q
import datetime,random,json,collections
from django.utils import timezone

# Create your views here.

# 添加回复
def messageadd(request):
    username = request.session.get('name')
    if not username:
        return JsonResponse({'status':'error'})
    if request.method == 'POST':
        Blog_Message.objects.create(
            message=request.POST['user_message'],
            subject=Blog_Subject.objects.filter(id=request.POST['subject_id']).first(),
            user=Blog_User.objects.filter(name=request.session['name']).first()
        )
        return JsonResponse({'status':'ok'})
        

# 查看主题回复
def show_message(request,subject_id):
    ok = Blog_Message.objects.filter(subject=subject_id).order_by('-message_create_date')
    message = render(request,'message/message.html',{'message':ok})
    return message

# 删除回复
def messagedel(request,subject_id,message_id):
    Blog_Message.objects.filter(id=message_id).delete()
    return show_message(request,subject_id)

# 查看用户留言
def show_usermes(request):
    comment_dic = collections.OrderedDict()
    usermes = User_Message.objects.all()
    for i in usermes:
        if i.fu_mes == 0:
            print(i.create_time)
            mesdate = timezone.localtime(i.create_time).strftime("%Y-%m-%d %H:%M")
            comment_dic[i.id,i.nicheng,i.usermes,mesdate,i.fu_mes] = collections.OrderedDict()
        else:
            tree_search(comment_dic, i)
    # print(comment_dic)
    return render(request,'message/usermes_list.html',{'comment_dic':comment_dic})

def tree_search(comment_dic, comment_obj):
    for k,j in comment_dic.items():
        # print(k)
        if k[0] == comment_obj.fu_mes:
            mesdate = timezone.localtime(comment_obj.create_time).strftime("%Y-%m-%d %H:%M")
            comment_dic[k][comment_obj.id,comment_obj.nicheng,comment_obj.usermes,mesdate,comment_obj.fu_mes] = collections.OrderedDict()
            return
        else:
            tree_search(comment_dic[k], comment_obj)
