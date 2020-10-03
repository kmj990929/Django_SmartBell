from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'bell_app/index.html')

def indexMenu(request):
    menus = Menu.objects.all()
    content = {'menus':menus}
    return render(request, 'bell_app/indexMenu.html',content)

def createMenu(request):
    name = request.POST['MenuName']
    price = request.POST['MenuPrice']
    hot_ice = request.POST['MenuHotIce']
    new_menu = Menu(menu_name = name, menu_price = price, menu_hot_ice = hot_ice)
    new_menu.save()
    return HttpResponseRedirect(reverse('indexMenu'))

def deleteMenu(request):
    delete_menu_id = request.GET['menuNum']
    print("삭제한 menu의 id", delete_menu_id)
    menu = Menu.objects.get(id = delete_menu_id)
    menu.delete()
    return HttpResponseRedirect(reverse('indexMenu'))

def indexOrder(request):
    menus = Menu.objects.all()
    content = {'menus':menus}
    return render(request, 'bell_app/indexOrder.html',content)
    #return HttpResponse('input order page')
    
def createOrder(request):
    time = request.POST['OrderTime']
    menu = request.POST['OrderMenu']
    num = request.POST['OrderNum']
    #ing = request.POST['OrderIng']
    new_order = Order(order_time = time, order_menu = menu, order_num = num)
    new_order.save()
    return HttpResponseRedirect(reverse('indexOrder'))
    
    
def OrderList(request):
    orders = Order.objects.all()
    content = {'orders':orders}
    return render(request, 'bell_app/OrderList.html',content)

def updateOrder(request):
    finish_order_id = request.GET['orderNum']
    print("제조 완료된 order의 id", finish_order_id)
    order = Order.objects.get(id = finish_order_id)
    order.order_ing = False
    order.save()
    return HttpResponseRedirect(reverse('OrderList'))

def printQR(request):
    orders = Order.objects.all()
    content = {'orders':orders}
    return render(request, 'bell_app/printQR.html',content)