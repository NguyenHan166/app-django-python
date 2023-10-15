from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from item.models import Item,Orders
# Create your views here.

@login_required
def index(request):
    items = Item.objects.filter(created_by =request.user)
    orders = Orders.objects.filter(seller=request.user)[0]
    return render(request, 'dashboard/index.html' , {
        'items': items,
        'orders': orders
    })

def detailOrder(request,pk):
    pass