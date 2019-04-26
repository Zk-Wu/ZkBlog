from django.db import models

# Create your models here.
class Blog_User(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(primary_key=True,verbose_name="用户名", max_length=50)
    password = models.CharField(verbose_name="密码", max_length=256)
    nicheng = models.CharField(null=True,blank=True,verbose_name="昵称", max_length=20)
    email = models.CharField(verbose_name="邮箱", max_length=50, unique=True)
    sex = models.CharField(default='无',verbose_name="性别", max_length=10)
    status = models.SmallIntegerField(verbose_name="状态",default=1)
    level = models.CharField(default='大神',verbose_name="级别", max_length=20)

    class Meta:
        db_table=''
        managed=True
        verbose_name="用户"
        verbose_name_plural="用户"