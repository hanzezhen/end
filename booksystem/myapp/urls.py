from django.conf.urls import include, url
from . import views,form,tests,hanzezhen_url,makaiquan
urlpatterns = [

    url(r'^signpass/$',views.signpass,name='signpass'),
    url(r'^foradmin/$',views.foradmin,name='formadmin'),
    url(r'^studentquanxian/$',views.studentquanxian,name='studentquanxian'),

    # url(r'^xiaowaishenqing/$',views.xiaowaishenqing,name='xiaowaishenqing'),
    url(r'^studentupdate/$',views.studentupdate,name='studentupdate'),
    url(r'^weekform/$',views.weekform,name='weekform'),
    url(r'^shenhe/$',views.shenhe,name='shenhe'),
    url(r'^gezhi/$',views.gezhi,name='gezhi'),
    url(r'^butongguo/$',views.butongguo,name='butongguo'),
    url(r'^dingshiforadmin/$',views.dingshiforadmin,name='dingshiforadmin'),
    url(r'^studentform/$',views.studentform,name='studentform'),
    url(r'^teacherform/$',views.teacherform,name='teacherform'),

    url(r'^studentshenqing/$', makaiquan.studentshenqing, name='studentshenqing'),
    url(r'^stusqupdateepi/$', makaiquan.stusqupdateepi, name='stusqupdateepi'),
    url(r'^chongxinfenpei1/$', makaiquan.chongxinfenpei1, name='chongxinfenpei1'),
    url(r'^chongxinfenpei2/$', makaiquan.chongxinfenpei2, name='chongxinfenpei2'),
    url(r'^tianjia1/$', makaiquan.tianjia1, name='tianjia1'),
    url(r'^tianjia2/$', makaiquan.tianjia2, name='tianjia2'),
    url(r'^shanchu1/$', makaiquan.shanchu1, name='shanchu1'),
    url(r'^shanchu2/$', makaiquan.shanchu2, name='shanchu2'),
    url(r'^xiaowaitongguo/$', makaiquan.xiaowaitongguo, name='xiaowaitongguo'),
    url(r'^foradmin2/$', makaiquan.foradmin2, name='foradmin2'),
    url(r'^shebeiform/$', makaiquan.shebeiform, name='shebeiform'),
    url(r'^shebeizhuangtai/$', makaiquan.shebeizhuangtai, name='shebeizhuangtai'),
    url(r'^weiyuecishu/$', makaiquan.weiyuecishu, name='weiyuecishu'),
    url(r'^zhengchang/$', makaiquan.zhengchang, name='zhengchang'),
    url(r'^weixiu/$', makaiquan.weixiu, name='weixiu'),


    url(r'^login/', views.login),
    url(r'^home2/', views.home2),
    url(r'^hometrans/', views.hometrans),
    url(r'^quitlogin/', views.quitlogin),
    url(r'^(\d{3})', views.date),
    url(r'^traceback', views.traceback),
    url(r'^signup', views.signup),
    url(r'^ajax1get/', form.ajax1get),
    url(r'^ajax2get/', form.ajax2get),
    url(r'^ajax3get/', form.ajax3get),
    url(r'^ajax4get/', form.ajax4get),
    url(r'^ajax5get/', form.ajax5get),
    url(r'^ajax6get/', form.ajax6get),

    url(r'^test11/', tests.test11),
    url(r'^index/', tests.index),
    url(r'^indextest/', tests.indextest),
    url(r'^baseinfo/', tests.baseinfo),
    url(r'^myappointment/', tests.myappointment),
    url(r'^epappoint/', tests.epappoint),
    url(r'^appoint(\d{1,3})/', tests.appoint),
    url(r'^appointfalse/', tests.appointfalse),

    url(r"^",include('myapp.hanzezhen_url',namespace='myapp1'))
]
