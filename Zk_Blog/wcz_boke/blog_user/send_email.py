import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


# 发件人邮箱
def send_email(user):
    my_sendemail = 'wucz_zk@qq.com'
    # 授权码 jrmyrnovzbvxbcfe
    my_pass = 'jrmyrnovzbvxbcfe'
    my_user = user
    return {'my_sendemail':my_sendemail,'my_pass':my_pass,'my_user':my_user}


def mail(request):
    ret = True
    new_user = send_email("lll")
    try:
        yzmstr = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        rand_emailstr = ''
        for i in range(0,6):
            rand_emailstr += yzmstr[random.randrange(0,len(yzmstr))]
        msg = MIMEText('<h1>欢迎来到我的博客</h1><br><h2>验证码为：%s<h2>' %rand_str, 'plain', 'utf-8')
        msg['From'] = formataddr(["From nicead.top", new_user['my_sendemail']])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", new_user['my_user']])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "博客网站"  # 邮件的主题，也可以说是标题
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(new_user['my_sendemail'], new_user['my_pass'])  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(new_user['my_sendemail'], [new_user['my_user'], ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        request.session['rand_emailstr'] = rand_emailstr
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret

