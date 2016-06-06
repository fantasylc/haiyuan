from django.shortcuts import render,render_to_response
from .models import Product,AboutUs
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from django.db.models import Q
from urllib.parse import urlparse
import json
def index(request):
    pd_tuijians = Product.objects.filter(is_tuijian = True).all()
    topfenleis = TopProductCategory.objects.all()
    # for product in pd_tuijians:
    #     product.versions = product.versions.all()
    return render(request,'index.html',locals())
    #return render_to_response('index.html',{'pd_tuijians':pd_tuijians})

def aboutus(request):
    about = AboutUs.objects.all().last()
    return render(request,'aboutus.html',locals())

def product(request,uid=None):
    product = Product.objects.get(uid=uid)
    return render(request,'store/product-detail.html',locals())

@login_required()
def view_cart(request):
    if request.user.is_authenticated():
        redirect_to = request.GET['next']

        cart = request.session.get(request.user.id,None)
        return render(request,'store/viewcart.html',locals())



#添加购物车
def add_cart(request):
    if request.user.is_authenticated():
        pd_id = request.POST.get('pd_id',None)
        pd_quantity = int(request.POST.get('pd_quantity',None))

        try:
            product = Product.objects.get(pk=pd_id)
            sum_price = product.versions.all()[0].now_price*pd_quantity
            cartitem = Cartitem(product=product,quantity=pd_quantity,sum_price=sum_price)

        except Product.DoesNotExist:
            return HttpResponse(json.dumps({'status':'error','message':'您购买的商品不存在'}))

        cart = request.session.get(request.user.id,None)
        if not cart:
            cart = Cart()
            cart.add(cartitem)
            print('car:',cart.items)
            request.session[request.user.id] = cart
            return HttpResponse(json.dumps({'status':'success','message':'添加购物车成功'}))
        else:
            print('cart',cart)
            print('pdname',cartitem.product.name)
            cart.add(cartitem)
            print('car:',cart.items)
            request.session[request.user.id] = cart
            return HttpResponse(json.dumps({'status':'success','message':'添加购物车成功2！'}))

    else:
        return HttpResponse(json.dumps({'status':'error','message':'您需要先登陆!'}))

def clear_cart(request):
    if request.user.is_authenticated():
        cart = Cart()
        request.session[request.user.id] = cart
        return HttpResponse(json.dumps({'status':'success','message':'清除购物车成功！'}))

    else:
        return HttpResponse(json.dumps({'status':'error','message':'请先登陆！'}))


def del_cart(request):
    if request.user.is_authenticated():
        index = request.POST.get('index',None)
        if index:
            index = int(index)
            cart = request.session.get(request.user.id,None)
            del cart.items[index]
            request.session[request.user.id] = cart
            return HttpResponse(json.dumps({'status':'success','message':'删除成功！'}))
        return HttpResponse(json.dumps({'status':'error','message':'cuola！'}))

    else:
        return HttpResponse(json.dumps({'status':'error','message':'请先登陆！'}))

@login_required()
def submitorder(request):
    if request.method == 'POST':
        cart = request.session.get(request.user.id,None)
        if cart.items:
            order = Order(user=request.user)
            order.save()
            for item in cart.items:
                item.order = order
                item.save()

            order.total_money = cart.total_price
            order.save()
            cart = Cart()
            request.session[request.user.id] = cart
        return HttpResponse(json.dumps({'status':'success','message':'chenggongla'}))


    return render(request,'store/submitorder.html',locals())

@login_required()
def myorders(request):
    orders = request.user.orders.all()
    return render(request,'store/myorders.html',locals())

def productcategory(request,uid = ''):
    category = ProductCategory.objects.get(uid=uid)
    products = category.products.all()
    return render(request,'store/categorys.html',locals())

def search(request):
    if request.method == 'GET':
        word = request.GET.get('word','')
        products = Product.objects.only('name','desc').filter(Q(name__icontains=word) | Q(desc__icontains=word))
        return render(request,'store/searchs.html',locals())