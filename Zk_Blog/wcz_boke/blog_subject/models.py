from django.db import models
from blog_user.models import Blog_User as User
from blog_block.models import Blog_Block as Block
# from blog_message.models import Blog_Message as Message

# Create your models here.
class Blog_Subject(models.Model):
    def __str__(self):
        return self.subject_name

    subject_name = models.CharField(max_length=255,verbose_name="主题标题")
    subject_create_date = models.DateTimeField(auto_now=True, auto_now_add=False,verbose_name="回复时间")
    block = models.ForeignKey(Block,on_delete=models.CASCADE,related_name="subject_names",verbose_name="所属版块")
    subject_type = models.CharField(verbose_name="文章类型", max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="subject_names",verbose_name="楼主")
    subject_bodymes = models.CharField(verbose_name="文章内容",max_length=999999)
    accesses_num = models.IntegerField(default=0,verbose_name="浏览数量")

    
    class Meta:
        db_table=''
        managed=True
        verbose_name='主题'
        verbose_name_plural='主题'

    # 阅读量统计
    def views_add(self):
        self.accesses_num +=1
        self.save(update_fields=["accesses_num"])
    


    