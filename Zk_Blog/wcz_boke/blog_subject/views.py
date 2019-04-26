from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from blog_user.models import Blog_User
from blog_block.models import Blog_Block
from blog_subject.models import Blog_Subject
from blog_message.models import Blog_Message
from django.core import serializers
from django.db.models import Q
import datetime,random,json,time,os,uuid,hashlib
from django.views.decorators.csrf import csrf_exempt
from wcz_boke import settings
from blog_message.views import show_message 
import re,socket
# Create your views here.

# 创建主题
def subjectadd(request):
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        message = request.POST.get('message')
        subject_type = request.POST.get('subject_type')
        block = request.POST.get('block')
        block = Blog_Block.objects.filter(block_name=request.POST.get('block')).first()
        user = Blog_User.objects.filter(name=request.session['name']).first()
        subject = Blog_Subject.objects.create(
            subject_name=subject_name,
            block=block,
            user=user,
            subject_type=subject_type,
            subject_bodymes=message
        )
        # 循环试验
        # for i in range(1,50):
        #     subject = Blog_Subject.objects.create(
        #         subject_name=i,
        #         # subject_name=subject_name,
        #         block=block,
        #         user=user,
        #         subject_type=subject_type,
        #         subject_bodymes=message
        #     )
        return JsonResponse({'status':'ok'})
    else:
        return render(request,'user/useradd.html')

# 生成摘要
# def create_abstract(message):
#     print(message)
#     tihuan = re.compile(r'<[^>]+>',re.S)
#     abstract_list = re.findall('<p>(.*?)</p>|<div>.*</div>',message,re.S)
#     a=0
#     while tihuan.sub('',abstract_list[a]) is None:
#         a+=1
#     else:
#         if len(abstract_list[a]) > 75:
#             mes_abstract = tihuan.sub('',abstract_list[a])[:75]+"..."
#         else:
#             mes_abstract = tihuan.sub('',abstract_list[a])
#         a=0
#     return mes_abstract

# 上传图片保存
@csrf_exempt
def img_save(request):
    imgfile = request.FILES.get('file')
    curttime = time.strftime("%Y_%m_%d")
    # 当前项目创建文件夹路径
    upload_url = os.path.join(settings.STATICFILES_DIRS[0], 'django-summernote', curttime)
    folder = os.path.exists(upload_url)
    # 判断文件夹是否存在，不存在创建文件夹
    if not folder:
        # 创建文件夹
        os.makedirs(upload_url)
    # 判断是否有图片上传
    if imgfile:
        file_name = imgfile.name
        if os.path.exists(os.path.join(upload_url, file_name)):
            name, etx = os.path.splitext(file_name)
            finally_name = name + "_" + get_random_str() + etx
        else:
            finally_name = imgfile.name
        upload_file_to = open(os.path.join(upload_url,finally_name),'wb+')
        for chunk in imgfile.chunks():
            upload_file_to.write(chunk)
            # print("写入")
        upload_file_to.close()
        file_upload_url = settings.STATIC_URL + 'django-summernote/' + curttime + '/' + finally_name
        response_data={}
        response_data['FileName'] = file_name
        response_data['FileUrl'] = file_upload_url
        response_json_data = json.dumps(response_data)
        # print(response_json_data)
        return JsonResponse(response_json_data,safe=False)
    else:
        return JsonResponse({'status':'f'})

# 随机函数
def get_random_str():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode('utf-8')
    #md5实例
    md5 = hashlib.md5()
    #拿uuid的md5摘要
    md5.update(uuid_str)
    #返回固定长度的字符串
    return md5.hexdigest()

# 查看主题
def show_subject(request,id):
    subject = Blog_Subject.objects.filter(id=id).first()
    subject.views_add()
    return render(request,'subject/show_subject.html',{'subject':subject})
