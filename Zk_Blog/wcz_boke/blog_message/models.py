from django.db import models
from blog_user.models import Blog_User as User
from blog_subject.models import Blog_Subject as Subject
# Create your models here.


class Blog_Message(models.Model):
    def __str__(self):
        return self.message

    message= models.TextField(max_length=1000,verbose_name="回复信息")
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name="messages",verbose_name="所属主题")
    message_create_date = models.DateTimeField(auto_now=False,auto_now_add=True,verbose_name="回复时间")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="messages",verbose_name="回复用户")

    class Meta:
        db_table=''
        managed=True
        verbose_name="回复"
        verbose_name_plural="回复" 

class User_Message(models.Model):

    def __str__(self):
        return self.usermes
    
    nicheng = models.CharField(null=False,blank=False,verbose_name="用户昵称", max_length=20)
    usermes = models.CharField(verbose_name="用户留言", max_length=100)
    email = models.CharField(null=True,blank=True,max_length=32, db_index=True,verbose_name="联系邮箱")
    fu_mes = models.SmallIntegerField(default=0,verbose_name="父级回复")
    create_time = models.DateTimeField(auto_now=False,auto_now_add=True,verbose_name="回复时间")

    class Meta:
        db_table=''
        managed=True
        verbose_name="用户留言" #指定在admin管理界面中显示的内容
        verbose_name_plural="用户留言" 

        # verbose_name表示单数形式的显示，
        # verbose_name_plural表示复数形式的显示；
        # 中文的单数和复数一般不作区别。



