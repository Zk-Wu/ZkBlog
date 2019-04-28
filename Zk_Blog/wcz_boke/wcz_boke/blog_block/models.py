from django.db import models
from blog_user.models import Blog_User as User

# Create your models here.
class Blog_Block(models.Model):
    def __str__(self):
        return self.block_name
    
    block_name = models.CharField(primary_key=True, max_length=50, verbose_name="版块名")
    block_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blocks",verbose_name="版主")
    block_create_date = models.DateTimeField(verbose_name="版块创建时间", auto_now=False, auto_now_add=True)

    class Meta:
        db_table=''
        managed=True
        verbose_name='版块'
        verbose_name_plural='版块'