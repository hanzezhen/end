from .models import student,teacher
from django.shortcuts import render
from django.http import HttpResponse
from .views import checklogin


def register(req):
    teacherlist = []
    tea=teacher.objects.all()
    for item in tea:
        teacherlist.append(item.tname)
    return render(req,'register.html',{
        'teacherlist':   teacherlist
    })



def register2(req):
    return render(req,'register2.html')


def zhucechenggong(request):
    name = request.POST.get('sname')
    sid = request.POST.get('sid')
    password = request.POST.get('password')
    teacher1 = request.POST.getlist('teacher1')
    semail = request.POST.get('semail')
    stelephone = request.POST.get('stelephone')
    tea = teacher.objects.filter(tname=teacher1[0])[0]
    st = student(sname=name, steacher=tea,semail=semail,sid=sid,stelephone=stelephone,password=password)
    st.save()
    stu=student.objects.filter(sname=name)
    return render(request,'zhucechenggong.html',{'stu':stu[0]})
import datetime,time

def zhucechenggong2(request):
    name = request.POST.get('sname')


    a = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    while student.objects.filter(sid=a) :
        time.sleep(0.5)
        a = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    sid = a
    password = request.POST.get('password')

    semail = request.POST.get('semail')
    stelephone = request.POST.get('stelephone')
    tname =r'校外人员'
    tea = teacher.objects.filter(tname=tname)[0]
    st = student(sname=name, steacher=tea, semail=semail, sid=sid, stelephone=stelephone, password=password,isstudent=False)
    st.save()
    stu = student.objects.filter(sname=name)
    return render(request, 'zhucechenggong.html',{'stu':stu[0]})
