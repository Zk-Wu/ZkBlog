from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from blog_user.models import Blog_User
from blog_subject.models import Blog_Subject
from blog_block.models import Blog_Block
from blog_message.models import User_Message
from blog_admin.models import My_Music,SongType
from django.core import serializers
from django.db.models import Q
import datetime,random,json,html,smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
# Create your views here.
# 首页
def index(request):
    subjects = Blog_Subject.objects.order_by('-subject_create_date')[:30]
    blocks = Blog_Block.objects.all()
    return render(request, 'user/index.html', {'subjects':subjects,'blocks':blocks})

# 到底部加载数据
def lastjz(request):
    first = int(request.GET.get('first'))
    last = int(request.GET.get('last'))
    print(first,last)
    subjects = Blog_Subject.objects.order_by('-subject_create_date')[first:last]
    lists = render(request,'user/lastjz.html',{'subjects':subjects})
    return lists

# 首页右侧最新更新信息
def newest_subject(request):
    newest_subjects = Blog_Subject.objects.order_by('-subject_create_date')[:5]
    xs = render(request,'user/newest_subject.html',{'newest_subjects':newest_subjects})
    return xs

# 验证码生成
def yzm(request):
    from PIL import Image,ImageDraw,ImageFont
    # 定义背景颜色
    # bgcolor = (
    #     random.randrange(20,100),
    #     random.randrange(20,100),
    #     random.randrange(20,100)
    # )
    # 设置宽高
    width=135
    height=35
    # 创建画布对象
    im = Image.new('RGB',(width,height),(255,255,255))
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数描绘线条
    for i in range(0,7):
        xya = (random.randrange(0,width),random.randrange(0,height))
        xyb = (random.randrange(0,width),random.randrange(0,height))
        fill = (random.randrange(0,255),255,random.randrange(0,255))
        draw.line([xya,xyb],fill=fill, width = 5)
    # 定义验证码字符库
    yzmstr = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    rand_str = ''
    # 随机4个字符为验证码
    for i in range(0,4):
        rand_str += yzmstr[random.randrange(0,len(yzmstr))]
    # 构造字体对象
    # font = ImageFont.truetype('/usr/local/django/wcz_boke/static/fonts/AdobeGothicStd-Bold.otf',30)
    font = ImageFont.truetype('/static/fonts/AdobeGothicStd-Bold.otf',30)
    # 构建字体颜色
    fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor1)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor2)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor3)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor4)
    #释放画笔
    del draw
    #内存文件操作
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    response = HttpResponse(buf.getvalue(), 'image/png')
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    return response

# 生成发送邮箱验证码
def send_email(request):
    try:
        if request.method == 'POST':
            user_email = request.POST.get('user_email')
            my_sendemail = 'wucz_zk@qq.com'
            # 授权码 jrmyrnovzbvxbcfe
            my_pass = 'jrmyrnovzbvxbcfe'
            # 注册填写邮箱
            my_user = user_email
            print(my_user)
            # 生成随机六位数密码
            yzmstr = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
            rand_emailstr = ''
            for i in range(0,6):
                rand_emailstr += yzmstr[random.randrange(0,len(yzmstr))]
            # 设置发送文本内容
            msg = MIMEText('欢迎来到我的博客，验证码为：%s' %rand_emailstr, 'plain', 'utf-8')
            msg['From'] = formataddr(["From www.zcorew.com", my_sendemail])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "zcorew博客"  # 邮件的主题，也可以说是标题
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sendemail, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sendemail, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
            request.session['rand_emailstr'] = rand_emailstr
            return JsonResponse({'status':'t'})
    except:
        return JsonResponse({'status':'f'})

# 验证邮箱验证码
def check_email(request,emailyzm):
    if request.session.get('rand_emailstr') == emailyzm:
        return JsonResponse({'status':'t'})
    else:
        return JsonResponse({'status':'f'})

# 检查验证码
def check_yzm(request,yzm):
    if request.session.get('verifycode') == yzm:
        print('1',request.session.get('verifycode'))
        return JsonResponse({'status':'t'})
    else:
        print('2',request.session.get('verifycode'))
        return JsonResponse({'status':'f'})

     
# 用户注册
def useradd(request):
    if request.method == 'POST':
        name = request.POST.get('user')
        pwd = make_password(request.POST.get('pwd'),None,'pbkdf2_sha256')
        # nicheng = request.POST.get('nicheng')
        email = request.POST.get('email')
        Blog_User.objects.create(name=name,password=pwd,email=email)
        return redirect('home')
    else:
        return render(request,'user/useradd.html')

