from django.urls import path

from . import views

app_name ='item'

urlpatterns = [
    path('<int:pk>/addCart/' , views.addCart , name = 'addCart'),
    path('cart/' , views.cart , name = 'cart'),
    path('<int:pk>/removecart/' , views.removecart , name = 'removecart'),
    path('new/' , views.new , name = 'new'),
    path('<int:pk>/', views.detail, name = 'detail'),
    path('<int:pk>/delete/' , views.delete , name = 'delete'),
    path('<int:pk>/edit/' , views.edit , name = 'edit'),
    path('' , views.items , name = 'items'),
]

