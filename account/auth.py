#coding:utf-8
__author__ = 'liuchao'

from .models import User

class MyBackend(object):
    '自定义用户认证,实现学号登陆'
    def authenticate(self,phone=None, password=None,active_code=None):
        try:
            user = User.objects.get(phone=phone)
            if user:
                if user.check_password(password):
                    return user
                elif user.active_code==active_code:
                    return user
                else:
                    return None
        except User.DoesNotExist:
            return None

    def get_user(self,user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user:
                return user
            return None
        except User.DoesNotExist:
            return None