# 用户名查重
def check_username(request,username):
    try:
        Blog_User.objects.get(name=username)
        return JsonResponse({'status':'f'})
    except:
        return JsonResponse({'status':'t'})

# 用户登录
def userlogin(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = Blog_User.objects.filter(name=name).first()
        if user:
            check_user = check_password(pwd,user.password)
            if check_user:
                # print('111')
                request.session['name'] = user.name
                request.session['nicheng'] = user.nicheng
                request.session['email'] = user.email
                request.session['sex'] = user.sex
                request.session['level'] = user.level
                # print('ok')
                return JsonResponse({'status':'t'})
            else:
                return JsonResponse({'status':'f'})
        else:
            return JsonResponse({'status':'f'})


# 忘记密码
def reset_pwd(request):
    return render(request,'user/repassword.html')
    # return render(request,)

# 修改密码
def set_pwd(request,status):
    if request.method == 'POST':
        if status == 'setpwd':
            email = request.POST.get('email')
            request.session['email'] = email
            return render(request,'user/setpwd.html')
        else:
            email = request.session['email']
            print(email)
            pwd = request.POST.get('pwd')
            user = Blog_User.objects.filter(email=email).update(password=make_password(pwd))
            return JsonResponse({'status':'t'})
    

# 用户注销模块
def userlogout(request):
    # 删除全部session值
    request.session.clear()
    return redirect('home')

# 创建主题模块
def create_subject(request):
    try:
        request.session['name']
        blocks = Blog_Block.objects.all()
        # return render(request,'subject/create_subject.html',{'blocks':blocks})
        return render(request,'subject/create_subject.html',{'blocks':blocks})
    except:
        return render(request, 'user/index.html',{'nologin':'f'})
        # return JsonResponse({'nologin':'nologin'})

# 查询模块
def user_search(request):
    # html.escape()对html语言转义
    search_text = html.escape(request.GET.get('search_text'))
    # print(html.escape(search_text))
    seach = Blog_Subject.objects.filter(
        Q(subject_name__contains=search_text) | 
        Q(subject_bodymes__contains=search_text) | 
        Q(messages__message__contains=search_text)
    ).distinct()
    # 清洗数据
    return render(request,'user/search.html',{'subjects':seach})


# 侧边导航栏
def nav_bar(request):
    block_name = request.POST.get('block_name')
    subjects = Blog_Subject.objects.filter(block=Blog_Block.objects.get(block_name=block_name)).order_by('-subject_create_date')
    ok = render(request, 'user/nav_bar.html', {'subjects':subjects})
    return ok

# 技术备忘页面
def study_back(request):
    subject = Blog_Subject.objects.all()
    blocks = Blog_Block.objects.all()
    return render(request,'user/study_back.html',{'subjects':subject,'blocks':blocks})

# 音乐交流页面
def music(request):
    music = My_Music.objects.order_by('subject_create_date')
    music_type = SongType.objects.all()
    return render(request,'user/music.html',{'musics':music,'music_types':music_type})

# 用户留言页面
def usermes(request):
    if request.method == "POST":
        mes = html.escape(request.POST.get('mes'))
        email = request.POST.get('email')
        nicheng = request.POST.get('nicheng')
        fuid = request.POST.get('fuid')
        if fuid:
            User_Message.objects.create(
            usermes=mes,
            email=email,
            nicheng=nicheng,
            fu_mes=fuid
        )
        else:
            User_Message.objects.create(
                usermes=mes,
                email=email,
                nicheng=nicheng,
            )
        return JsonResponse({'status':'t'})
    else:
        return render(request,'user/usermes.html')

# 时间归档
def save_date(request):
    import datetime
    if request.method == "POST":
        print(request.POST.get('date'))
        datea = datetime.datetime.strptime(request.POST.get('date'),'%Y-%m-%d')
        date = datetime.datetime.strftime(datea,'%Y-%m')
        datesubject = Blog_Subject.objects.filter(subject_create_date__startswith=date)
        print(datesubject)
        return render(request,'user/nav_bar.html',{'subjects':datesubject})
    else:
        date = Blog_Subject.objects.dates('subject_create_date','month',order='DESC')
        # print(date)
        return render(request,'user/save_date.html',{'dates':date})

# 文章分类
def subject_type(request):
    subject_type = request.GET.get('type')
    subjects = Blog_Subject.objects.filter(subject_type=subject_type)
    return render(request,'subject/subject_type.html',{'subjects':subjects})
