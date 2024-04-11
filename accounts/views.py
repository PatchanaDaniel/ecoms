from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model,login,logout,authenticate


# Create your views here.

def signup(request):
    User=get_user_model()
   
    msg=''
    if request.method=="POST":
       username=request.POST.get("username")
       password=request.POST.get("password")
       
       
       try:

         user=User.objects.create_user(username=username,password=password)
         login(request,user)
         return redirect('index')
       except:
          msg='Cet utilisateur existe déja'
          return render(request,'accounts/signup.html',{"msg":msg})
    
    return render(request,'accounts/signup.html')


def login_user(request):
   if request.method=="POST":
      username=request.POST.get("username")
      password=request.POST.get("password")
      user=authenticate(username=username,password=password)
      if user:
         login(request,user)
         return redirect('index')
      
   return render(request,'accounts/login.html')

def register(request):
   return render(request,'accounts/register.html')
 

def logout_user(request):
   logout(request)
   return redirect('index')
