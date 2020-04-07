from django.shortcuts import render, redirect

from orders.models import Order
from .models import Cart
from products.models import Product
# Create your views here.

def cart_create(user=None):
    cart_obj= Cart.objects.create(user=None)
    return cart_obj

def cart_home(request):
    #request.session['cart_id']="12"
    #cart_id= request.session.get("cart_id", None)
    #print(cart_id)
    #print(request.session.session_key)
    """ cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    print(total)
    cart_obj.total = total
    cart_obj.save() """
    """ cart_id= request.session.get("cart_id", None)
    qs= Cart.objects.filter(id=cart_id)
    if  qs.count() == 1:
        print("ID cart exist")
        cart_obj= qs.first()
        if request.user.is_authenticated  and cart_obj.user is None:
            cart_obj.user= request.user
            cart_obj.save()
    else:
        print("Create new cart")
        #cart_obj= cart_create()
        cart_obj = Cart.objects.new_cart(user=request.user)
        request.session['cart_id']=cart_obj.id """
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html",{"cart":cart_obj})

def cart_update(request):
    #print("request",request.POST.get("product_id"))
    product_id= request.POST.get("product_id")
    if product_id is not None:
        try:
            product_obj= Product.objects.get(id=product_id)
            print("OBJEKT",product_obj)
        except Product.DoesNotExist:
            return redirect("cart:home")
        cart_obj, new_obj= Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items']=cart_obj.products.count()
    return redirect ("cart:home")

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:home")
    else:
        order_obj , new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    return render(request, "carts/checkout.html", { "object" : order_obj })

        
