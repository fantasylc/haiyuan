#coding:utf-8
from django.conf.urls import patterns,url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^login/$',views.user_login),
    url(r'^register/$',views.register),
    url(r'^logout/$',views.user_logout),
    url(r'^confirm/(?P<active_code>[\w\-]+)/$',views.active_user),
    url(r'^userinfo/$',views.userinfo),
    url(r'^changepasswd/$',views.changepasswd),
    url(r'^forgetpassword/$',views.forgetpassword),
    url(r'^resetpassword/(?P<active_code>[\w\-]+)/$',views.resetpassword),
    url(r'^confirmreset/$',views.confirmreset),

]