#coding:utf-8
__author__ = 'liuchao'
import os
from django.db import models
from django.conf import settings
import uuid
from django.utils.deconstruct import deconstructible
STATUS = {
    '0':'采购中',
    '1':'上线',
}


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]

        filename = '{}.{}'.format(uuid.uuid4().hex,ext)

        return os.path.join(self.path, filename)

@deconstructible
class ThumPathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]

        filename = '{}.{}'.format(uuid.uuid4().hex+'_thum',ext)

        return os.path.join(self.path, filename)





class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self


class AboutUs(models.Model):
    content = models.TextField(default='',verbose_name='关于我们')

    class Meta:
        verbose_name_plural = verbose_name='关于我们'

    def __str__(self):
        return str(self.id)

class TopProductCategory(models.Model):
    name = models.CharField(max_length=20,verbose_name='顶级分类名')
    index = models.IntegerField(default=1,verbose_name='排序')

    class Meta:
        verbose_name = verbose_name_plural = '商品顶级分类'
        ordering = ['index','name']

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    uid = models.CharField(max_length=80,default='',verbose_name='Token')
    name = models.CharField(max_length=15,verbose_name='产品分类名')
    index = models.IntegerField(default=1,verbose_name='排序')
    parent = models.ForeignKey(TopProductCategory,default=None,related_name='childs',verbose_name='顶级分类')


    def save(self, *args,**kwargs):
        self.uid = uuid.uuid5(uuid.NAMESPACE_DNS,str(self.pk))
        super(ProductCategory,self).save(*args,**kwargs)

    class Meta:
        verbose_name = verbose_name_plural = '商品分类'
        ordering = ['index','name']



    def __str__(self):

        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=30,default='', verbose_name='品牌名称')
    index = models.IntegerField(default=1,verbose_name='排列顺序')

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = verbose_name
        ordering = ['index',]

    def __str__(self):
        return self.name



class Product(models.Model):
    #id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=80,default='',verbose_name='Token')
    category = models.ForeignKey(ProductCategory,related_name='products',verbose_name='产品分类')
    brand = models.ForeignKey(Brand,verbose_name='品牌',blank=True,null=True)
    name = models.CharField(max_length=50,default='',verbose_name='商品名')
    desc = models.CharField(max_length=100,default='',verbose_name='商品简介')
    detail = models.TextField(default='',verbose_name='商品详情')
    unit = models.CharField(default='',max_length=10,verbose_name='单位')
    color = models.CharField(max_length=10,default='',null=True,blank=True,verbose_name='颜色')
    sales = models.IntegerField(default=0,verbose_name='销量')
    status = models.CharField(max_length=5,default='',choices=STATUS.items(),verbose_name='状态')
    add_time = models.DateTimeField(auto_now_add=True)
    is_tuijian = models.BooleanField(default=False,verbose_name='是否首页推荐')
    index = models.IntegerField(default=1,verbose_name='排序')



    # version = models.ManyToManyField(Version,verbose_name='版本')
    number = models.IntegerField(default=0,verbose_name='库存')
    img_show = models.ImageField(upload_to=PathAndRename("product/show/"),
                                 null=True,blank=True,editable=True,verbose_name='展示图片地址')
    img_detail_1 = models.ImageField(upload_to=PathAndRename("product/detail/"),
                                     null=True,blank=True,editable=True,verbose_name='详情图片地址1')
    img_detail_2 = models.ImageField(upload_to=PathAndRename("product/detail/"),
                                     null=True,blank=True,editable=True,verbose_name='详情图片地址2')
    img_detail_3= models.ImageField(upload_to=PathAndRename("product/detail/"),
                                    null=True,blank=True,editable=True,verbose_name='详情图片地址3')
    thum_width = models.PositiveIntegerField(default=50,verbose_name='缩略图宽度')
    thum_height = models.PositiveIntegerField(default=50,verbose_name='缩略图高度')
    img_thum = models.ImageField(upload_to=ThumPathAndRename("product/thum/"),width_field='thum_width',
                                 height_field='thum_height',
                                    null=True,blank=True,editable=True,verbose_name='缩略图')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name
        ordering = ['id']


    def img_show_tag(self):
        if self.img_show:
            return '<img src="/media/%s" width=100,height=100/>' %(self.img_show)

    def img_d1_tag(self):
        if self.img_detail_1:
            return '<img src="/media/%s" width=100,height=100/>' %(self.img_detail_1)

    def img_d2_tag(self):
        if self.img_detail_2:
            return '<img src="/media/%s" width=100,height=100/>' %(self.img_detail_2)

    def img_d3_tag(self):
        if self.img_detail_3:
            return '<img src="/media/%s" width=100,height=100/>' %(self.img_detail_3)

    def img_thum_tag(self):
        if self.img_thum:
            return '<img src="/media/%s" width=100,height=100/>' %(self.img_thum)

    img_show_tag.short_description = '列表展示图'
    img_show_tag.allow_tags = True
    img_d1_tag.short_description = '详情图1'
    img_d1_tag.allow_tags = True
    img_d2_tag.short_description = '详情图2'
    img_d2_tag.allow_tags = True
    img_d3_tag.short_description = '详情图3'
    img_d3_tag.allow_tags = True
    img_thum_tag.short_description = '缩略图'
    img_thum_tag.allow_tags = True


    def save(self,*args,**kwargs):
        self.uid = uuid.uuid5(uuid.NAMESPACE_DNS,str(self.pk))
        if self.id is not None:
            current = Product.objects.get(id=self.id)
            if self.img_show != current.img_show:
                # Delete old image and thumbnail
                current.img_show.delete(save=False)
            # Set save=False because it's saving now.
            if self.img_detail_1 != current.img_detail_1:
                current.img_detail_1.delete(save=False)
            if self.img_detail_2 != current.img_detail_2:
                current.img_detail_2.delete(save=False)
            if self.img_detail_3 != current.img_detail_3:
                current.img_detail_3.delete(save=False)
            if self.img_thum != current.img_thum:
                current.img_thum.delete(save=False)
        super(Product,self).save(*args,**kwargs)


    def __str__(self):
        return self.name



