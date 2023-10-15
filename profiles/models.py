from django.contrib.auth.models import User
from django.db import models

from item.models import Orders

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orders = models.ForeignKey(Orders, related_name= 'orders',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username