from django.contrib import admin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Register your models here.
from . import models


class studentAdmin(admin.ModelAdmin):
    def spk1(self):
        return self.spk
    spk1.short_description = '编号'

    def sid1(self):
        return self.sid
    sid1.short_description='用户名'

    def sname1(self):
        return self.sname
    sname1.short_description='姓名'

    def steacher1(self):
        return self.steacher
    steacher1.short_description='老师'

    def semail1(self):
        return self.semail
    semail1.short_description='邮箱'

    def stelephone1(self):
        return self.stelephone
    stelephone1.short_description='电话'

    def isshenhe1(self):
        if(self.isshenhe):
            return "是"
        else:
            return "否"

    isshenhe1.short_description='已审'

    def time1(self):
        return self.time
    time1.short_description='时间'

    list_display = [spk1,sid1,sname1,steacher1,semail1,stelephone1,isshenhe1,time1]
    list_filter = ['steacher']
    search_fields = ['sname']






admin.site.site_header='材料学院设备信息管理系统'
admin.site.site_title='信息管理'
admin.site.register(models.student,studentAdmin)




class teacherAdmin(admin.ModelAdmin):
    def tid1(self):
        return self.tid
    tid1.short_description = '编号'
    def tname1(self):

        return self.tname
    tname1.short_description='姓名'


    def temail1(self):

        return self.temail
    temail1.short_description='邮箱'
    def ttelephone1(self):

        return self.ttelephone
    ttelephone1.short_description='电话'

    list_display=[tid1,tname1,temail1,ttelephone1]
    list_filter = ['tname']
    search_fields=['tname','ttelephone']

admin.site.register(models.teacher,teacherAdmin)


class quanxianAdmin(admin.ModelAdmin):
    def qsid1(self):
        return self.qsid
    qsid1.short_description = '学生'
    def qeid1(self):
        return self.qeid
    qeid1.short_description='设备'
    list_display = [qsid1, qeid1]
    list_filter = ['qsid','qeid']
    search_fields = ['qsid__sname','qeid__ename']

admin.site.register(models.quanxian,quanxianAdmin)


class equipmentAdmin(admin.ModelAdmin):
    def eid1(self):
        return self.eid
    eid1.short_description = "编号"
    def ename1(self):
        return self.ename
    ename1.short_description = "器材"
    def eshiyanshi1(self):
        return self.eshiyanshi
    eshiyanshi1.short_description = "实验室"

    def exianshi1(self):
        return self.exianshi
    exianshi1.short_description = "限时"

    def eguanliyuan1(self):
        return self.eguanliyuan
    eguanliyuan1.short_description = "管理人"

    def ezhuangtai1(self):
        return self.ezhuangtai
    ezhuangtai1.short_description = "状态"

    list_display = [eid1,ename1,eshiyanshi1,exianshi1,eguanliyuan1,ezhuangtai1]
    list_filter = ['ename','eshiyanshi']
    search_fields = ['ename','eshiyanshi']
admin.site.register(models.equipment,equipmentAdmin)

class yuyueAdmin(admin.ModelAdmin):
    def ysid1(self):
        return self.ysid
    ysid1.short_description = '学生'

    def yeid1(self):
        return self.yeid
    yeid1.short_description = '设备'

    def ydate1(self):
        return self.ydate
    ydate1.short_description = '预约日期'

    def ytimestart1(self):
        return self.ytimestart
    ytimestart1.short_description = '开始时间'

    def shichang1(self):
        return self.shichang
    shichang1.short_description = '用时'

    def shichang1(self):
        return self.shichang
    shichang1.short_description = '用时'

    def yuyuebeizhu1(self):
        return self.yuyuebeizhu
    yuyuebeizhu1.short_description = '备注'

    def shiyanfankui1(self):
        return self.shiyanfankui
    shiyanfankui1.short_description = '反馈'

    def isqiandao1(self):
        if(self.isqiandao):
            return "是"
        else:
            return "否"

    isqiandao1.short_description = '违约'



    list_display = [ysid1, yeid1, ydate1,ytimestart1,shichang1,yuyuebeizhu1,shiyanfankui1,isqiandao1]
    list_filter = ['ysid','yeid','ydate','isqiandao']
    search_fields = ['ysid__sname','yeid__ename','ydate','isqiandao']
admin.site.register(models.yuyue,yuyueAdmin)

class weiyuecishuAdmin(admin.ModelAdmin):
    def ysid1(self):
        return self.ysid
    ysid1.short_description = '学生'
    def number1(self):
        return self.number
    number1.short_description = '次数'
    list_display = [ysid1, number1]
    list_filter = ['ysid', 'number']
    search_fields = ['ysid']
admin.site.register(models.weiyuecishu,weiyuecishuAdmin)

class xitongxinxiAdmin(admin.ModelAdmin):
    def yuyueshichang1(self):
        return self.yuyueshichang
    yuyueshichang1.short_description = '预约提前天数'

    def quxiaoyuyue1(self):
        return self.quxiaoyuyue
    quxiaoyuyue1.short_description = '违约提前天数'
    list_display = [yuyueshichang1, quxiaoyuyue1]
    # def get_model_perms(self, request):
    #     return {
    #         # 'add': self.has_add_permission(request),
    #         'change': self.has_change_permission(request),
    #         # 'delete': self.has_delete_permission(request),
    #     }
    #关闭添加功能
    def has_add_permission(self, request):
        return False




admin.site.register(models.xitongxinxi, xitongxinxiAdmin)




