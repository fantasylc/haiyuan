#coding:utf-8
__author__ = 'liuchao'
from django.contrib import admin
from .models import *

class VersionAdminInline(admin.TabularInline):
    model = Version
    extra = 0

class CartitemAdminInline(admin.TabularInline):
    model = Cartitem
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = (VersionAdminInline,)
    list_display = ('name','category','number',)
    fieldsets = (
        ('None',{'fields':('id','category','name','brand','unit',
                           'desc','detail','sales','status','is_tuijian','number','img_show','img_show_tag',
                           'img_detail_1','img_d1_tag','img_detail_2','img_d2_tag',
                           'img_detail_3','img_d3_tag','img_thum','img_thum_tag')}),
    )
    readonly_fields = ('id','img_show_tag','img_d1_tag','img_d2_tag','img_d3_tag','img_thum_tag')

class OrderAdmin(admin.ModelAdmin):
    inlines = (CartitemAdminInline,)
    list_display = ('id','user','date_add')
    fields = ('id','user','total_money','date_add')
    readonly_fields = ('id','date_add',)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','parent')
    fields = ('id','name','index','parent')
    readonly_fields = ('id',)

admin.site.register(AboutUs)
admin.site.register(TopProductCategory)
admin.site.register(ProductCategory,ProductCategoryAdmin)
admin.site.register(Version)
admin.site.register(Brand)
admin.site.register(Cartitem)
admin.site.register(Order,OrderAdmin)
admin.site.register(Product,ProductAdmin)
