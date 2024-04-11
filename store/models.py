from django.utils import timezone
from django.db import models as m
from django.urls import reverse

from shop.settings import AUTH_USER_MODEL

# Create your models here.
  
class Product(m.Model):
    name=m.CharField(max_length=128)
    slug=m.SlugField(max_length=128)
    price=m.FloatField(default=0.0)
    stock=m.IntegerField(default=0)
    description=m.TextField(blank=True) 
    thumbnail=m.ImageField(upload_to='products',blank=True,null=True)
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("product",kwargs={"slug":self.slug})
    
class Order(m.Model):
    user=m.ForeignKey(AUTH_USER_MODEL,on_delete=m.CASCADE)
    product=m.ForeignKey(Product,on_delete=m.CASCADE)
    quantity=m.IntegerField(default=1)
    ordered=m.BooleanField(default=False)
    ordered_date=m.DateTimeField(blank=True,null=True)
    
    def __str__(self) -> str:
        return f"{self.product.name} {self.quantity}"

class Cart(m.Model):
    user=m.OneToOneField(AUTH_USER_MODEL,on_delete=m.CASCADE)#l'utilisateur ne peut créer qu'un seul panier
    orders=m.ManyToManyField(Order)
    
    
    
    def __str__(self):
        return self.user.username
    
    def delete (self,*args,**kwargs):
        for order in self.orders.all():
            order.ordered=True
            order.ordered_date=timezone.now()
            order.save()
        self.orders.clear()
        super().delete(*args,**kwargs)