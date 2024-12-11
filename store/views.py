from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Products, Bag

# Create your views here.
def index(request):
    products = Products.objects.all()
    if request.user.is_authenticated:
        bag = Bag.objects.filter(user=request.user)
        return render(request, 'index.html', {'products': products, 'bagCount': bag.count()})
    return render(request, 'index.html', {'products': products})

def loginV(request):
    if request.user.is_authenticated:
        return redirect('store:index')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'market/login.html', {'form': form})

def signup(request):
    if request.user.is_authenticated:
        return redirect('store:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'market/signup.html', {'form': form})

def logoutV(request):
    logout(request)
    return redirect('store:login')

def viewBag(request):
    if request.user.is_authenticated:
        bag = Bag.objects.filter(user=request.user)
        total_price = 0
        for item in bag:
            total_price += item.product.price * item.quantity
        return render(request, 'market/bag.html', {'bag_items': bag, 'total_price': total_price})
    else:
        return redirect('store:login')

def add_to_bag(request, product_id):
    if request.user.is_authenticated:
        product = Products.objects.get(id=product_id)
        
        if Bag.objects.filter(user=request.user, product=product).exists():
            bag = Bag.objects.get(user=request.user, product=product)
            bag.quantity += 1
            bag.save()
        else:
            bag = Bag(user=request.user, product=product, quantity=1)
            bag.save()
        return redirect('store:index')
    else:
        return redirect('store:login')

def remove_from_bag(request, product_id):
    if request.user.is_authenticated:
        bag = Bag.objects.get(user=request.user, id=product_id)
        if bag.quantity > 1:
            bag.quantity -= 1
            bag.save()
        else:
            bag.delete()
        return redirect('store:bag')
    else:
        return redirect('store:login')

def checkout(request):
    if request.user.is_authenticated:
        bag = Bag.objects.filter(user=request.user)
        total_price = 0
        for item in bag:
            total_price += item.product.price * item.quantity
        bag.delete()
        return render(request, 'market/checkout.html', {'total_price': total_price})