from django.http import JsonResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Category, Item , Cart
from .forms import EditItemForm, NewItemForm
# Create your views here.

# search
def items(request):
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    category_id = request.GET.get('category' , 0)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category , is_sold = False).exclude(pk=pk)[0:3]

    return render(request , 'item/detail.html', {
        'item' : item,
        'related_items' : related_items,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST , request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail' ,pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html' , {
        'form' : form,
        'title': 'New Item',
    })

@login_required
def delete(request , pk):
    item = get_object_or_404(Item, pk=pk , created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

@login_required
def edit(request , pk):
    item = get_object_or_404(Item, pk=pk , created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST , request.FILES , instance=item)
        if form.is_valid():
            form.save()

            return redirect('item:detail' ,pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html' , {
        'form' : form,
        'title': 'Edit Item',
    })

@login_required
def cart(request):
    cart = Cart.objects.filter(user = request.user)[0]
    items = cart.items.all()
    total_price = sum([x.price for x in items])
    stt = range(1 , len(items) + 2)
    items = zip(items, stt)
    return render(request, 'item/cart.html' , {
        'cart' : cart,
        'items' : items,
        'total_price' : total_price
    })

@login_required
def addCart(request , pk):
    item = Item.objects.get(pk=pk)
    cart = Cart.objects.filter(user=request.user)[0]
    print(cart)
    cart.items.add(item)
    cart.save()
    return redirect('/')

@login_required
def removecart(request,pk):
    try:
        cart = Cart.objects.filter(user = request.user)[0]
        item = cart.items.all()[pk-1]
        print(item)
        cart.items.remove(item)
        return JsonResponse({
            'status' : 'success',
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})