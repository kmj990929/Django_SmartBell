from django.db import models

# Create your models here.
class Order(models.Model):
    order_time = models.DateField()
    order_menu = models.CharField(max_length = 100)
    order_num = models.IntegerField()
    order_ing = models.CharField(max_length = 100)
    
class Menu(models.Model):
    menu_name = models.CharField(max_length = 100) #메뉴 이름
    menu_price = models.IntegerField() #가격
    menu_hot_ice = models.BooleanField() # hot/ice
    
    