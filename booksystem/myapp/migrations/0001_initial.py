# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('epic', models.ImageField(upload_to='img', storage=myapp.models.ImageStorage())),
                ('eid', models.AutoField(verbose_name='编号', primary_key=True, serialize=False)),
                ('ename', models.CharField(verbose_name='设备名', max_length=50)),
                ('eshiyanshi', models.CharField(verbose_name='实验室', max_length=50)),
                ('eguanliyuan', models.CharField(verbose_name='管理人', max_length=50)),
                ('ezhuangtai', models.BooleanField(verbose_name='设备状态', default=True)),
                ('exianshi', models.DecimalField(verbose_name='限时', default=100.0, max_digits=10, decimal_places=1)),
                ('ejieshao1', models.CharField(verbose_name='介绍第一段', max_length=500, blank=True)),
                ('ejieshao2', models.CharField(verbose_name='介绍第二段', max_length=500, blank=True)),
                ('ejieshao3', models.CharField(verbose_name='介绍第三段', max_length=500, blank=True)),
            ],
            options={
                'verbose_name': '设备',
                'verbose_name_plural': '设备',
                'db_table': 'equipment',
            },
        ),
        migrations.CreateModel(
            name='quanxian',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('qeid', models.ForeignKey(verbose_name='设备', db_column='qeid', on_delete=django.db.models.deletion.PROTECT, to='myapp.equipment')),
            ],
            options={
                'verbose_name': '权限',
                'verbose_name_plural': '权限',
                'db_table': 'quanxian',
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('spk', models.AutoField(verbose_name='编号', primary_key=True, serialize=False)),
                ('sid', models.CharField(verbose_name='用户名', max_length=30, unique=True)),
                ('sname', models.CharField(verbose_name='姓名', max_length=20)),
                ('semail', models.CharField(verbose_name='邮箱', max_length=50, blank=True)),
                ('stelephone', models.CharField(verbose_name='电话', max_length=30, blank=True)),
                ('isshenhe', models.BooleanField(verbose_name='已审', default=False)),
                ('time', models.DateField(verbose_name='注册时间', default=django.utils.timezone.now)),
                ('password', models.CharField(verbose_name='密码', max_length=50)),
                ('time_use', models.DecimalField(verbose_name='用时', default=0.0, max_digits=10, decimal_places=1)),
                ('istongguo', models.BooleanField(verbose_name='审核通过', default=False)),
                ('isstudent', models.BooleanField(verbose_name='是否组内', default=True)),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('tid', models.AutoField(verbose_name='编号', primary_key=True, serialize=False)),
                ('tname', models.CharField(verbose_name='姓名', max_length=20)),
                ('temail', models.CharField(verbose_name='邮箱', max_length=50, blank=True)),
                ('ttelephone', models.CharField(verbose_name='电话', max_length=30, blank=True)),
            ],
            options={
                'verbose_name': '老师',
                'verbose_name_plural': '老师',
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='weiyuecishu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField(verbose_name='违约次数', default=0)),
                ('ysid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.student')),
            ],
            options={
                'verbose_name': '违约次数',
                'verbose_name_plural': '违约次数',
                'db_table': 'weiyue',
            },
        ),
        migrations.CreateModel(
            name='xitongxinxi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('yuyueshichang', models.IntegerField(verbose_name='预约提前天数', default=14)),
                ('quxiaoyuyue', models.IntegerField(verbose_name='取消预约提前', default=1)),
            ],
            options={
                'verbose_name': '系统信息',
                'verbose_name_plural': '系统信息',
                'db_table': 'xitongxinxi',
            },
        ),
        migrations.CreateModel(
            name='yuyue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('qiandaoshijian', models.BooleanField(verbose_name='签到时间', default=False)),
                ('ydate', models.DateField(verbose_name='预约日期')),
                ('jieshushijian', models.CharField(verbose_name='结束时间', max_length=30, default='a')),
                ('isquxiao', models.BooleanField(verbose_name='取消', default=False)),
                ('ytimestart', models.CharField(verbose_name='开始时间', max_length=30)),
                ('shichang', models.DecimalField(verbose_name='时长', max_digits=5, decimal_places=1)),
                ('yuyuebeizhu', models.CharField(verbose_name='备注', max_length=200, blank=True)),
                ('shiyanfankui', models.CharField(verbose_name='实验反馈', max_length=200, blank=True)),
                ('isqiandao', models.BooleanField(verbose_name='违约', default=True)),
                ('quxiabeizhu', models.CharField(verbose_name='取消备注', max_length=200, blank=True)),
                ('quxiaoshijian', models.BooleanField(verbose_name='是否到了取消时间', default=False)),
                ('yeid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.equipment')),
                ('ysid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.student')),
            ],
            options={
                'verbose_name': '预约',
                'verbose_name_plural': '预约',
                'db_table': 'yuyue',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='steacher',
            field=models.ForeignKey(verbose_name='老师', on_delete=django.db.models.deletion.PROTECT, to='myapp.teacher'),
        ),
        migrations.AddField(
            model_name='quanxian',
            name='qsid',
            field=models.ForeignKey(verbose_name='学生', db_column='qsid', on_delete=django.db.models.deletion.PROTECT, to='myapp.student'),
        ),
        migrations.AlterUniqueTogether(
            name='quanxian',
            unique_together=set([('qsid', 'qeid')]),
        ),
    ]
