# Generated by Django 2.1.3 on 2019-04-18 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Block',
            fields=[
                ('block_name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='版块名')),
                ('block_create_date', models.DateTimeField(auto_now_add=True, verbose_name='版块创建时间')),
                ('block_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='blog_user.Blog_User', verbose_name='版主')),
            ],
            options={
                'verbose_name': '版块',
                'verbose_name_plural': '版块',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
