from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from blog_admin.models import Record_myself
# Create your views here.

def hello(request):
    # 22=a
    return render(request, 'blogadmin/index.html')

# 记录生活页面
def record_myself(request):
    myself = Record_myself.objects.all()
    return render(request,'blogadmin/record_myself.html',{'myself':myself})

# 显示生活
def show_record_myself(request):
    myself = request.GET.get('myselfid')
    subject = Record_myself.objects.filter(id=myself).first()
    subject.views_add()
    return render(request,'blogadmin/show_record_myself.html',{'mysubject':subject})

# 关于自己页面
def myself(request):
    return render(request,'blogadmin/myself.html')