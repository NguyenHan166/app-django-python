import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    # Cung cấp thêm thông tin bổ sung
    class Meta:
        ordering = ('name',) # Sắp xếp theo tên
        verbose_name_plural = 'Categories' # Thay đổi lại tên hiển thị trong adminpage

    def __str__(self):
        return self.name
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True , null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to='items_image', blank=True,null=True)
    # Biểu thị quan hệ giũa User và item , mỗi khi xóa 1 user thì sẽ xóa các item liên quan đến user đó
    created_by = models.ForeignKey(User , related_name='items',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    remaining_quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    items = models.ManyToManyField(Item)
    user = models.ForeignKey(User , related_name='cart' , blank=True, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('user',)
    def __str__(self):
        return 'Cart of ' + self.user.username

class Orders(models.Model):
    item = models.ForeignKey(Item , related_name='items', on_delete=models.CASCADE)
    seller = models.ForeignKey(User , related_name='seller' , on_delete=models.CASCADE)
    buyer = models.ForeignKey(User , related_name='buyer' , on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=50 , default='')
    address = models.CharField(max_length=1000 , default='')
    payment = models.CharField(max_length=50,default='cash')
    time_order = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    class Meta:
        ordering = ('buyer',)
    def __str__(self):
        return 'Order of ' + self.buyer.username
    
class Feedback(models.Model):
    content = models.CharField(max_length=10000000 , default='')
    item = models.ForeignKey(Item, related_name='feedback' , on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='feedback',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
    def __str__(self):
        return 'Feedback from '+ self.user.username + ' to ' + self.item.name