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
    from django.core.paginator import Paginator,PageNotAnInteger,InvalidPage,EmptyPage
    ok = Blog_Message.objects.filter(subject=subject_id)
    subjectmes = []
    for index,value in enumerate(ok,1):
        subjectmes.append((index,value))
    paginator = Paginator(list(reversed(subjectmes)),5)
    page_range=[]
    page = request.GET.get('page')
    try:
        conttacts = paginator.get_page(page)
        if paginator.num_pages > 5:
            page_range = range(1,6)
            print(page)
            if page != 'undefined':
                page = int(page)
                if page > 3 and page < paginator.num_pages+1:
                    if page+2 < paginator.num_pages:
                        page_range = range(page-2,page+3)
                    elif page+2 >= paginator.num_pages:
                        page_range = range(paginator.num_pages-4,paginator.num_pages+1)
        else:
            page_range = paginator.page_range
    except PageNotAnInteger:
        conttacts = paginator.get_page(1)
    except InvalidPage:
        return HttpResponse("找不到页面内容")
    except EmptyPage:
        conttacts = paginator.get_page(paginator.num_pages)
    message = render(request,'message/message.html',{'message':conttacts,'page_range':page_range})
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
