from django.http import JsonResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache

from .models import Category, Item , Cart
from .forms import EditItemForm, NewItemForm
# Create your views here.

# search
def items(request):
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    category_id = request.GET.get('category' , 0)
    sort_by = request.GET.get('sort_by','')
    from_price = request.GET.get('from_price', '')
    to_price = request.GET.get('to_price' , '')
    if from_price == '':
        from_price = 0
    if to_price == '':
        to_price = 100000000000

    if category_id != 0:
        items = items.filter(category_id=category_id)
        items = items.filter(price__gte=from_price , price__lte=to_price , category_id=category_id)
    else:
        items = items.filter(price__gte=from_price , price__lte=to_price)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    

    if (sort_by == 'asc'):
        items = sorted(items , key=lambda item: item.price)
    else:
        items = sorted(items, key=lambda item: item.price , reverse=True)
    
    

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        'sort_by' :sort_by,
        'from_price': from_price,
        'to_price': to_price,
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
            item.is_sold = False
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
def cart(request):
    cart = Cart.objects.filter(user = request.user)[0]
    items = cart.items.all()
    total_price = sum([x.price for x in items])
    stt = range(1 , len(items) + 1)
    items = zip(items, stt)
    return render(request, 'item/cart.html' , {
        'cart' : cart,
        'items' : items,
        'total_price' : total_price
    })

@login_required
def addCart(request , pk):
    item = Item.objects.get(pk=pk)
    page = request.GET.get('page' ,'')
    print(request.user)
    cart = Cart.objects.filter(user=request.user)
    if not cart.exists():
        c = Cart.objects.create(user = request.user)
        c.save()
    cart = Cart.objects.filter(user=request.user)[0]
    cart.items.add(item)
    cart.save()
    if page != '':
        return redirect("/items/" + str(pk))
    return redirect('/')

@login_required
@never_cache
def removecart(request,pk):
    try:
        cart = Cart.objects.filter(user = request.user)[0]
        item = cart.items.all()[pk - 1]
        print(item)
        total_price = sum([x.price for x in cart.items.all()])
        print(total_price)
        total_price -= item.price
        cart.items.remove(item)
        return JsonResponse({
            'status' : 'success',
            'total_price' : total_price
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

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