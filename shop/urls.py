from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store.views import *
from shop import settings
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('signup/',signup,name='signup'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('cart/',cart,name='cart'),
    path('cart/delete',delete_cart,name='delete_cart'),
    path('cart/<int:id>/delete_order',delete_order,name='delete_order'),
    path('product/<str:slug>',product_detail,name='product'),
    path('product/<str:slug>/add_to_cart',add_to_cart,name='addtocart'),
    path('search/',search,name='search'),
    path('register/',register,name='register')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
