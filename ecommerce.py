from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
 
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    image = models.ImageField(null=True,blank=True)
    description = models.CharField(max_length=400,null=True)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey( Product,null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,default= 'PENDING')
    def __str__(self):
        return self.name
      
      Py manage.py makemigrations
Py manage.py migrate

from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 
 
class createorderform(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        exclude=['status']
 
class createproductform(ModelForm):
    class Meta:
        model=Product
        fields='__all__'
 
class createcustomerform(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']
        
        from django.contrib import admin
from .models import *
 
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)

import os
STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]

"""OnlineShopping URL Configuration
 
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website.views import *
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home ,name='home'),
    path('placeOrder/<str:i>/',placeOrder,name='placeOrder'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),
    path('addProduct/', addProduct,name='addProduct'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.http import HttpResponse
 
# Create your views here.
 
def home(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'website/home.html',context)
 
def placeOrder(request,i):
    customer= Customer.objects.get(id=i)
    form=createorderform(instance=customer)
    if(request.method=='POST'):
        form=createorderform(request.POST,instance=customer)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'website/placeOrder.html',context)
 
def addProduct(request):
    form=createproductform()
    if(request.method=='POST'):
        form=createproductform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'website/addProduct.html',context)
 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        customerform=createcustomerform()
        if request.method=='POST':
            form=createuserform(request.POST)
            customerform=createcustomerform(request.POST)
            if form.is_valid() and customerform.is_valid():
                user=form.save()
                customer=customerform.save(commit=False)
                customer.user=user 
                customer.save()
                return redirect('login')
        context={
            'form':form,
            'customerform':customerform,
        }
        return render(request,'website/register.html',context)
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'website/login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')
