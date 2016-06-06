#coding:utf-8
__author__ = 'liuchao'


from django import forms

from .models import User

from django.forms import TextInput

# class MyTextInput(TextInput):
#     def __init__(self,*args,**kwargs):
#         self.attrs = None
#         super(MyTextInput,self).__init__(*args,**kwargs)
#
# class UserInfoForm(forms.ModelForm):
#
#     def __init__(self,*args,**kwargs):
#         self.request = kwargs.pop('request',None)
#         super(UserInfoForm,self).__init__(*args,**kwargs)
#         self.fields['nikename'].attrs.value = self.request.user.nikename
#
#
#     nickname = forms.CharField(label='昵称',max_length=20,widget=MyTextInput(
#         attrs={'class':'form-control',}
#     ))