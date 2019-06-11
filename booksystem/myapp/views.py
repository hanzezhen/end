from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from .models import teacher,student,equipment,quanxian,yuyue
import json
# Create your views here.

from django.contrib.auth import authenticate, login,get_user
def adminloginin(request):
    username = request.POST['username']
    print("username:",username)
    password = request.POST['password']
    print("password:", password)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request=request,user=user)
        # Redirect to a success page.
        return HttpResponseRedirect('/foradmin/')
    else:
        return HttpResponseRedirect('/admin/login/')

def  signpass(request):
    name=request.POST.get("name")
    sid=request.POST.get("sid")
    teachername=request.POST.get("teacher")
    email=request.POST.get("email")
    telephone=request.POST.get("telephone")
    print("456")
    teacherlist=teacher.objects.filter(tname=teachername)[0]
    print(teacher)
    print("123")
    newstudent=student(sname=name,sid=sid,steacher=teacherlist,stname=teachername,semail=email,stelephone=telephone)
    newstudent.save()

    return JsonResponse({"data":"yes"})

def index(request):

    return render(request, 'index.html')

def foradmin(request):
    user=get_user(request=request)
    # print("user:",user)
    if not request.user.is_authenticated():
    # if str(user) == "AnonymousUser":
        return HttpResponseRedirect('/admin/login/')
    else:
        newstudents=student.objects.filter(Q(isshenhe=False),Q(isstudent=True))
        number1=len(newstudents)
        newzuwairenyuan=student.objects.filter(Q(isshenhe=False),Q(isstudent=False))
        number2=len(newzuwairenyuan)
        print("number:",number1)
        # number1=5
        return render(request,'foradmin.html',{"number1":number1,"number2":number2})


def studentquanxian(request):
    queryname = request.GET.get('q', default='')
    print("ID:",queryname)

    # newstudents = student.objects.filter(Q(sname__icontains=queryname))
    newstudents = student.objects.filter(Q(sname__icontains=queryname),Q(isshenhe=False))
    print("newstudents:",newstudents)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")



    equipments = equipment.objects.all()
    return render(request,'studentquanxian.html',{"queryname":queryname,"students":newstudents,"equipments":equipments})


def xiaowaishenqing(request):
    queryname = request.GET.get('q', default='')
    print("ID:", queryname)

    # newstudents = student.objects.filter(Q(sname__icontains=queryname))
    newstudents = student.objects.filter(Q(sname__icontains=queryname), Q(isshenhe=False), Q(isstudent=False))
    print("newstudents:", newstudents)


    equipments = equipment.objects.all()
    return render(request, 'xiaowaishenqing.html',
                  {"queryname": queryname, "students": newstudents, "equipments": equipments})






def studentupdate(request):
    return render(request,"studentupdate.html")

def administerupdate(request):
    return render(request,"administerupdate.html")

def shenhe(request):

    jsonstring = json.loads(request.body.decode())
    stuid = jsonstring["stuid"]
    mychecked=jsonstring["mychecked"]
    print("jsonstring:",jsonstring)

    print("nycheckd:", mychecked)
    print("#################################")
    print("stuid:",stuid)
    print("#################################")
    studentpk=student.objects.filter(sid=stuid)
    print("studentpk:",studentpk[0])
    print(type(studentpk))
    print("#################################")


    print("end:", studentpk[0].isshenhe)



    quanxianlist=quanxian.objects.filter(qsid=studentpk[0])
    print("quanxianlist:",quanxianlist)
    quanxianlist.delete()#��ɾ��Ȩ��
    print("shanchuchenggong")


    for check in mychecked:
        equipmentone = equipment.objects.filter(eid=check)[0]
        print("studentpk[0]:",studentpk[0])
        print("equipmentone:",equipmentone)

        newone=quanxian(qsid=studentpk[0],qeid=equipmentone)
        newone.save()


    studente=student.objects.get(sid=stuid)
    studente.isshenhe = 1
    studente.istongguo=1
    studente.save()
    return JsonResponse({"data": "mydata"})


