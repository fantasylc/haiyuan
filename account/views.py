#coding:utf-8
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
import json
from .models import User
import uuid
from .utils import sendconfirmemail
from django.contrib import messages
import time
from django.contrib.auth.decorators import login_required
from .config import ROLE,YUANXI
from django.contrib.auth.forms import PasswordChangeForm

def user_login(request):
    if request.method == "POST":

        try:
            phone = request.POST.get('phone','')
            password = request.POST.get('password','')
            user = authenticate(phone=phone,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    info = {'status':'success','message':'登录成功'}
                    return HttpResponse(json.dumps(info))
                else:
                    return HttpResponse(json.dumps({'status':'failure','message':'邮箱还没有验证,请验证你的邮箱!'}))

            else:
                info = {'status':'failure','message':'手机号或密码错误'}
                return HttpResponse(json.dumps(info))

        except Exception as e:
            return HttpResponse(json.dumps({'status':'failure','message':'登录异常,请再试一次!'}))

    return render(request,'account/login2.html',locals())


def user_logout(request):
    try:
        logout(request)
        return HttpResponse('注销成功!')
    except Exception as e:
        return HttpResponse('注销异常')


def register(request):
    if request.method == 'POST':
        errors = []
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        active_code = str(uuid.uuid5(uuid.NAMESPACE_DNS,phone+str(time.time())))
        user = User.objects.filter(phone = phone).first()
        if user:
            if user.is_active:
                return HttpResponse(json.dumps({'status':'failure','message':'手机号已注册，请直接登陆或用其他手机号注册！'}))
            #return HttpResponse(user)
            else:
                return HttpResponse(json.dumps({'status':'failure','message':'手机号已经注册,请验证邮箱!'}))
        try:
            sendconfirmemail(email=email,active_code=active_code,other='confirm')


        except Exception as e:
            return HttpResponse('邮件发送出错，注册失败!',status=500)

        User.objects.create_user(phone,email,password=password,active_code=active_code)
        return HttpResponse(json.dumps({'status':'success','message':'验证邮件已发送给你,请查收验证邮箱!'}))

def active_user(request,active_code=None):
    try:
        user = User.objects.filter(active_code=active_code).first()
        if user:
            user.is_active=True
            user.save()
            user = authenticate(phone=user.phone,active_code=active_code)
            if user.is_active:
                login(request,user)
                messages.success(request,"你的邮箱已经验证成功!")
                user.active_code = None
                user.save()
                return HttpResponseRedirect('/')

        return HttpResponseNotFound('<h1>Page not found</h1>')
    except:
        return HttpResponseNotFound('<h2>没有查找到用户!</h2>')

@login_required()
def userinfo(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email','').replace('-','\-').replace("'","")
        user.nickname = request.POST.get('nickname','').replace('-','\-').replace("'","")
        user.address = request.POST.get('address','').replace('-','\-').replace("'","")
        user.yuanxi = request.POST.get('yuanxi','').replace('-','\-').replace("'","")
        user.shenfen = request.POST.get('shenfen','').replace('-','\-').replace("'","")
        user.xuehao = request.POST.get('xuehao','').replace('-','\-').replace("'","")
        user.realname = request.POST.get('realname','').replace('-','\-').replace("'","")
        user.save()
        return HttpResponse(json.dumps({'status':'success','message':''}))

    passwdresetform = PasswordChangeForm(user=request.user)
    roles = ROLE
    yuanxis = YUANXI
    return render(request,'account/userinfo.html',locals())

@login_required()
def changepasswd(request):
    if request.method == 'POST':
        error=[]
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return HttpResponse(json.dumps({'status':'success','message':'修改成功'}),content_type='application/json')

        else:
            for k,v in form.error_messages.items():
                error.append(str(v))
                return HttpResponse(json.dumps({'status':'failure','message':error}),content_type='application/json')

def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email',None)
        if email:
            try:
                user = User.objects.get(email=email)
                if user:
                    active_code = str(uuid.uuid5(uuid.NAMESPACE_DNS,user.phone+str(time.time())))
                    try:
                        sendconfirmemail(email=email,active_code=active_code,other='resetpassword')
                    except:
                        return HttpResponse(json.dumps({'status':'failure','message':'系统错误!'}))
                    user.active_code = active_code
                    user.save()
                    return HttpResponse(json.dumps({'status':'success','message':'邮件发送成功,请查收!'}))
            except User.DoesNotExist:
                return HttpResponse(json.dumps({'status':'failure','message':'此邮箱之前并未注册,请更换邮箱!'}))


    if request.method == 'GET':
        return render(request,'account/forgetpassword.html',locals())

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def resetpassword(request,active_code=None):

    return render(request,'account/resetpassword.html',locals())

def confirmreset(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1',None)
        password2 = request.POST.get('password2',None)
        active_code = request.POST.get('active_code',None)
        if not (password1 and password2 and active_code):
            return HttpResponse(json.dumps({'status':'failure','message':'选项不能为空！'}))
        try:
            user = User.objects.get(active_code=active_code)
            user.set_password(password2)
            user.save()
            user = authenticate(phone=user.phone,active_code=active_code)
            if user.is_active:
                login(request,user)
                return HttpResponse(json.dumps({'status':'success','message':'重置密码成功！'}))
        except User.DoesNotExist:
            return HttpResponse(json.dumps({'status':'failure','message':'用户不存在！！'}))

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

