from django.contrib import admin
from .models import Category,Item,Cart , Orders,Feedback

# Register your models here.

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(Feedback)