def gezhi(request):
    jsonstring = json.loads(request.body.decode())
    stuid = jsonstring["stuid"]
    studente = student.objects.get(sid=stuid)
    studente.isshenhe = 1
    studente.istongguo=1
    studente.save()
    return JsonResponse({"data": "mydata"})

def butongguo(request):
    jsonstring = json.loads(request.body.decode())
    stuid = jsonstring["stuid"]
    studente = student.objects.get(sid=stuid)
    studente.isshenhe = 1

    studente.save()
    return JsonResponse({"data": "mydata"})


def dingshiforadmin(request):
    newstudents = student.objects.filter(isshenhe=False)
    number = len(newstudents)
    print("number")
    return JsonResponse({'number1':"haha"})

# from django.db import connection
from django.db.models import F, FloatField, Sum
def studentform(request):
    queryxuehao=request.GET.get('xuehao',default='')
    queryname = request.GET.get('name', default='')
    queryteacher=request.GET.get('teacher',default='')
    startdate = request.GET.get('timestart', default='')
    enddate = request.GET.get('timeend', default='')
    print('queryxuehao:',queryxuehao)
    print('queryname:',queryname)
    print('queryteacher:',queryteacher)
    print('startdate:',startdate)
    print('enddate:',enddate)
    if (startdate == ""):
        startquery = ""
        startTime = datetime.datetime.strptime('2019/01/01', '%Y/%m/%d').date()
    else:
        startquery = startdate
        startTime = datetime.datetime.strptime(startdate, '%Y/%m/%d').date()

    if (enddate == ""):
        endquery = ""
        endTime = datetime.date.today()
    else:
        endquery = enddate
        endTime = datetime.datetime.strptime(enddate, '%Y/%m/%d').date()

    studentall = yuyue.objects.filter(Q(ysid__steacher__tname__icontains=queryteacher),Q(ysid__sid__icontains=queryxuehao), Q(ysid__sname__icontains=queryname), Q(ydate__gte=startTime),
                                      Q(ydate__lte=endTime))
    studentall1 = studentall.values_list("ysid__spk","ysid__sid", "ysid__sname", "ysid__steacher__tname").annotate(
        sum_shichang=Sum('shichang'))




    print("##########################################")
    result=[]
    for row in studentall1:
        spk=row[0]
        sid=row[1]
        sname=row[2]
        tname=row[3]
        sum_shichang=row[4]
        result.append({"spk":spk,"sid":sid,"sname":sname,"tname":tname,"sum_shichang":sum_shichang})

    return render(request,'studentform.html',{"startquery":startquery,"endquery":endquery,"queryname":queryname,"querysid":queryxuehao,"queryteacher":queryteacher,"starttime":startTime,"endtime":endTime,'students':result})

def teacherform(request):

    queryname = request.GET.get('name', default='')
    startdate=request.GET.get('timestart',default='')
    enddate=request.GET.get('timeend',default='')
    if(startdate==""):
        startquery=""
        startTime=datetime.datetime.strptime('2019/01/01', '%Y/%m/%d').date()
    else:
        startquery =startdate
        startTime = datetime.datetime.strptime(startdate, '%Y/%m/%d').date()

    if (enddate == ""):
        endquery = ""
        endTime = datetime.date.today()
    else:
        endquery = enddate
        endTime = datetime.datetime.strptime(enddate, '%Y/%m/%d').date()

    print("startTime:",startTime)
    print("endTime:",endTime)
    print("ID:", queryname)
    teacherall = yuyue.objects.filter(Q(ysid__steacher__tname__icontains=queryname),Q(ydate__gte=startTime),Q(ydate__lte=endTime))
    teacherall1=teacherall.values_list("ysid__steacher__tid","ysid__steacher__tname").annotate(sum_shichang=Sum('shichang'))
    print("teacherall1:",teacherall1)
    result=[]
    for row in teacherall1:
        tid=row[0]
        tname=row[1]
        sum_shichang=row[2]
        result.append({"tid":tid,"tname":tname,"sum_shichang":sum_shichang})
    return render(request,'teacherform.html',{"startquery":startquery,"endquery":endquery,"queryname":queryname,"starttime":startTime,"endtime":endTime,"teachers":result})


