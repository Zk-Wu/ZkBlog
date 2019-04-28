from django.db import models
from blog_block.models import Blog_Block
from blog_subject.models import Blog_Subject
from blog_message.models import Blog_Message
# Create your models here.
class Blog_Admin(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(verbose_name="用户名", max_length=50)
    password = models.CharField(verbose_name="密码", max_length=256)
    level = models.CharField(verbose_name="级别", max_length=20)

    class Meta:
        db_table=''
        managed=True
        verbose_name="管理员"
        verbose_name_plural="管理员"

class Record_myself(models.Model):
    def __str__(self):
        return self.titie_name

    titie_name = models.CharField(max_length=255,verbose_name="标题")
    subject_create_date = models.DateTimeField(auto_now=True, auto_now_add=False,verbose_name="创建时间")
    user = models.ForeignKey(Blog_Admin,on_delete=models.CASCADE,related_name="myselfs",verbose_name="楼主")
    mainmes = models.CharField(verbose_name="文章内容",max_length=999999)
    views_num = models.IntegerField(default=0,verbose_name="浏览数量")

    class Meta:
        db_table=''
        managed=True
        verbose_name="记录生活"
        verbose_name_plural="记录生活"

    # 浏览量统计
    def views_add(self):
        self.views_num +=1
        self.save(update_fields=["views_num"])

class SongType(models.Model):
    def __str__(self):
        return self.song_type

    song_type = models.CharField(verbose_name="歌曲类型", max_length=50)

    class Meta:
        db_table=''
        managed=True
        verbose_name="歌曲类型"
        verbose_name_plural="歌曲类型"

class My_Music(models.Model):
    def __str__(self):
        return self.music_name

    music_name = models.CharField(verbose_name="歌名", max_length=50)
    songer = models.CharField(verbose_name="歌手", max_length=50)
    song_type = models.ForeignKey(SongType,verbose_name="歌曲类型",on_delete=models.CASCADE,related_name="mymusics")
    subject_create_date = models.DateTimeField(auto_now=True, auto_now_add=False,verbose_name="创建时间")
    music_info = models.CharField(verbose_name="歌曲简介", max_length=9999)

    class Meta:
        db_table=''
        managed=True
        verbose_name="音乐分享"
        verbose_name_plural="音乐分享"

