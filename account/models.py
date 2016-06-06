#coding:utf-8
__author__ = 'liuchao'

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
# Create your models here.
from .config import ROLE,YUANXI


class MyUserManager(BaseUserManager):
    def create_user(self,phone,email,password=None,**kwargs):
        if not phone:
            raise ValueError('注册必须使用学号!')
        user = self.model(phone=phone)
        user.email = email
        user.set_password(password)

        if kwargs:
            if kwargs.get('active_code',None):
                user.active_code=kwargs['active_code']
            if kwargs.get('nickname',None):
                user.username = kwargs['nickname']

        user.save(using=self._db)


        return user

    def create_superuser(self,phone,email,password,**kwargs):
        user = self.create_user(phone,email,password=password)
        user.is_admin = True
        #user.is_staff=True
        user.is_active=True
        user.is_superuser = True

        user.save(using=self._db)
        return user




class User(AbstractBaseUser):

    phone = models.CharField(max_length=20,default='',verbose_name='手机号',unique=True)
    email = models.EmailField(verbose_name='邮箱',max_length=255)
    xuehao = models.CharField(max_length=20,default='',verbose_name='学号')
    nickname = models.CharField(max_length=30, default='改个昵称吧', verbose_name='昵称')
    realname = models.CharField(max_length=10,default='',verbose_name='真实姓名')
    avatar = models.ImageField(upload_to='avatars', verbose_name='头像')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    is_active = models.BooleanField(default=False,verbose_name='是否激活')
    active_code = models.CharField(max_length=200,default='',verbose_name='激活码')
    is_admin = models.BooleanField(default=False)

    yuanxi = models.CharField(default='',max_length=30)
    role = models.CharField(default='',max_length=10,verbose_name='身份')
    huiyuan = models.IntegerField(default=0,verbose_name='会员等级')
    address = models.CharField(max_length=100,default='',verbose_name='收货地址')



    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']



    objects = MyUserManager()

    def get_full_name(self):
        return self.phone

    def get_short_name(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin



    class Meta:
        verbose_name_plural = verbose_name = '用户'
        ordering = ['phone']


    def __str__(self):
        return self.phone