def weekform(request):
    print("weekformstart")
    queryname = request.GET.get('name', default='')
    startdate=request.GET.get('timestart',default='')
    enddate=request.GET.get('timeend',default='')
    if(startdate==""):
        startquery=""
        startTime=datetime.datetime.strptime('2019/01/01', '%Y/%m/%d').date()
    else:
        startquery =startdate
        startTime = datetime.datetime.strptime(startdate, '%Y/%m/%d').date()

    if (enddate == ""):
        endquery = ""
        endTime = datetime.date.today()
    else:
        endquery = enddate
        endTime = datetime.datetime.strptime(enddate, '%Y/%m/%d').date()


    shebei1 = yuyue.objects.filter(Q(yeid__ename__icontains=queryname),Q(ydate__gte=startTime),Q(ydate__lte=endTime))
    shebeis=shebei1.values_list("yeid__eid","yeid__ename").annotate(sum_shichang=Sum('shichang'))
    print("shebeis:",shebeis)
    result=[]
    for row in shebeis:
        tid=row[0]
        tname=row[1]
        sum_shichang=row[2]
        result.append({"tid":tid,"tname":tname,"sum_shichang":sum_shichang})
    print("result:",result)
    return render(request,'weekform.html',{"startquery":startquery,"endquery":endquery,"queryname":queryname,"starttime":startTime,"endtime":endTime,"shebeis":result})





















#####################################################
from django.shortcuts import render,redirect

# Create your views here.


from .models import student



from django.db.models import Max,F,Q

from django.http import HttpResponse


def studentshtml(request):
    # studentlist = Students.objects.all()
    return render(request,'showStudents.html')


from functools import wraps

def checklogin(f):
    @wraps(f)
    def inner(request,*args,**kwargs):
        if request.session.get('is_login') == '1':
            return f(request,*args,**kwargs)
        else:
            return redirect('/login/')
    return inner



@checklogin
def home(request):

    uname    = request.POST.get('username',None)
    upasswrd = request.POST.get('password',None)

    return render(request,'home.html',{'username':uname,'password':upasswrd})

def login(request):
    return render(request,'login.html')


def hometrans(request):
    uname = request.POST.get('username', None)
    upasswrd = request.POST.get('password', None)

    stu = student.objects.filter(sid=uname,password=upasswrd)
    try:
        a = yuyue.objects.all()
        for i in a:
            a=i.ytimestart.replace(':', '：')
            i.ytimestart=a
            i.save()
            # print(i.ytimestart)
    except:
        print('None')


    if stu:
        request.session['is_login'] = '1'
        request.session['username'] = stu[0].sname
        return redirect('/indextest/')

    return render(request,'login.html', {'error': 1})










from .datecal import dateRange
import datetime

@checklogin
def home2(request):
    name=request.session.get('username')
    stu = student.objects.filter(sname=name)
    equipment = [401,403,501,]
    if name:
        return render(request, 'home2.html', {'susername': name,'student': stu[0],

                                              'equipment':equipment})
    else:
        return render(request,'home2.html')

@checklogin
def quitlogin(request):
    request.session.flush()
    return render(request,'login.html')


@checklogin
def date(request,num):
    stimelist = list(range(7))
    rangelist = list(range(14))
    now_time = datetime.datetime.now()
    datelist = dateRange(now_time)
    ep = num
    return render(request,'date.html',{'t':stimelist,'s':rangelist,'date1':datelist,'ep':ep})


def traceback(request):
    # name=request.POST.get('name')
    # print(name)
    # idnumber = request.POST.get('idn')
    # print(idnumber)
    # username = request.POST.get('username')
    # print(username)
    # password = request.POST.get('password')
    # print(password)
    # st=student(sname=name,sid=username,
    #             sphonenumber=idnumber,password=password,sidnumber=idnumber)
    # st.save()
    # stu=student.objects.filter(sid=username)
    return render(request,'traceback.html',{})

def signup(request):
    return render(request,'signup.html')



from django.contrib import auth

