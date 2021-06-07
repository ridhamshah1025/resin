from django.shortcuts import render,redirect
from products.models import Product,users,cart
# Create your views here.


def index(request):
    index = "yes"
    products = Product.objects.all()
    return render(request,"index.html",{'products':products, 'index':index})

def add_product(request):
    if request.method=="POST":
        products = Product.objects.all()
        return render(request,"index2.html",{'products':products})
    else:
        # return render(request,"index.html")
        # return redirect('index')
        products = Product.objects.all()
        return render(request,"index2.html",{'products':products})

def home(request):
    if request.session.has_key('user_id'):    
        products = Product.objects.all()
        user_id = request.session['user_id']
        all_cart_products = cart.objects.filter(user=user_id)
        return render(request,"add_product.html",{'products':products,'all_cart_products':all_cart_products})
    else:
        products = Product.objects.all()
        return render(request,"home.html",{'products':products})

def add_products(request):
    if request.method=="POST":
        user = users.objects.create(name=request.POST["name"])
        print(user.id)
        request.session['user_id'] = user.id
        products = Product.objects.all()
        return render(request,"add_product.html",{'products':products})
    else:
        if request.session.has_key('user_id'):    
            products = Product.objects.all()
            user_id = request.session['user_id']
            all_cart_products = cart.objects.filter(user=user_id)
            return render(request,"add_product.html",{'products':products,'all_cart_products':all_cart_products})
        else:
            return render(request,"home.html")

def add_cart(request):
    if request.method=="POST" and request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user_id = users.objects.get(pk=user_id)
        product_id=Product.objects.get(name=request.POST['p_name'])
        add_cart = cart.objects.create(user=user_id,product=product_id
                                   ,quantity=request.POST['quantity']
                                   ,total_price=request.POST['price'])
        products = Product.objects.all()
        all_cart_products = cart.objects.filter(user=user_id)
        return render(request,"add_product.html",{'products':products,'all_cart_products':all_cart_products})
    else:
        if request.session.has_key('user_id'):    
            products = Product.objects.all()
            user_id = request.session['user_id']
            all_cart_products = cart.objects.filter(user=user_id)
            return render(request,"add_product.html",{'products':products,'all_cart_products':all_cart_products})
        else:
            return render(request,"home.html")
    
