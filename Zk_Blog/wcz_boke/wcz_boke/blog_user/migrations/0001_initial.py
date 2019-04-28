# Generated by Django 2.1.3 on 2019-04-18 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_User',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('nicheng', models.CharField(blank=True, max_length=20, null=True, verbose_name='昵称')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('sex', models.CharField(default='无', max_length=10, verbose_name='性别')),
                ('status', models.SmallIntegerField(default=1, verbose_name='状态')),
                ('level', models.CharField(default='大神', max_length=20, verbose_name='级别')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
