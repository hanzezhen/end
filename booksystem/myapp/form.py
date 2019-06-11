import json
from django.http import HttpResponse,JsonResponse
import re
import datetime
from .models import student,teacher,yuyue,equipment

def ajax1get(request):
    uname = json.loads(request.body.decode())
    stu = student.objects.filter(sid=uname['username'])

    if stu :
        ret = {"sttr":"yes"}
    else:
        ret = {"sttr":"no"}
    print(ret)
    return HttpResponse(json.dumps(ret))


from .datecal import dateRange
def ajax2get(request):
    data= json.loads(request.body.decode())
    uername = data['username']
    eid =data['eid']
    val = data['val']
    now_time = datetime.datetime.now()
    datelist = dateRange(now_time)
    num = re.search(r'(^[0-9]+)and',val).group(1)
    date = datelist[int(num)-1]
    hour = re.search(r"and([0-9]+)$",val).group(1)
    starthour = str(int(hour)+6)+'：00'
    stu = student.objects.filter(sname=uername)[0]
    ep = equipment.objects.filter(eid=eid)[0]
    ax = yuyue.objects.filter(yeid=ep).filter(ysid=stu).filter(ydate=date).filter(ytimestart=starthour).filter(isquxiao=False)
    if ax:
        ret = {'sttr':'no'}
    else:
        ret = {'sttr':'yes'}
        yy = yuyue(yeid=ep,ysid=stu,ydate=date,ytimestart=starthour,shichang=1.0)
        yy.save()

    print(ret)
    return HttpResponse(json.dumps(ret))

def ajax3get(request):
    uname = json.loads(request.body.decode())
    stu = uname['username']
    nianyueri = re.compile(r'^(.+?)an')
    time2 =re.compile(r'and(.+?)$')
    nianyue= re.search(nianyueri,stu).group(1)
    shijian = re.search(time2,stu).group(1)
    # print(nianyue)
    # print(shijian)
    ename = re.search(r'an(.+?)and',stu).group(1)
    # print(ename)
    eid = equipment.objects.filter(ename = ename)[0]
    ydate=datetime.datetime.strptime(nianyue, "%Y年%m月%d日")
    ytimestart =shijian
    ko = yuyue.objects.filter(ydate=ydate).filter(ytimestart=ytimestart).filter(yeid=eid).filter(isquxiao=False)[0]
    # print('你要的',ko)
    try:
        ko.isquxiao=True
        ko.isqiandao = False
        ko.save()
        print(ko.isquxiao)
        ret = {"sttr": "yes"}
    except:
        ret = {"sttr": "no"}

    return HttpResponse(json.dumps(ret))

def ajax4get(request):
    uname = json.loads(request.body.decode())
    stu = uname['username']
    # print(stu)
    nianyueri = re.compile(r'^(.+?)an')
    time2 =re.compile(r'and(.+?)$')
    nianyue= re.search(nianyueri,stu).group(1)
    shijian = re.search(time2,stu).group(1).replace('a','')
    # print(nianyue)
    # print(shijian)
    ename = re.search(r'an(.+?)and',stu).group(1)
    # print(ename)
    eid = equipment.objects.filter(ename = ename)[0]
    ydate=datetime.datetime.strptime(nianyue, "%Y年%m月%d日")
    ytimestart =shijian
    ko = yuyue.objects.filter(ydate=ydate).filter(ytimestart=ytimestart).filter(yeid=eid).filter(isquxiao=False)[0]
    # print('你要的',ko)
    neirong = uname['con']
    ko.isqiandao=False
    ko.shiyanfankui=neirong
    ko.save()
    return HttpResponse('ok')

def ajax5get(request):
    uname = json.loads(request.body.decode())
    stu = uname['username']
    print(stu)
    nianyueri = re.compile(r'^(.+?)an')
    time2 =re.compile(r'and(.+?)$')
    nianyue= re.search(nianyueri,stu).group(1)
    shijian = re.search(time2,stu).group(1).replace('a','')
    print(nianyue)
    print(shijian)
    name = re.search(r'an(.+?)and',stu).group(1)
    eid = equipment.objects.filter(ename=name)[0]
    sname = eid.ename

    ret = {'nianyue': nianyue,
           'shijian':shijian,
           'ename':sname}


    print(ret)
    return HttpResponse(json.dumps(ret))

def ajax6get(request):
    uname = json.loads(request.body.decode())
    stu = uname['username']
    print('1231231231321')
    # print(stu)
    nianyueri = re.compile(r'^(.+?)an')
    time2 =re.compile(r'and(.+?)$')
    nianyue= re.search(nianyueri,stu).group(1)
    shijian = re.search(time2,stu).group(1).replace('a','')

    # print(shijian)
    ename = re.search(r'an(.+?)and',stu).group(1)
    # print(ename)
    eid = equipment.objects.filter(ename = ename)[0]
    ydate=datetime.datetime.strptime(nianyue, "%Y年%m月%d日")
    ytimestart =shijian
    ko = yuyue.objects.filter(ydate=ydate).filter(ytimestart=ytimestart).filter(yeid=eid).filter(isquxiao=False)[0]
    # print('你要的',ko)
    neirong = uname['con']
    ko.isquxiao=True
    ko.quxiaobeizhu=neirong
    ko.save()
    return HttpResponse('ok')




