from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse

# Create your views here.
def index(request):
    menus = Menu.objects.all()
    content = {'menus':menus}
    return render(request, 'bell_app/index.html',content)

def createMenu(request):
    name = request.POST['MenuName']
    price = request.POST['MenuPrice']
    hot_ice = request.POST['MenuHotIce']
    new_menu = Menu(menu_name = name, menu_price = price, menu_hot_ice = hot_ice)
    new_menu.save()
    return HttpResponseRedirect(reverse('index'))

def deleteMenu(request):
    delete_menu_id = request.GET['menuNum']
    print("삭제한 menu의 id", delete_menu_id)
    menu = Menu.objects.get(id = delete_menu_id)
    menu.delete()
    return HttpResponseRedirect(reverse('index'))

def inputOrder(request):
    return HttpResponse('input order page')