class Version(models.Model):
    product = models.ForeignKey(Product,related_name='versions',verbose_name='商品')
    name = models.CharField(max_length=30,default='',verbose_name='商品版本')
    old_price = models.FloatField(default=0.0,verbose_name='原价')
    discount = models.FloatField(default=1,verbose_name='折扣')
    now_price = models.FloatField(default=0,verbose_name='现价')

    class Meta:
        verbose_name_plural = verbose_name = '商品版本'

    def __str__(self):
        return self.name


#订单类
class Order(models.Model):
    uid = models.CharField(max_length=80,default='',verbose_name='Token')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='orders',default=None,verbose_name='拥有者')
    date_add = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    total_money = models.FloatField(default=0.0,verbose_name='总价')

    def save(self,*args,**kwargs):
        self.uid = uuid.uuid5(uuid.NAMESPACE_DNS,str(self.pk))
        super(Order,self).save(*args,**kwargs)

    class Meta:
        verbose_name_plural = verbose_name='订单'

    def __str__(self):
        return str(self.id)





class Cartitem(models.Model):
    product = models.ForeignKey(Product,related_name='car',verbose_name='商品')
    quantity = models.IntegerField(default=1,verbose_name='数量')
    sum_price = models.FloatField(default=0.0,verbose_name='小计')
    date_added = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order,default=None,blank=True,null=True,
                              related_name='items', verbose_name='条目')

    class Meta:
        verbose_name_plural = verbose_name = '购物车头目'
        ordering = ['date_added']

    def save(self,*args,**kwargs):
        self.sum_price = self.product.versions.all()[0].now_price*self.quantity
        super(Cartitem,self).save(*args,**kwargs)


    def add_quantity(self,quantity):
        self.quantity = self.quantity+int(quantity)
        self.save()



    def __str__(self):
        return '%s--%d'.format(self.product.name,self.quantity)
#购物车
class Cart(object):
    def __init__(self):
        self.items = []
        self._total_price = 0.0

    def add(self,cartitem):
        for item in self.items:
            if item.product.id == cartitem.product.id:
                item.quantity+=cartitem.quantity
                item.sum_price+=cartitem.sum_price
                return
            else:
                print('addcar',cartitem)
                self.items.append(cartitem)
                return
        self.items.append(cartitem)

    @property
    def total_price(self):
        money = 0.0
        for item in self.items:
            money = money+item.sum_price
        return money

    @total_price.setter
    def total_price(self, value):

        self._total_price = value






