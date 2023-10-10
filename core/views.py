from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

from item.models import Item, Category,Cart
# Create your views here.
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    cart = Cart.objects.all()
    if not cart.exists() and request.user.is_authenticated:
        cart = Cart.objects.create(user = request.user)
        cart.save()
    return render(request, 'core/index.html',{
        'categories' : categories,
        'items' : items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    # khi da tao xong tk
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html' , {
        'form' : form,
    })

def logout(request):
    auth_logout(request)
    return redirect('/')
