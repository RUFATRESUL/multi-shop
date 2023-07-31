from django.shortcuts import render,redirect,get_object_or_404
from .models import Customer,WishItem
from .forms import RegisterForm,ContactForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from shop.models import Prouduct
from django.contrib.auth.decorators import login_required
# Create your views here.

def cart(request):
    return render(request,'cart.html')

def wishlist(request):
    return render(request,'wishlist.html')

@login_required
def wish_product(request,pk):
    product = get_object_or_404(Prouduct,pk=pk)
    customer =request.user.customer
    wishitem = WishItem.objects.filter(product=product,customer=customer).delete()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def unwish_product(request,pk):
    product = get_object_or_404(Prouduct,pk=pk)
    customer =request.user.customer
    wishitem = WishItem.objects.create(product=product,customer=customer)
    return redirect(request.META.get('HTTP_REFERER'))


def contact(request):
    form = ContactForm()
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'contact.html',{'form':ContactForm,'result':'success'})
        return render(request,'contact.html',{'form':form,'result':'fail'})
    return render(request,'contact.html',{'form':form})








def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            customer = form.save()
            login(request,customer.user)
            return redirect('customer:login')
    return render(request, 'register.html', {'form': form})





def login_view(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
         username = request.POST.get('username')
         password = request.POST.get('password')
         remember_me = request.POST.get('remember_me')
         user = authenticate(username=username,password=password)
         if user:
            login(request,user)
            nextUrl = request.GET.get('next')
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('shop:index')
         return render(request,'login.html',context={'unsuccess':True,'nextUrl':nextUrl})

             
           


    
def logout_view(request):
    logout(request)
    return redirect('customer:login')

    
