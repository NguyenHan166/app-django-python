from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('' , views.index , name= 'index'),
    path('<int:pk>/detailOrder/' , views.detailOrder , name= 'detailOrder'),
    path('<int:pk>/detailMyorder/' , views.detailMyorder , name= 'detailMyorder'),
    path('<int:pk>/deleteOrder/' , views.deleteOrder , name= 'deleteOrder'),
]
