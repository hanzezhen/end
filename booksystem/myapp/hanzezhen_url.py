from . import hanzezhen
from django.conf.urls import include, url
urlpatterns = [

    url(r'^register/$',hanzezhen.register),
    url(r'^register2/$', hanzezhen.register2),

    url(r'^zhucechenggong/$', hanzezhen.zhucechenggong),
    url(r'^zhucechenggong2/$', hanzezhen.zhucechenggong2),


]