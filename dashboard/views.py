from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from item.models import Item,Orders
# Create your views here.

@login_required
def index(request):
    items = Item.objects.filter(created_by =request.user)
    orders = list(Orders.objects.filter(seller=request.user))
    itemsOrder = [order.item for order in orders]

    # my order 
    myorders = list(Orders.objects.filter(buyer=request.user))
    myorders_items = [myorder.item for myorder in myorders]
    myorders_times = [myorder.time_order for myorder in myorders]

    return render(request, 'dashboard/index.html' , {
        'items': items,
        'orders': orders,
        'itemsOrder': itemsOrder,
        'myorders': myorders,
        'myorders_items': myorders_items,
        'myorders_times': myorders_times,
    })

def detailOrder(request,pk):
    item = Item.objects.get(pk=pk)
    order = Orders.objects.filter(seller=request.user , item=item)[0]
    return render(request, 'dashboard/detailorder.html',{
        'order': order,
        'item': item,
    })