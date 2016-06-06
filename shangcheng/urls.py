#coding:utf-8
__author__ = 'liuchao'

from django.conf.urls import url,patterns
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^product/(?P<uid>[\w\-]+)/$',views.product),
    url(r'^aboutus/$',views.aboutus),
    url(r'^add_cart/$',views.add_cart),
    url(r'^viewcart/$',views.view_cart),
    url(r'^clearcart/$',views.clear_cart),
    url(r'^delcart/$',views.del_cart),
    url(r'^submitorder/$',views.submitorder),
    url(r'^myorders/$',views.myorders),
    url(r'^productcategory/(?P<uid>[\w\-]+)/$',views.productcategory),
    url(r'^search/$',views.search),
        ]