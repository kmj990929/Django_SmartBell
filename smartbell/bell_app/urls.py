# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 07:24:26 2020

@author: kmj99
"""

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    
    path('indexMenu/',views.indexMenu, name = 'indexMenu'),
    path('indexMenu/createMenu/', views.createMenu, name = 'createMenu'),
    path('indexMenu/deleteMenu/', views.deleteMenu, name = 'deleteMenu'),
    
    path('indexOrder/', views.indexOrder, name = 'indexOrder'),
    path('indexOrder/createOrder/', views.createOrder, name = 'createOrder'),
    path('indexOrder/OrderList/', views.OrderList, name = 'OrderList'),
    path('indexOrder/updateOrder/', views.updateOrder, name = 'updateOrder'),
    path('indexOrder/printQR/', views.printQR, name = 'printQR'),
]