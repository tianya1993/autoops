# Generated by Django 2.0 on 2017-12-29 15:50

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='librarys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, null=True, unique=True, verbose_name='标题')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', max_length=1024000000000, verbose_name='内容')),
                ('classify', models.CharField(blank=True, max_length=128, null=True, verbose_name='分类')),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '技术文库',
                'verbose_name_plural': '技术文库',
                'db_table': 'librarys',
                'permissions': {('read_librarys', '只读技术文库')},
            },
        ),
    ]
