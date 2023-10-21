from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

from item.models import Item, Category,Cart,Orders
# Create your views here.
from .forms import SignupForm
from profiles.models import UserProfile

def index(request):
    items = Item.objects.filter(is_sold=False)
    items = sorted(items , key= lambda x: x.created_at , reverse=True)
    categories = Category.objects.all()
    session_value = request.session.pop('messageBuy', None)  # Lấy giá trị của session và xóa nó
    return render(request, 'core/index.html',{
        'categories' : categories,
        'items' : items,
        'session_value' : session_value
    })

def contact(request):
    user = request.user
    return render(request, 'core/contact.html' ,{
        'user' : user,
    })

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
