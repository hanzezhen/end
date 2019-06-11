from django.db import models

# Create your models here.


class teacher(models.Model):
    class Meta:
        db_table='teacher'
        verbose_name = '老师'
        verbose_name_plural = '老师'
    tid=models.AutoField('编号',primary_key=True)#使用id作为主键的好处是，可以修改导师姓名，不会影响外联数据表
    tname=models.CharField('姓名',max_length=20)
    temail=models.CharField('邮箱',max_length=50,blank=True)
    ttelephone = models.CharField('电话', max_length=30,blank=True)
    def __str__(self):
        return self.tname


from django.utils import timezone
class student(models.Model):
    class Meta:
        db_table='student'
        verbose_name = '学生'
        verbose_name_plural = '学生'
    spk=models.AutoField('编号',primary_key=True)
    sid=models.CharField('用户名',max_length=30,unique=True)
    sname=models.CharField('姓名',max_length=20)
    steacher=models.ForeignKey(teacher,verbose_name='老师',on_delete=models.PROTECT)#是否使用级联删除，修改老师时，不要删除老师,修改老师

    semail=models.CharField('邮箱',max_length=50,blank=True)
    stelephone=models.CharField('电话',max_length=30,blank=True)
    isshenhe=models.BooleanField('已审',default=False)
    time=models.DateField("注册时间",default = timezone.now)#自动时间，可以手动修改

    password =models.CharField('密码',max_length=50)
    time_use=models.DecimalField('用时',max_digits=10,decimal_places=1,default=0.0)
    istongguo=models.BooleanField('审核通过',default=False)
    isstudent=models.BooleanField('是否组内',default=True)
    def __str__(self):
        return self.sname


# -*- coding: UTF-8 -*-
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


class ImageStorage(FileSystemStorage):
    from django.conf import settings

    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        # 初始化
        super(ImageStorage, self).__init__(location, base_url)

    # 重写 _save方法
    def _save(self, name, content):
        # name为上传文件名称
        print(type(content))

        import os, time, random
        # 文件扩展名
        ext = os.path.splitext(name)[1]
        # 文件目录
        d = os.path.dirname(name)
        # 定义文件名，年月日时分秒随机数
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(0, 100)
        # 重写合成文件名
        name = os.path.join(d, fn + ext)
        # 调用父类方法
        return super(ImageStorage, self)._save(name, content)

from PIL import Image

def make_thumb(path, size = 480):
    pixbuf = Image.open(path)
    return pixbuf.resize((890,593))

# from __future__ import division
import os
from booksystem.settings import MEDIA_ROOT
from django.db.models.fields.files import ImageFieldFile

THUMB_ROOT=r'thumb'


class equipment(models.Model):
    class Meta:
        db_table='equipment'
        verbose_name = '设备'
        verbose_name_plural = '设备'
    epic=models.ImageField(upload_to='img',storage=ImageStorage())
    eid=models.AutoField('编号',primary_key=True)
    ename=models.CharField('设备名',max_length=50)
    eshiyanshi=models.CharField('实验室',max_length=50)
    eguanliyuan=models.CharField('管理人',max_length=50)
    ezhuangtai=models.BooleanField('设备状态',default=True)
    exianshi=models.DecimalField("限时",max_digits=10,decimal_places=1,default=100.0)#对应一周还是两周
    ejieshao1=models.CharField("介绍第一段",max_length=500,blank=True)
    ejieshao2=models.CharField("介绍第二段",max_length=500,blank=True)
    ejieshao3=models.CharField("介绍第三段",max_length=500,blank=True)

    def save(self):
        super(equipment, self).save()  # 将上传的图片先保存一下，否则报错
        base, ext = os.path.splitext(os.path.basename(self.epic.path))
        thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT, self.epic.name))
        relate_thumb_path = os.path.join(THUMB_ROOT, base + '.thumb' + ext)
        thumb_path = os.path.join(MEDIA_ROOT, relate_thumb_path)
        thumb_pixbuf.save(thumb_path)
        self.epic = ImageFieldFile(self, self.epic, relate_thumb_path)
        super(equipment, self).save()


    def __str__(self):
        return self.ename


class quanxian(models.Model):
    class Meta:
        db_table='quanxian'
        unique_together=('qsid','qeid',)
        verbose_name = '权限'
        verbose_name_plural = '权限'
    qsid=models.ForeignKey(student,on_delete=models.PROTECT,db_column="qsid",verbose_name='学生',limit_choices_to={'istongguo':True})#给外键添加约束条件，只选择istongguo=True的项，不会保存到数据库
    qeid=models.ForeignKey(equipment,on_delete=models.PROTECT,db_column="qeid",verbose_name='设备')

    def __str__(self):
        return self.qsid.sname+"   ----  "+self.qeid.ename



#如果预约有错误，最后是删除重新预约，不要在后台更改预约信息
class yuyue(models.Model):
    class Meta:
        db_table='yuyue'
        verbose_name = '预约'
        verbose_name_plural = '预约'
    ysid=models.ForeignKey(student,limit_choices_to={'istongguo':True},on_delete=models.PROTECT)
    qiandaoshijian = models.BooleanField('签到时间',default=False)
    yeid=models.ForeignKey(equipment,on_delete=models.PROTECT)
    ydate=models.DateField('预约日期')
    jieshushijian = models.CharField('结束时间',max_length=30,default='a')
    isquxiao = models.BooleanField('取消',default=False)
    ytimestart=models.CharField('开始时间',max_length=30)
    shichang=models.DecimalField('时长',max_digits=5,decimal_places=1)
    yuyuebeizhu=models.CharField("备注",max_length=200,blank=True)
    shiyanfankui=models.CharField("实验反馈",max_length=200,blank=True)
    isqiandao=models.BooleanField('违约',default=True)
    quxiabeizhu = models.CharField('取消备注',max_length=200,blank=True)
    quxiaoshijian = models.BooleanField('是否到了取消时间',default=False)
    def __str__(self):
        return str("预约")



#违约次数
class weiyuecishu(models.Model):
    class Meta:
        db_table='weiyue'
        verbose_name = '违约次数'
        verbose_name_plural = '违约次数'
    ysid=models.ForeignKey(student,limit_choices_to={'istongguo':True},on_delete=models.PROTECT)
    number=models.IntegerField('违约次数',default=0)
    def __str__(self):
        return str("weiyue")


#系统信息
class xitongxinxi(models.Model):
    class Meta:
        db_table='xitongxinxi'
        verbose_name = '系统信息'
        verbose_name_plural = '系统信息'
    yuyueshichang=models.IntegerField("预约提前天数",default=14)
    quxiaoyuyue=models.IntegerField('取消预约提前',default=1)
    def __str__(self):
        return str("系统信息只能修改不能添加")