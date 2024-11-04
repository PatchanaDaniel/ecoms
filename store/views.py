from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from store.models import Cart, Order, Product , Category

# Create your views here.

def index(request):
    products=Product.objects.all()
    
    categories=Category.objects.all()

    return render(request,'store/index.html',{"products":products,"categories":categories})

def cat(request,id):
    if id==0:
        products=Product.objects.all()
    else:
        products=Product.objects.filter(category=id)
    
    categories=Category.objects.all()

    return render(request,'store/index.html',{"products":products,"categories":categories})

def product_detail(request,slug):
    product=get_object_or_404(Product,slug=slug)
    user=request.user
    a='addtocart' if user.is_authenticated else 'register'
    b= True if user.is_authenticated else False
    print (a)

   

    return render(request,'store/detail.html',{"product":product,"a":a,"b":b})
 
def add_to_cart(request,slug):
    user=request.user
    product=get_object_or_404(Product,slug=slug)
    cart,_=Cart.objects.get_or_create(user=user)
    order,created=Order.objects.get_or_create(user=user,ordered=False,product=product)
    if created:
        cart.orders.add(order)
        cart.save()  
    else:
        order.quantity+=1
        order.save()
    return redirect(reverse("product",kwargs={"slug":slug}))

def delete_order(request,id):
    Order.objects.get(id=id).delete()
    return redirect('cart')


def cart(request):
    cart=get_object_or_404(Cart,user=request.user)
    
    
    return render(request,'store/cart.html',context={"orders":cart.orders.all()})

def delete_cart(request):
    if cart := request.user.cart:
        orders=cart.orders.all()
        orders.delete() 

        
    return redirect("index")

def search(request):
    requete=request.GET.get('query')
    product=Product.objects.filter(name__contains=requete)
    
    return render(request,'store/search.html',context={"product":product})
