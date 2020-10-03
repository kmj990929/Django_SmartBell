from django.db import models

# Create your models here.
class Order(models.Model):
    order_time = models.DateField() #주문 시각
    order_menu = models.CharField(max_length = 100) #주문한 메뉴 명
    order_num = models.IntegerField() # 주문한 갯수
    order_ing = models.BooleanField(default = True) # 제조중/제조완료
    
class Menu(models.Model):
    menu_name = models.CharField(max_length = 100) #메뉴 이름
    menu_price = models.IntegerField() #가격
    menu_hot_ice = models.CharField(max_length = 50) # hot/ice
    
    