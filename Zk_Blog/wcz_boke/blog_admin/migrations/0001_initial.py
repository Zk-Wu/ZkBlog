# Generated by Django 2.1.3 on 2019-04-21 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('level', models.CharField(max_length=20, verbose_name='级别')),
            ],
            options={
                'verbose_name': '管理员',
                'verbose_name_plural': '管理员',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='My_Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.CharField(max_length=50, verbose_name='歌名')),
                ('song_type', models.CharField(max_length=50, verbose_name='歌手类型')),
                ('songer', models.CharField(max_length=50, verbose_name='歌手')),
                ('music_info', models.CharField(max_length=9999, verbose_name='歌曲简介')),
            ],
            options={
                'verbose_name': '音乐分享',
                'verbose_name_plural': '音乐分享',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Record_myself',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titie_name', models.CharField(max_length=255, verbose_name='标题')),
                ('subject_create_date', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('mainmes', models.CharField(max_length=999999, verbose_name='文章内容')),
                ('views_num', models.IntegerField(default=0, verbose_name='浏览数量')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myselfs', to='blog_admin.Blog_Admin', verbose_name='楼主')),
            ],
            options={
                'verbose_name': '记录生活',
                'verbose_name_plural': '记录生活',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
